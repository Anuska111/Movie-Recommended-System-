# 🎬 Movie Recommended System

<p align="center">
  <b>AI/ML Powered Content-Based Movie Recommendation System</b>
</p>

<p align="center">
  <i>Discover movies you'll love using Machine Learning, Cosine Similarity, Streamlit & TMDB API.</i>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![TMDB](https://img.shields.io/badge/API-TMDB-blue)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

</p>

---

## 🌐 Live Application

🚀 **Try the Movie Recommendation System:**

👉 **[Launch Streamlit App](YOUR_STREAMLIT_APP_LINK)**

---

# 📌 Overview

The **Movie Recommended System** is an interactive Machine Learning application that recommends movies based on the content and characteristics of a movie selected by the user.

Instead of relying only on popularity or ratings, the system analyzes movie metadata such as:

- 🎭 Genres
- 🔑 Keywords
- 👥 Cast
- 🎬 Crew / Director

These features are transformed into numerical representations and compared using **Cosine Similarity** to identify movies with similar characteristics.

The final recommendation experience is enhanced using the **TMDB API**, which dynamically provides movie posters, ratings, genres, cast, release dates, overviews, and trailers.

---

# 🎯 Project Objectives

The major objectives of this project are:

- Build an end-to-end Machine Learning recommendation pipeline.
- Implement a Content-Based Filtering approach.
- Perform feature engineering on movie metadata.
- Convert textual movie information into numerical representations.
- Calculate movie-to-movie similarity using Cosine Similarity.
- Recommend the most relevant movies for a selected title.
- Integrate a real-time external API for rich movie information.
- Deploy the complete ML application using Streamlit.
- Handle large serialized similarity data efficiently using compression.

---

# ✨ Key Features

### 🎯 Intelligent Movie Recommendations
Select a movie and receive the **Top 5 similar movies** based on content similarity.

### 🎭 Content-Based Filtering
Recommendations are generated from movie metadata rather than relying on other users' ratings.

### 🧠 Machine Learning Pipeline
The system uses feature engineering, text vectorization and Cosine Similarity to generate recommendations.

### 🎬 TMDB API Integration
Real-time movie information is fetched from TMDB.

### 🖼️ Dynamic Movie Posters
Recommended movies are displayed with their posters.

### ⭐ Movie Ratings
Displays movie rating information fetched through TMDB.

### 📅 Release Information
Shows release dates and other movie metadata.

### 👥 Cast & Director
Provides important information about the cast and director.

### 📖 Movie Overview
Displays a detailed description of the recommended movie.

### ▶️ Trailer Integration
Fetches available YouTube trailers for recommended movies.

### 🌐 Interactive Streamlit UI
Provides a simple and user-friendly interface for exploring recommendations.

### 💾 Optimized Model Storage
The similarity data is stored in compressed format to reduce file size and make deployment easier.

---

# 🧠 Recommendation System Architecture

```text
                    ┌─────────────────────┐
                    │    Movie Dataset    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Data Preprocessing │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Feature Engineering│
                    │                     │
                    │ Genres              │
                    │ Keywords            │
                    │ Cast                │
                    │ Crew / Director     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Combination │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Text Vectorization  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Cosine Similarity   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Top Similar Movies  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Streamlit Interface │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     TMDB API        │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌──────────────────────────────────┐
              │ Posters • Ratings • Cast • Genre │
              │ Director • Overview • Trailer    │
              └──────────────────────────────────┘

