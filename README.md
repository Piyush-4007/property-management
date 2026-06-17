# Estate — Property Rental Management System

**Version 1.0** — Core build

A FastAPI + SQLite application for property owners to manage rental
properties. This first version establishes the foundation: a working
backend with full CRUD and a basic HTML/CSS interface.

## What's in this version
- FastAPI backend with SQLite database (SQLAlchemy ORM)
- Property model: title, address, city, type, rent, status, image
- Full CRUD endpoints — GET, POST, PUT, DELETE
- HTML/CSS frontend pages served by FastAPI

## Stack
- Backend: Python, FastAPI, SQLAlchemy
- Database: SQLite
- Frontend: HTML + CSS

## Run it
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000

## Roadmap
- v2 — JWT authentication & secure, per-user data
- v3 — Image upload & redesigned dashboard
- v4 — Tenants, agreements & payment records