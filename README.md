Ticket-management-system
A FastAPI-based Ticket Management System with SQLite and SQLAlchemy for creating, tracking, updating, and deleting customer support tickets through REST APIs.

# Ticket Management System

A backend REST API project built using **FastAPI**, **SQLite**, **SQLAlchemy**, and **Python**.

## Project Overview

Ticket Management System is a customer support backend application that allows users to create, view, update, and delete support tickets. It helps support teams manage customer issues in a structured way by tracking ticket priority, status, and creation time.

## Features

- Create new support tickets
- View all tickets
- View a ticket by ID
- Update ticket status
- Delete tickets
- Track ticket priority
- Auto-generate ticket creation time
- SQLite database integration
- REST API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Folder Structure

text
ticket-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── requirements.txt
├── README.md
└── .gitignore
