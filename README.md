# IMDB Sentiment Analysis

This project performs sentiment analysis on IMDB movie reviews using Natural Language Processing (NLP) techniques. The dataset is processed, vectorized using TF-IDF, and classified using the **Naive Bayes classifier**.

## Dataset
The dataset is extracted from the **IMDB Large Movie Review Dataset** ([source](https://ai.stanford.edu/~amaas/data/sentiment/)). It consists of positive and negative movie reviews.

## Installation & Dependencies
To run the project, install the required Python packages:
```bash
pip install pandas numpy scikit-learn requests
```

## Project Structure
- `sentiment_analysis.py`: Main script for downloading, processing, and training the model.
- `README.md`: Documentation for the project.

## Steps in the Analysis
1. **Download & Load Data**: Fetch the dataset from Stanford’s IMDB sentiment analysis dataset.
2. **Preprocessing**: Convert star ratings into binary sentiment labels (Positive/Negative).
3. **Train-Test Split**: 60% training, 20% validation, 20% testing.
4. **Vectorization**: Convert text into numerical features using TF-IDF.
5. **Train Model**: Use **Multinomial Naive Bayes** for classification.
6. **Evaluate Model**: Measure **accuracy, precision, recall, and F1-score**.

## Model Performance
```
Accuracy: 0.83
Precision: 0.86
Recall: 0.80
F1 Score: 0.83
```

## Next Steps
- Implement **Logistic Regression** for comparison.
- Optimize model performance with hyperparameter tuning.

## Author
Developed by [Fatemeh Ramazanian]

