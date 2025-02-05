# -*- coding: utf-8 -*-
"""TensorFlow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TLwpfGz9aVU5GASmt5rZyo5ydLqhTeC8
"""

import tensorflow as tf
import numpy as np
import pandas as pd
import requests
import io
import tarfile
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping

# Download and extract dataset
dataset_url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
response = requests.get(dataset_url)
with tarfile.open(fileobj=io.BytesIO(response.content), mode='r:gz') as tar:
    tar.extractall()

def load_imdb_data(folder):
    texts, labels = [], []
    for label in ['pos', 'neg']:
        folder_path = f"aclImdb/{folder}/{label}"
        for file in os.listdir(folder_path):
            with open(os.path.join(folder_path, file), encoding='utf-8') as f:
                texts.append(f.read())
                labels.append(1 if label == 'pos' else 0)
    return pd.DataFrame({'review_body': texts, 'sentiment': labels})

train_data = load_imdb_data('train')
test_data = load_imdb_data('test')

# Tokenization & Padding
vocab_size = 20000
max_length = 300  # Slightly increased for better context capture
tokenizer = Tokenizer(num_words=vocab_size, oov_token='<OOV>')
tokenizer.fit_on_texts(train_data['review_body'])

train_sequences = tokenizer.texts_to_sequences(train_data['review_body'])
test_sequences = tokenizer.texts_to_sequences(test_data['review_body'])

train_padded = pad_sequences(train_sequences, maxlen=max_length, padding='post', truncating='post')
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding='post', truncating='post')

train_labels = np.array(train_data['sentiment'])
test_labels = np.array(test_data['sentiment'])

# Define Optimized Model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 128, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True, dropout=0.3)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences=True, dropout=0.3)),
    tf.keras.layers.GlobalMaxPooling1D(),  # Replaces last LSTM layer to reduce overfitting
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile Model
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), metrics=['accuracy'])

# Callbacks
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=1e-6)
early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Train Model
history = model.fit(
    train_padded, train_labels,
    epochs=10,
    batch_size=32,
    validation_data=(test_padded, test_labels),
    callbacks=[reduce_lr, early_stop]
)

# Evaluate Model
y_pred = (model.predict(test_padded) > 0.5).astype('int32')
accuracy = accuracy_score(test_labels, y_pred)
precision = precision_score(test_labels, y_pred)
recall = recall_score(test_labels, y_pred)
f1 = f1_score(test_labels, y_pred)

# Print Metrics
print("Optimized TensorFlow Model Evaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")