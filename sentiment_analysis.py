# -*- coding: utf-8 -*-
"""IMDB-Sentiment-Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mn927y8GovBMX_il72f95pSCW_8xQCAs
"""

import pandas as pd
import numpy as np
import requests
import tarfile
import os
import io
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

# Download and extract the dataset
dataset_url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
response = requests.get(dataset_url)
tar = tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz")
tar.extractall("aclImdb")  # Content extraction
tar.close()

# Function to read data from text files
def load_imdb_data(directory, label):
    texts = []
    labels = []
    path = f"aclImdb/{directory}"
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), "r", encoding="utf-8") as file:
            texts.append(file.read())
            labels.append(label)
    return texts, labels

# Load data from the train and test folders
train_pos_texts, train_pos_labels = load_imdb_data("aclImdb/train/pos", 1)
train_neg_texts, train_neg_labels = load_imdb_data("aclImdb/train/neg", 0)
test_pos_texts, test_pos_labels = load_imdb_data("aclImdb/test/pos", 1)
test_neg_texts, test_neg_labels = load_imdb_data("aclImdb/test/neg", 0)

# Create a dataframe
train_data = pd.DataFrame({"review": train_pos_texts + train_neg_texts, "sentiment": train_pos_labels + train_neg_labels})
test_data = pd.DataFrame({"review": test_pos_texts + test_neg_texts, "sentiment": test_pos_labels + test_neg_labels})

# Division into train, validation, test
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42, stratify=train_data["sentiment"])
test_data, val_data = train_test_split(test_data, test_size=0.5, random_state=42, stratify=test_data["sentiment"])

# Remove text and labels
X_train, y_train = train_data["review"], train_data["sentiment"]
X_val, y_val = val_data["review"], val_data["sentiment"]
X_test, y_test = test_data["review"], test_data["sentiment"]

# Text vectorization with TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)
X_test_vec = vectorizer.transform(X_test)

# Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Model performance report
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred):.2f}")
print(f"Recall: {recall_score(y_test, y_pred):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.2f}")