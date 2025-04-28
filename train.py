# train.py
from models import train_and_save_model

if __name__ == "__main__":
    data_path = "data/combined_emails_with_natural_pii.csv"  # Correct dataset path
    model_path = "model/classifier.pkl"  # Where model will be saved

    train_and_save_model(data_path, model_path)
