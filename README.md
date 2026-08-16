# 🎬 Movie Recommender System

### An Intelligent Content-Based Movie Recommendation Web Application

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">

<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">

<img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white">

<img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white">

<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white">

<img src="https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=git&logoColor=white">

</p>

<p align="center">

<strong>🎥 Discover movies. 🤖 Get intelligent recommendations. 🍿 Find your next favourite.</strong>

</p>

---

# 🚀 Live Demo

<p align="center">

<a href="YOUR_STREAMLIT_APP_LINK_HERE">

<img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">

</a>

</p>

👉 **[Launch the Live Movie Recommender](YOUR_STREAMLIT_APP_LINK_HERE)**

> Replace `YOUR_STREAMLIT_APP_LINK_HERE` with your deployed Streamlit application URL.

---

# 📓 Jupyter Notebook

The complete machine learning workflow is available in the Jupyter Notebook.

### The notebook includes:

- Dataset loading
- Data exploration
- Data preprocessing
- Feature engineering
- Genre processing
- Keyword processing
- Cast processing
- Crew processing
- Movie tag creation
- Text vectorization
- Cosine similarity
- Recommendation logic
- Model/data serialization

👉 **[View Complete Jupyter Notebook](YOUR_GITHUB_NOTEBOOK_LINK_HERE)**

---

# 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objective](#-project-objective)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [How the Recommendation System Works](#-how-the-recommendation-system-works)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Content-Based Filtering](#-content-based-filtering)
- [Feature Engineering](#-feature-engineering)
- [CountVectorizer](#-countvectorizer)
- [Cosine Similarity](#-cosine-similarity)
- [Recommendation Logic](#-recommendation-logic)
- [TMDB API Integration](#-tmdb-api-integration)
- [Streamlit Application](#-streamlit-application)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [API Configuration](#-api-configuration)
- [Run Locally](#-run-locally)
- [Deployment](#-deployment)
- [Security](#-security)
- [Advantages](#-advantages)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Skills Demonstrated](#-skills-demonstrated)
- [Project Status](#-project-status)
- [Author](#-author)

---

# 🎬 Project Overview

The **Movie Recommender System** is an end-to-end machine learning application that recommends movies similar to a movie selected by the user.

The system uses a **Content-Based Filtering** approach.

Instead of relying on user ratings or collaborative filtering, the recommendation engine analyzes movie metadata such as:

- 🎭 Genres
- 🔑 Keywords
- 🎬 Cast
- 🎥 Crew

These attributes are combined to create a unified textual representation of each movie.

The textual representation is transformed into numerical vectors using **CountVectorizer**.

The similarity between movies is then calculated using **Cosine Similarity**.

When a user selects a movie, the system finds the movies with the highest similarity scores and returns the **Top 5 recommendations**.

The recommended movies are then enriched using the **TMDB API**, allowing the application to display:

- 🎞️ Movie posters
- ⭐ Ratings
- 📅 Release dates
- 🎭 Genres
- 🎬 Cast
- 👨‍🎬 Director
- 📝 Movie overview
- ▶️ Available trailers

The complete recommendation pipeline is integrated into an interactive **Streamlit web application**.

---

# 🎯 Project Objective

The primary objective is to build a practical recommendation system that combines:

```text
Movie Metadata
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Natural Language Processing
       ↓
CountVectorizer
       ↓
Cosine Similarity
       ↓
Top-5 Recommendations
       ↓
TMDB API
       ↓
Streamlit Web Application

# 🎯 Main Goals

The main goals of this project are:

### 1. 🎬 Build an Intelligent Movie Recommendation System
Develop a machine-learning-based system capable of recommending the **Top 5 movies** similar to a movie selected by the user.

### 2. 🧠 Implement Content-Based Filtering
Use movie metadata such as **genres, keywords, cast and crew** to determine the similarity between movies without requiring user-rating history.

### 3. 🔤 Apply NLP & Feature Engineering
Combine movie metadata into meaningful movie tags and transform the textual information into numerical representations using **CountVectorizer**.

### 4. 📐 Calculate Movie Similarity
Use **Cosine Similarity** to mathematically measure the similarity between movies and rank the most relevant recommendations.

### 5. 🌐 Develop a Complete Interactive Application
Integrate the machine learning recommendation engine with **TMDB API and Streamlit** to create an interactive web application where users can explore movie posters, ratings, genres, cast, crew, descriptions and available trailers.

