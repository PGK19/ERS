# ERS (Event Registration System)

A RESTful Event Registration System built using Django and Django REST Framework as part of my backend development internship. The project provides APIs to manage events and user registrations while demonstrating Django's ORM, model relationships, and REST API development.

## Features

- View all events
- View event details
- Register for an event
- View registered events
- Cancel registrations
- Django Admin panel for managing data

## Tech Stack

- Python 3.10
- Django 5.2
- Django REST Framework
- SQLite

## Project Structure

```
ERS/
├── ERS/
├── events/
├── manage.py
└── db.sqlite3
```

## API Endpoints

| Method | Endpoint |
|--------|----------|
| GET | `/events/` |
| GET | `/events/<id>/` |
| GET | `/registrations/` |
| POST | `/registrations/` |
| DELETE | `/registrations/<id>/` |

## Running the Project

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---
Built as part of my internship to learn Django backend development and REST API design.

## Key Concepts Practiced

- Django Models & ORM
- Database Relationships (Foreign Keys)
- REST API Development
- Django Admin
- CRUD Operations
