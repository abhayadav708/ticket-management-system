from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    issue_title = Column(String, nullable=False)
    issue_description = Column(String, nullable=False)
    priority = Column(String, default="Medium")
    status = Column(String, default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)