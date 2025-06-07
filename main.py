import logging
from fastapi import FastAPI, HTTPException
from hubspot_client import fetch_contacts_from_hubspot
from dentally_client import push_contact_to_dentally
from models import Contact

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

@app.post("/sync")
def sync_contacts():
    logging.info("Starting contact sync...")
    try:
        contacts = fetch_contacts_from_hubspot()
        logging.info(f"Fetched {len(contacts)} contacts from HubSpot.")
    except Exception as e:
        logging.error(f"Error fetching contacts from HubSpot: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch contacts from HubSpot.")

    results = []
    for contact in contacts:
        try:
            logging.info(f"Syncing contact {contact.email}...")
            success = push_contact_to_dentally(contact)
            results.append({"email": contact.email, "synced": success})
            logging.info(f"Contact {contact.email} sync result: {'Success' if success else 'Failure'}")
        except Exception as e:
            logging.error(f"Error syncing contact {contact.email}: {e}")
            results.append({"email": contact.email, "synced": False})

    logging.info("Contact sync completed.")
    return {"results": results}


@app.post("/customers")
def receive_customer(contact: Contact):
    logging.info(f"Received customer data: {contact.dict()}")
    return {"message": f"Received {contact.email}"}
