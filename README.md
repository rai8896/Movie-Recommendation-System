# 🎬 Movie Recommendation System

A simple and interactive **Movie Recommendation System** built using **Machine Learning + Streamlit**.
This app recommends 5 similar movies based on the movie selected by the user.

---

## 🚀 Live Demo

👉 **Live App:** https://movie-recommendation-manishrai.streamlit.app/

---

## 📌 Features

* Recommends top 5 similar movies
* Fast similarity search using precomputed similarity matrix
* Clean and simple Streamlit UI
* Lightweight model using `joblib` compression
* Easy deployment on Streamlit Cloud

---

## 🧠 How It Works

The system uses **Content-Based Filtering**:

1. Movie data is processed and converted into vectors
2. Cosine similarity is calculated between movies
3. Similarity matrix is stored using `joblib`
4. When a movie is selected, top similar movies are recommended

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib / Pickle

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/rai8896/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📦 Requirements.txt

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## &#x20;

## 👨‍💻 Author

**Manish Rai**<br>
M.Tech (Artificial Intelligence) – Delhi Technological University (DTU)<br>

  

