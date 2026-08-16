# 🎬 Movie Recommender System

### An Intelligent Content-Based Movie Recommendation Web Application

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">

<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">

<img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white">

<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white">

<img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white">

</p>

---

## 🌐 Live Demo

🎬 **Try the Movie Recommender System**

👉 [Launch Movie Recommender](YOUR_STREAMLIT_APP_LINK_HERE)

> Replace `YOUR_STREAMLIT_APP_LINK_HERE` with your deployed Streamlit application URL.

---

## 📓 Jupyter Notebook

The complete machine learning workflow is implemented in the Jupyter Notebook.

The notebook contains the complete recommendation-system pipeline, including:

- Dataset loading
- Data preprocessing
- Feature selection
- Feature engineering
- Genres processing
- Keywords processing
- Cast processing
- Crew processing
- Movie tag creation
- Text vectorization
- Cosine similarity
- Recommendation logic
- Model/data serialization

👉 [View Jupyter Notebook](YOUR_JUPYTER_NOTEBOOK_LINK_HERE)

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
- [Movie Details, Cast, Crew & Trailers](#-movie-details-cast-crew--trailers)
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

# 📌 Project Overview

The **Movie Recommender System** is an end-to-end machine learning web application that recommends movies based on the similarity of their content and metadata.

The project follows a **Content-Based Filtering** approach.

Instead of relying on user ratings, watch history, or collaborative filtering, the system analyzes movie-related information such as:

- 🎭 Genres
- 🔑 Keywords
- 🎬 Cast
- 🎥 Crew

These attributes are processed and combined into a unified movie representation known as **movie tags**.

The generated tags are converted into numerical vectors using **CountVectorizer** from Scikit-learn.

The similarity between movies is then calculated using **Cosine Similarity**.

When a user selects a movie, the recommendation engine searches the similarity matrix, ranks movies according to their similarity score, and returns the **Top 5 most similar movies**.

The application is connected with the **TMDB API** to retrieve additional movie information such as posters, ratings, genres, cast, crew, descriptions and available trailer information.

Finally, the complete recommendation system is integrated into a **Streamlit web application**, providing an interactive interface for users.

---

# 🎯 Project Objective

The primary objective of this project is to build a practical and interactive recommendation system that converts movie metadata into meaningful similarity relationships.

The project aims to:

- Build a content-based movie recommendation engine.
- Combine multiple movie metadata features.
- Transform textual movie information into numerical vectors.
- Calculate similarity between movie representations.
- Rank movies based on similarity scores.
- Generate Top 5 movie recommendations.
- Integrate TMDB API for dynamic movie information.
- Display recommendations through an interactive Streamlit interface.
- Demonstrate an end-to-end Data Science and Machine Learning workflow.

### Core Concept

Movie Metadata

↓  

Feature Engineering

↓

Movie Tags

↓

CountVectorizer

↓

Numerical Feature Vectors

↓

Cosine Similarity

↓

Similarity Matrix

↓

Top-5 Recommendations

↓

TMDB API

↓

Streamlit Web Application

---

# ✨ Key Features

### 🎯 Content-Based Recommendation

Recommends movies based on similarity between movie metadata.

### 🎭 Multi-Feature Movie Representation

The recommendation engine uses multiple features including:

- Genres
- Keywords
- Cast
- Crew

### 🔤 Text Vectorization

Uses Scikit-learn's `CountVectorizer` to transform movie tags into numerical vectors.

### 📐 Cosine Similarity

Calculates similarity between movie vectors.

### 🏆 Top-5 Recommendations

Returns the five most similar movies for the selected movie.

### 🌐 TMDB API Integration

Retrieves dynamic information about movies from TMDB.

### 🖼️ Movie Posters

Displays posters for recommended movies.

### ⭐ Movie Information

Can retrieve movie information such as:

- Ratings
- Genres
- Overview
- Cast
- Crew

### 🎥 Trailer Support

Available trailer information can be integrated into the Streamlit interface.

### 🖥️ Interactive Web Interface

Users can select a movie and generate recommendations through Streamlit.

---

# 🏗️ System Architecture

The complete system follows this architecture:

User

↓

Streamlit Movie Selection

↓

Selected Movie

↓

Recommendation Function

↓

Movie Index Lookup

↓

Similarity Vector

↓

Similarity Ranking

↓

Top-5 Movies

↓

TMDB API

↓

Movie Posters + Details + Cast + Crew + Trailer Information

↓

Streamlit Results

---

# 🔄 How the Recommendation System Works

The recommendation process can be divided into several stages.

### Step 1 — Movie Dataset

The system starts with movie metadata containing information such as genres, keywords, cast and crew.

### Step 2 — Data Preprocessing

The relevant movie attributes are cleaned and transformed into a suitable format.

### Step 3 — Feature Engineering

Important movie attributes are combined to create a unified textual representation.

### Step 4 — Movie Tags

The selected features are combined into a `tags` representation.

Example:

Genres + Keywords + Cast + Crew

↓

Movie Tags

### Step 5 — Vectorization

CountVectorizer converts the movie tags into numerical vectors.

### Step 6 — Similarity Calculation

Cosine Similarity calculates the similarity between movie vectors.

### Step 7 — Recommendation

For a selected movie, the system retrieves its similarity scores and ranks other movies.

### Step 8 — Top 5 Selection

The five highest-ranked similar movies are selected.

### Step 9 — TMDB API

TMDB is used to retrieve additional movie information.

### Step 10 — Streamlit Display

The recommendations are displayed through the web application.

---

# 🤖 Machine Learning Pipeline

The complete machine learning pipeline can be represented as:

Raw Movie Dataset

↓

Data Loading

↓

Data Cleaning

↓

Feature Selection

↓

Feature Engineering

↓

Movie Tags

↓

Text Vectorization

↓

CountVectorizer

↓

Feature Vectors

↓

Cosine Similarity

↓

Similarity Matrix

↓

Recommendation Function

↓

Top-5 Recommendations

---

# 🎯 Content-Based Filtering

This project implements a **Content-Based Filtering** recommendation technique.

Content-based recommendation systems recommend items that are similar to an item selected by the user.

In this project, similarity is based on movie metadata rather than user behaviour.

### Example

Suppose a user selects a movie containing:

- Action
- Adventure
- Science Fiction
- Space
- Specific actors
- Related keywords

The system compares its feature representation against other movies and recommends movies with similar representations.

### Concept

Selected Movie

↓

Movie Features

↓

Feature Representation

↓

Compare With Other Movies

↓

Calculate Similarity

↓

Rank Similar Movies

↓

Recommend Top Movies

---

# 🛠️ Feature Engineering

Feature engineering is one of the most important stages of the recommendation system.

The project combines multiple movie attributes to generate a unified representation.

### Movie Features

| Feature | Role |
|---|---|
| Genres | Represents movie categories |
| Keywords | Represents themes and concepts |
| Cast | Represents actors associated with the movie |
| Crew | Represents relevant crew information |

These features are combined to create the movie's textual representation.

### Feature Transformation

Genres

+

Keywords

+

Cast

+

Crew

↓

Movie Tags

↓

Text Representation

↓

Numerical Vector

---

# 🔤 CountVectorizer

The project uses **CountVectorizer** from Scikit-learn to convert movie tags into numerical representations.

Machine learning algorithms cannot directly calculate vector similarity from raw textual data.

Therefore, movie tags are transformed into feature vectors.

### Process

Movie Tags

↓

Tokenization

↓

Vocabulary Creation

↓

Word Frequency Representation

↓

Numerical Feature Vectors

### Implementation Concept

`CountVectorizer` creates a vocabulary from the movie tags and represents each movie according to the occurrence of vocabulary terms.

This allows movies to be compared mathematically.

---

# 📐 Cosine Similarity

The recommendation system uses **Cosine Similarity** to calculate the similarity between movie vectors.

Cosine Similarity measures the cosine of the angle between two vectors.

### Formula

Similarity(A,B) = (A · B) / (||A|| × ||B||)

Where:

- `A` = Vector representation of Movie A
- `B` = Vector representation of Movie B
- `A · B` = Dot product
- `||A||` = Magnitude of vector A
- `||B||` = Magnitude of vector B

### Implementation

The similarity matrix is generated using Scikit-learn's pairwise similarity functionality.

The resulting matrix stores similarity relationships between movies.

### Why Cosine Similarity?

Cosine Similarity is useful for text-based representations because it focuses on the orientation of vectors rather than their absolute magnitude.

This makes it suitable for comparing movie tag representations.

---

# 🎯 Recommendation Logic

The recommendation engine identifies the selected movie and retrieves its corresponding similarity scores.

The basic logic is:

1. Find the selected movie.
2. Retrieve its index.
3. Access its similarity vector.
4. Pair movie indices with similarity scores.
5. Sort the movies by similarity.
6. Exclude the selected movie itself.
7. Select the Top 5 movies.
8. Retrieve additional information through TMDB.
9. Display the recommendations.

### Recommendation Flow

Selected Movie

↓

Movie Index

↓

Similarity Scores

↓

Similarity Ranking

↓

Top Similar Movies

↓

Top 5 Recommendations

---

# 🌐 TMDB API Integration

The project integrates the **TMDB API** to enrich the recommendation experience.

The machine learning model determines which movies should be recommended, while TMDB provides additional information about those movies.

### TMDB Integration Flow

Recommendation Engine

↓

Recommended Movie

↓

TMDB API Request

↓

JSON Response

↓

Movie Metadata

↓

Streamlit UI

### Information Retrieved

Depending on the API response and implementation, the application can use information such as:

- Movie poster
- Movie title
- Rating
- Genres
- Overview
- Cast
- Crew
- Trailer/video information

This makes the application more visually appealing and informative than displaying movie titles alone.

---

# 🎥 Movie Details, Cast, Crew & Trailers

The application can use TMDB endpoints to retrieve additional movie information.

### Movie Details

Movie details can include:

- Title
- Overview
- Rating
- Genres
- Release information

### Cast

The cast information can be used to display the actors associated with a movie.

### Crew

Crew information can be used to identify important contributors such as directors and other crew members.

### Videos / Trailers

TMDB's video information can be used to identify available movie trailers.

The application can then integrate available trailer information into the Streamlit interface.

### User Experience

Movie Recommendation

↓

Movie Poster

↓

Movie Details

↓

Cast & Crew

↓

Available Trailer

This creates a more complete movie-discovery experience.

---

# 🖥️ Streamlit Application

The machine learning model is deployed through a Streamlit web interface.

The application allows the user to:

1. Open the application.
2. Select a movie.
3. Click the recommendation button.
4. Generate Top-5 recommendations.
5. View movie posters.
6. Retrieve additional movie information through TMDB.
7. Explore available movie information and trailers.

### Application Flow

User

↓

Select Movie

↓

Click Recommend

↓

Recommendation Engine

↓

Top 5 Movies

↓

TMDB API

↓

Posters / Details / Cast / Crew / Trailer

↓

Interactive Streamlit Interface

---

# 📁 Project Structure

```text
Movie-Recommended-System-
│
├── app.py
│
├── Movie_Recommender_System.ipynb
│
├── movie_dict.pkl
│
├── similarity.pkl
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
