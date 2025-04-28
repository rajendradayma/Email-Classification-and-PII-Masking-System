# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii, unmask_pii
from models import load_model


# Create FastAPI app
app = FastAPI()

# Load the trained model at startup
model = load_model("model/classifier.pkl")

# Define request schema
class EmailRequest(BaseModel):
    email_body: str

# Define the API endpoint
@app.post("/predict")
def classify_email(req: EmailRequest):
    email_text = req.email_body

    # Step 1: Mask PII
    masked_text, entities = mask_pii(email_text)

    # Step 2: Predict Category
    category = model.predict([masked_text])[0]

    # Step 3: Build the response
    response = {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }

    return response
