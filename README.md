# ShopMate

ShopMate is an e-commerce application with a React frontend, a Django REST API, a SQLite database, and Gemini-powered product description generation.

## Requirements

- Python 3.10 or newer
- Node.js and npm
- A Gemini API key for the AI description feature

## Project structure

- `server/` contains the Django project, product API, database, migrations, and Gemini service.
- `client/` contains the React and Vite frontend.

## Backend setup

Open PowerShell in the project root and run:

```powershell
cd server
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `server/.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

Create or update the database tables:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Add the sample products. The command replaces the existing seeded products:

```powershell
python manage.py seed_products
```

Start the Django backend on port `8000`:

```powershell
python manage.py runserver 8000
```

The backend is available at `http://127.0.0.1:8000/`.

## Frontend setup

Keep the backend terminal running and open a second PowerShell terminal:

```powershell
cd client
npm install
npm run dev
```

Open the Vite address displayed in the terminal, usually `http://localhost:5173/`.

The frontend is configured to use the Django API on port `8000`. Start both the backend and frontend before using the application.
