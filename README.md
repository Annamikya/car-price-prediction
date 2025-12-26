# Car Price Prediction Project

Project structure

```
car_price_project/
│
├── backend/
│   ├── app.py
│   ├── model.pkl  <-- paste your trained binary model here (from Colab)
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

## Setup (backend)

1. Paste your trained `model.pkl` (binary) into `backend/model.pkl`.
2. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

3. Run the API:

```bash
uvicorn app:app --reload
```

4. Open the docs to test endpoints:

- http://127.0.0.1:8000/docs
- Health: `GET /health`
- Predict: `POST /predict` with JSON body matching input schema

## Frontend

- Option 1 (recommended): Install Live Server extension in VS Code and "Open with Live Server" on `frontend/index.html`.
- Option 2: Open `frontend/index.html` directly in a browser.

The frontend posts to `http://127.0.0.1:8000/predict`.

## Notes
- Replace the placeholder `backend/model.pkl` with your actual trained model file (binary) from Colab before running the API. The placeholder file is non-functional.

Enjoy! 🚗