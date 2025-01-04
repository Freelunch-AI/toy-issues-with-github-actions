# Item Management API

A FastAPI application for managing items with admin authentication.

## Features

- Admin authentication using JWT tokens
- Create items (admin only)
- List items (public)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Usage

### Authentication

Get admin token:
```bash
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

### Items

Create item (requires admin token):
```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Item", "description": "Test Description", "price": 10.0}'
```

List all items (public):
```bash
curl "http://localhost:8000/items/"
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc