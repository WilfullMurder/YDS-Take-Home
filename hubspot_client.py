import logging
from typing import List
from models import Contact

def fetch_contacts_from_hubspot() -> List[Contact]:
    logging.info("Fetching contacts from HubSpot...")
    try:
        return [
            Contact(id="1", first_name="Alice", last_name="Smith", email="alice@example.com"),
            Contact(id="2", first_name="Bob", last_name="Jones", email="bob@example.com"),
        ]
    except Exception as e:
        logging.error(f"Failed to fetch contacts: {e}")
        return []
