# YDS Take Home

A lightweight FastAPI service that syncs customer contact data between two systems: HubSpot and a mock Dentally API.

Fetches new contact records from a mocked HubSpot API and pushes them to a mock Dentally API endpoint. Includes simple logging, error handling, and unit tests.

## Features

- FastAPI-based REST service
- Pulls customer contacts from a mock HubSpot API
- Pushes them to a mock Dentally endpoint
- Designed to be easy to run and test
- Includes unit tests using pytest

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/WilfullMurder/YDS-Take-Home.git <local-repo-name>
cd <local-repo-name>
```
### 2. Set up a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Service
Start the FastAPI server
```bash
uvicorn main:app --reload
```
You should see output like:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000
```


## Triggering a Sync

In a new terminal (while the server is running), send a POST request to the /sync endpoint:
```bash
curl -X POST http://127.0.0.1:8000/sync
```
Expected response:
```bash
{
  "results": [
    { "email": "alice@example.com", "synced": true },
    { "email": "bob@example.com",   "synced": true }
  ]
}
```
These mock contacts are fetched from the HubSpot client and forwarded to the simulated Dentally API.

## Running Tests

This project includes unit tests for the sync function.

To run the tests:
```bash
pytest
```
Sample output:
```
collected 2 items
test_sync.py ..                                     [100%]

========== 1 passed in 0.04s ==========
```
Requirements
```
    Python 3.8+

    pip
```
All dependencies are listed in requirements.txt and include:
```
    fastapi

    uvicorn

    httpx

    pytest
```
