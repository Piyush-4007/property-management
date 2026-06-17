# Estate — Property Rental Management System

**Version 4.0** — Complete system

The full Property Rental Management System. On top of secure, image-rich
property management, this version completes the brief with tenants, rental
agreements, and payment records — everything an owner needs in one place.

## What's new in v4
- Tenant records and management
- Rental agreements linking properties to tenants
- Payment records and tracking
- Unified dashboard across the full rental workflow

## The complete feature set
- Full CRUD — GET, POST, PUT, DELETE — across all entities
- JWT authentication with per-user data isolation
- Image upload for property listings
- Modern HTML/CSS dashboard with portfolio stats

## Stack
- Backend: Python, FastAPI, SQLAlchemy
- Auth: JWT (python-jose), bcrypt (passlib)
- Database: SQLite
- Frontend: HTML + CSS

## Project structure
```
property-management/
├── main.py            # FastAPI app: auth, CRUD, upload, pages
├── database.py        # SQLite + SQLAlchemy setup
├── models.py          # User, Property (+ tenants, agreements, payments)
├── schemas.py         # Pydantic request/response models
├── auth.py            # password hashing + JWT
├── requirements.txt
├── frontend/          # HTML pages
└── static/            # CSS, JS, uploaded images
```

## Run it
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000
Demo login: **demo@rental.app** / **demo1234**

## API
Interactive docs at http://127.0.0.1:8000/docs