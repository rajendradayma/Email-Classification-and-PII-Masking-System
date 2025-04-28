# utils.py
import re

def mask_pii(text):
    entities = []
    original_text = text

    # Define patterns
    patterns = {
        "full_name": r"(?:(?:Mr|Ms|Mrs|Dr)\\.?\s)?[A-Z][a-z]+(?:\s[A-Z][a-z]+)+",
        "email": r"[\\w\\.-]+@[\\w\\.-]+",
        "phone_number": r"(\\+91[-\\s]?)?[6-9]\\d{9}",
        "dob": r"(\\d{2}[/-]\\d{2}[/-]\\d{4})",
        "aadhar_num": r"\\d{4}\\s\\d{4}\\s\\d{4}",
        "credit_debit_no": r"\\d{4}[-\\s]\\d{4}[-\\s]\\d{4}[-\\s]\\d{4}",
        "cvv_no": r"\\b\\d{3}\\b",
        "expiry_no": r"(0[1-9]|1[0-2])/\\d{2}"
    }

    masked_text = text

    for entity, pattern in patterns.items():
        for match in re.finditer(pattern, original_text):
            start, end = match.span()
            matched_text = match.group()

            entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": matched_text
            })

            masked_text = masked_text.replace(matched_text, f"[{entity}]", 1)

    return masked_text, entities

def unmask_pii(masked_text, entities):
    unmasked_text = masked_text
    for ent in entities:
        unmasked_text = unmasked_text.replace(f"[{ent['classification']}]", ent['entity'], 1)
    return unmasked_text
