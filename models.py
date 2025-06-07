from pydantic import BaseModel

class Contact(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
