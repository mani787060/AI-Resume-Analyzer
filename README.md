# AI Resume Analyzer 🚀

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-green.svg)](https://spacy.io/)
[![Database](https://img.shields.io/badge/Database-TiDB%20Cloud-orange.svg)](https://www.pingcap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

# 📌 Project Overview

**AI Resume Analyzer** is an intelligent resume screening and analysis platform that leverages **Natural Language Processing (NLP)** and **Machine Learning-driven resume intelligence** to evaluate resumes, extract candidate information, provide optimization recommendations, and generate actionable insights.

The application automatically processes uploaded PDF resumes, identifies key resume sections, calculates resume scores, recommends improvements, and stores all candidate interactions in a scalable cloud database.

Built using **Streamlit**, **spaCy**, **NLTK**, **PyMuPDF**, and **TiDB Cloud Serverless**, this project demonstrates a complete end-to-end AI-powered recruitment analytics workflow.

---

# 🎯 Objectives

* Automate resume screening and evaluation
* Extract candidate information from PDF resumes
* Analyze resume quality and completeness
* Provide personalized improvement suggestions
* Generate recruiter-friendly candidate insights
* Store candidate analytics in a cloud-native database
* Create a scalable AI-powered hiring assistant

---

# ✨ Key Features

## 📄 Resume Upload & Parsing

* Upload PDF resumes directly through the Streamlit interface
* Support for multi-page PDF documents
* Fast text extraction using PyMuPDF

---

## 🧠 NLP-Based Information Extraction

Automatically identifies and extracts:

* Name
* Email Address
* Phone Number
* Skills
* Education
* Experience
* Projects
* Certifications
* Achievements
* Hobbies
* Objectives
* Declarations

using NLP techniques powered by **spaCy** and **NLTK**.

---

## 📊 Resume Scoring Engine

The application dynamically evaluates resumes based on:

* Skills Availability
* Project Information
* Work Experience
* Certifications
* Resume Completeness
* Professional Sections

and generates a resume score with improvement recommendations.

---

## 📈 Recruiter Analytics Dashboard

Visual dashboards help recruiters analyze:

* Candidate Profiles
* Resume Scores
* Skill Distributions
* Experience Levels
* Resume Statistics

using interactive charts and graphs.

---

# 🏗️ System Architecture

```text
                 ┌────────────────────────────┐
                 │     Candidate Uploads      │
                 │        PDF Resume          │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │    PyMuPDF PDF Parser      │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │      Text Extraction       │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │      NLP Processing        │
                 │      spaCy + NLTK          │
                 └─────────────┬──────────────┘
                               │
               ┌───────────────┼───────────────┐
               │               │               │
               ▼               ▼               ▼

         Skill Mining     Section Parsing   Contact Extraction

               └───────────────┬───────────────┘
                               ▼

                 ┌────────────────────────────┐
                 │     Resume Scoring Engine  │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │ Recommendation Generator   │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │  Streamlit Interactive UI  │
                 └─────────────┬──────────────┘
                               │
                               ▼

                 ┌────────────────────────────┐
                 │   TiDB Cloud Database      │
                 └────────────────────────────┘
```

---

# ⚙️ Technology Stack

## Frontend

* Streamlit

## Natural Language Processing

* spaCy
* NLTK

## Document Processing

* PyMuPDF (fitz)
* PDFMiner

## Database

* TiDB Cloud Serverless
* PyMySQL

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly
* Matplotlib


---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Streamlit Secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
admin_user="your_admin_username"

admin_password="your_admin_password"

db_host="your_tidb_host"

db_user="your_tidb_user"

db_password="your_tidb_password"

db_database="cv"

db_port=4000
```

---

## 5️⃣ Launch Application

```bash
streamlit run app.py
```

---

# 🏁 Conclusion

AI Resume Analyzer demonstrates how Natural Language Processing, Cloud Databases, and Interactive Dashboards can be combined to automate resume evaluation and candidate profiling.

The project serves as a practical example of building production-ready AI applications that solve real-world recruitment and talent acquisition challenges while providing valuable insights for both recruiters and job seekers.
