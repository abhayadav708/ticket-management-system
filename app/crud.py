from sqlalchemy.orm import Session
from app.models import Ticket
from app.schemas import TicketCreate, TicketUpdate


def create_ticket(db: Session, ticket: TicketCreate):
    new_ticket = Ticket(
        customer_name=ticket.customer_name,
        email=ticket.email,
        issue_title=ticket.issue_title,
        issue_description=ticket.issue_description,
        priority=ticket.priority,
        status="Open"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket_status(db: Session, ticket_id: int, ticket_update: TicketUpdate):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket:
        ticket.status = ticket_update.status
        db.commit()
        db.refresh(ticket)

    return ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket:
        db.delete(ticket)
        db.commit()

    return ticket