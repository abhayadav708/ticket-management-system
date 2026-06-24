from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.schemas import TicketCreate, TicketUpdate, TicketResponse
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ticket Management System",
    description="A FastAPI-based customer support ticket management system",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Ticket Management System API is running"
    }


@app.post("/tickets", response_model=TicketResponse)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)


@app.get("/tickets", response_model=list[TicketResponse])
def read_all_tickets(db: Session = Depends(get_db)):
    return crud.get_all_tickets(db)


@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket_by_id(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@app.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    ticket = crud.update_ticket_status(db, ticket_id, ticket_update)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@app.delete("/tickets/{ticket_id}")
def remove_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.delete_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "message": "Ticket deleted successfully"
    }