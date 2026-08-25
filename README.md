# ShopMateTaskPython

A teaching-ready e-commerce application for learning how to add Generative AI features with Python.

## Architecture

- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** Django + Django REST Framework
- **Database:** SQLite for simple local setup
- **GenAI:** Gemini through the Google GenAI Python SDK

The `client/` application is kept as the existing React frontend. The backend is implemented in `server/` with Django.

```text
React
  |
  | HTTP / JSON
  v
Django REST Framework
  |
  +-- Products ----> SQLite
  |
  +-- AI services ----> Gemini
```

## Project structure

```text
ShopMateTaskPython/
├── client/                  # Existing React frontend
└── server/
    ├── manage.py
    ├── config/              # Django project configuration
    ├── products/            # Product model and REST API
    ├── ai/                  # Gemini integration and future AI lessons
    ├── requirements.txt
    └── .env.example
```

## Run the backend

```bash
cd server
python -m venv venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Gemini API key when you are ready to use the AI endpoint.

Run migrations:

```bash
python manage.py migrate
```

Seed the ShopMate products:

```bash
python manage.py seed_products
```

Start Django on port **3001** so the existing React frontend can be used without changing its API URLs:

```bash
python manage.py runserver 3001
```

## Run the frontend

In another terminal:

```bash
cd client
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

## Existing product API

```text
GET    /api/products/
GET    /api/products/?search=headphones
GET    /api/products/<id>/
POST   /api/products/
PUT    /api/products/<id>/
DELETE /api/products/<id>/
```

The API deliberately returns `_id` as the product identifier so the existing React code can remain unchanged.

## First Gemini endpoint

Once `GEMINI_API_KEY` is configured:

```text
POST /api/ai/generate/
Content-Type: application/json

{
  "prompt": "Explain why noise cancelling headphones are useful for travel."
}
```

Response:

```json
{
  "text": "..."
}
```

This endpoint is intentionally small. Students can build on the `ai/services/gemini.py` abstraction in later lessons for prompt engineering, structured output, product recommendations, tool calling, and RAG.
