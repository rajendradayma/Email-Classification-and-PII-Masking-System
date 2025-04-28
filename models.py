# model.py
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def train_and_save_model(data_path, model_path):
    # Load dataset
    df = pd.read_csv(data_path)

    # Rename columns
    df.rename(columns={'email': 'email_body', 'type': 'category'}, inplace=True)

    X = df['email_body']
    y = df['category']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build pipeline
    clf_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Train model
    clf_pipeline.fit(X_train, y_train)

    # Evaluate model
    y_pred = clf_pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Validation Accuracy: {acc:.4f}")

    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf_pipeline, model_path)

def load_model(model_path):
    return joblib.load(model_path)


