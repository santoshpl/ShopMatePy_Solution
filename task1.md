# Task 1: Product Description Generation

## Objective

Add an AI-assisted feature that generates a product description from the product name and category. The generated text should be placed into the product form so an administrator can review or edit it before saving.

## Backend work

Implement the feature in the Django backend:

- Add or update the Gemini service in `server/ai/services/gemini.py`.
- Add the description-generation view in `server/ai/views.py`.
- Register the endpoint in `server/ai/urls.py`.
- Include the AI URL configuration in the main Django URL configuration.
- Read the Gemini API key from the server environment configuration.

The backend endpoint is:

`POST http://127.0.0.1:8000/api/ai/generate/`

The request uses the product `name` and `category`. The response returns the generated `description`.

## Frontend work

Update the Admin Dashboard in `client/src/pages/AdminDashboard.jsx`:

- Add a **Generate with AI** button beside the description field.
- Require the administrator to enter a product name and category before generating text.
- Show a loading state while the request is running.
- Place the returned description into the description field.
- Show a useful error message when the request fails.
- Allow the administrator to edit the generated text before saving the product.

The frontend must use the Django backend on port `8000`.

## Configuration

Create `server/.env` and provide a valid Gemini API key. Restart the Django server after changing the environment file.

Both services must be running:

- Django backend: `http://127.0.0.1:8000/`
- React frontend: the Vite URL shown after starting the client

## Verification checklist

- The backend starts successfully on port `8000`.
- The frontend loads products from the backend.
- The Admin Dashboard opens the add-product form.
- The Generate with AI button is disabled while a request is in progress.
- A product name and category are required before generation.
- A generated description appears in the description field.
- The generated description can be edited and saved with the product.
- Missing credentials or backend failures produce a visible error message.
