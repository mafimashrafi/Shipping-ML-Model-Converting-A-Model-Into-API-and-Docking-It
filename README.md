# 🚀 Insurance Premium Predictor — Serving an ML Model with FastAPI & Docker

A production-style machine learning system that predicts **insurance premiums** based on India's insurance dataset. The project demonstrates the full journey from a trained model to a containerized, API-served application with a frontend interface.

---

## 📌 Overview

Most ML projects stop at the notebook. This one doesn't.

This project takes a trained regression model and ships it as a real service — with a clean REST API, input validation, a user-facing UI, and a fully containerized deployment. The dataset reflects fragmented, real-world insurance data from India, making preprocessing and validation a core part of the pipeline.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│                  User                        │
└──────────────────┬──────────────────────────┘
                   │
         ┌─────────▼──────────┐
         │  Streamlit Frontend │  ← Interactive UI for input
         └─────────┬──────────┘
                   │ HTTP Request
         ┌─────────▼──────────┐
         │   FastAPI Backend   │  ← REST API + Pydantic validation
         └─────────┬──────────┘
                   │
         ┌─────────▼──────────┐
         │    ML Model (.pkl)  │  ← Trained regression model
         └────────────────────┘

      All services orchestrated via Docker Compose
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Data Validation | Pydantic |
| Frontend | Streamlit |
| Containerization | Docker + Docker Compose |
| ML & Data | Scikit-learn, Pandas, NumPy |
| Environment | Python 3.x |

---

## 📁 Project Structure

```
├── Backend/
│   └── main.py              # FastAPI app — routes, prediction logic
├── Frontend/
│   └── app.py               # Streamlit UI
├── Model/
│   └── model.pkl            # Serialized trained model
├── Data/
│   └── insurance.csv        # India insurance dataset
├── Notebooks/
│   └── training.ipynb       # EDA, preprocessing, model training
├── Dockerfile               # Container image definition
├── docker-compose.yml       # Multi-service orchestration
├── .dockerignore
├── .gitignore
└── requirements.txt
```

---

## ✨ Features

- **REST API** — `/predict` endpoint accepts JSON and returns a premium estimate
- **Input Validation** — Pydantic schemas reject malformed or out-of-range inputs before they reach the model
- **Streamlit UI** — A simple frontend to interact with the model without writing any code
- **Fully Containerized** — Both the backend and frontend run as isolated Docker services, orchestrated with Compose
- **Clean Separation** — Model, API, and UI are decoupled into separate layers

---

## ⚙️ Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) installed
- [Docker Compose](https://docs.docker.com/compose/) installed

### Run the Application

```bash
# 1. Clone the repository
git clone https://github.com/mafimashrafi/Shipping-ML-Model-Converting-A-Model-Into-API-and-Docking-It.git
cd Shipping-ML-Model-Converting-A-Model-Into-API-and-Docking-It

# 2. Build and start all services
docker-compose up --build
```

Once running:
- **Streamlit UI** → `http://localhost:8501`
- **FastAPI Docs** → `http://localhost:8000/docs`

---

## 🔌 API Reference

### `POST /predict`

Accepts patient/policyholder features and returns a predicted insurance premium.

**Request Body:**
```json
{
  "age": 28,
  "income": 450000,
  "bmi": 24.5,
  "region": "northeast",
  "smoker": false,
  "dependents": 1
}
```

> ⚠️ Fields and types may vary based on the dataset features used during training. See `/docs` for the live Swagger schema.

**Response:**
```json
{
  "predicted_premium": 12340.75
}
```

---

## 🧠 Model & Dataset

The model is trained on a fragmented insurance dataset reflecting real-world conditions in India, where missing values, inconsistent entries, and regional variation are common challenges.

**Training pipeline (see `Notebooks/`):**
1. Exploratory Data Analysis (EDA)
2. Handling missing values and inconsistent data
3. Feature encoding and scaling
4. Model training and serialization

---

## 💡 Key Engineering Decisions

- **Why FastAPI?** Async-capable, auto-generates OpenAPI docs, and integrates naturally with Pydantic for strict input contracts.
- **Why Pydantic validation?** Real-world insurance data is messy. Validating at the API boundary prevents corrupt inputs from ever reaching the model.
- **Why Docker Compose?** Keeps the frontend and backend as separate, independently deployable services while keeping local development simple.

---

## 📚 What I Learned

- How to design and structure a multi-service ML application
- The importance of input validation in production ML pipelines
- Containerizing Python services and managing inter-service communication
- Separating model training concerns from serving concerns

---

## 👤 Author

**Mashrafi Rahman**
[LinkedIn](https://www.linkedin.com/in/mashrafi-rahman-mafi) · [GitHub](https://github.com/mafimashrafi)
