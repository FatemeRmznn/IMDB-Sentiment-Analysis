# IMDB Sentiment Analysis

This repository contains various models to perform sentiment analysis on the IMDB movie reviews dataset.he goal is to classify movie reviews as positive or negative using different machine learning and deep learning techniques.
## Dataset

The IMDB dataset consists of 50,000 movie reviews labeled as positive or negative.t is commonly used for binary sentiment classification tasks.

## Models Implemented

1. **Naive Bayes Model (`sentiment_analysis_nb.py`)**:
   - Utilizes a Multinomial Naive Bayes classifier with TF-IDF vectorization.
2. **Logistic Regression Model (`LogisticRegression.py`)**:
   - Employs Logistic Regression with TF-IDF vectorization for sentiment classification.
3. **TensorFlow Model (`TensorFlow.py`)**:
   - Implements a deep learning model using TensorFlow and Keras, featuring an embedding layer followed by Bidirectional LSTM layers.
## Requirements

o install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

1. **Naive Bayes Model**:
   - Execute `sentiment_analysis_nb.py` to train and evaluate the Naive Bayes model.
2. **Logistic Regression Model**:
   - Run `LogisticRegression.py` to train and assess the Logistic Regression model.
3. **TensorFlow Model**:
   - Use `TensorFlow.py` to train and evaluate the deep learning model.
Each script is self-contained and can be run independently.nsure that the IMDB dataset is properly loaded and preprocessed as required by each model.
## Results

The performance of each model is evaluated using metrics such as accuracy, precision, recall, and F1 score.etailed results can be found within the respective scripts.
## License

This project is licensed under the MIT License.
## Acknowledgments

The IMDB dataset is provided by Stanford and is available [here](https://ai.stanford.edu/~amaas/data/sentiment/).
