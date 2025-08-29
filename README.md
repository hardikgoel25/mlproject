# ML Project – API + Streamlit Frontend

## 🌐 Live Demo

* **Flask API (Backend):** [https://mlproject-2rmf.onrender.com](https://mlproject-2rmf.onrender.com)
* **Streamlit App (Frontend):** [https://mlproject-cjkjgtqc75uqkscwpeiwzr.streamlit.app/](https://mlproject-cjkjgtqc75uqkscwpeiwzr.streamlit.app/)

---

## 📖 Project Overview

This project demonstrates a full‑stack Machine Learning workflow:

* **Model Inference API** built using **Flask**, deployed on **Render**.
* **Interactive Frontend** built using **Streamlit**, deployed on **Streamlit Cloud**.
* **Environment Variables** are used for secure API communication.

---

## ⚙️ Tech Stack

* **Backend:** Flask + Gunicorn (Render)
* **Frontend:** Streamlit (Streamlit Cloud)
* **Language:** Python 3.12+
* **Deployment:** Render (API) + Streamlit Cloud (UI)

---

## 📂 Project Structure

```
├── application.py        # Flask API entrypoint
├── app.py                # Streamlit frontend
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (not committed)
├── README.md             # Project documentation
└── model/                # Trained ML model + preprocessing
```

---

## 🔑 Environment Variables

Both services rely on environment variables:

### Render (Flask API)

```
FLASK_ENV=production
FLASK_APP=application.py
FLASK_RUN_PORT=5000
SECRET_KEY=supersecret123
```

### Streamlit Cloud (Frontend)

```
API_URL=https://mlproject-2rmf.onrender.com
```

Add them under **Render → Environment → Secret Files / Variables** and **Streamlit → Advanced Settings → Secrets**.

---

## ▶️ Running Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/mlproject.git
   cd mlproject
   ```

2. Create a virtual environment & install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   pip install -r requirements.txt
   ```

3. Run Flask API locally:

   ```bash
   flask run
   ```

   or with gunicorn:

   ```bash
   gunicorn application:app
   ```

4. Run Streamlit frontend locally:

   ```bash
   streamlit run app.py
   ```

---

## 🚀 Deployment Notes

* **Flask API on Render:** Make sure the Start Command is `gunicorn application:app`.
* **Streamlit App:** Set `API_URL` secret to your deployed Flask Render URL.

---

## 👤 Author

Developed by **Hardik Goel**
