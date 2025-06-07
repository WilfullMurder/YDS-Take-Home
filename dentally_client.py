import httpx
import logging
from models import Contact

DENTALLY_API_URL = "http://localhost:8001/customers"

def push_contact_to_dentally(contact: Contact) -> bool:
    logging.info(f"Pushing contact {contact.email} to Dentally...")
    try:
        response = httpx.post(DENTALLY_API_URL, json=contact.model_dump())
        response.raise_for_status()
        logging.info(f"Successfully pushed {contact.email}")
        return True
    except httpx.HTTPStatusError as e:
        logging.error(f"Dentally API error for {contact.email}: {e.response.text}")
    except Exception as e:
        logging.error(f"Unexpected error pushing {contact.email}: {e}")
    return False
