from pydantic import BaseModel, EmailStr
from datetime import datetime


class TicketCreate(BaseModel):
    customer_name: str
    email: EmailStr
    issue_title: str
    issue_description: str
    priority: str = "Medium"


class TicketUpdate(BaseModel):
    status: str


class TicketResponse(BaseModel):
    id: int
    customer_name: str
    email: EmailStr
    issue_title: str
    issue_description: str
    priority: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True