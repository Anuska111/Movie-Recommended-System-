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
# 📌 Project Overview

The **Movie Recommender System** is an end-to-end machine learning web application that recommends movies similar to a movie selected by the user.

The system uses a **Content-Based Filtering** approach and analyzes movie metadata such as:

- 🎭 Genres
- 🔑 Keywords
- 🎬 Cast
- 🎥 Crew

These features are combined into a unified movie representation and transformed into numerical vectors using **CountVectorizer**. **Cosine Similarity** is then used to calculate the similarity between movies and identify the **Top 5 most similar movies**.

The recommendation engine is integrated with the **TMDB API** to retrieve additional movie information such as posters, ratings, genres, cast, crew, movie descriptions and available trailers.

The complete system is deployed through an interactive **Streamlit application**, providing users with a simple and engaging interface for discovering movies.

### 🔄 Overall Workflow

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Genres + Keywords + Cast + Crew
      ↓
Movie Tags
      ↓
CountVectorizer
      ↓
Feature Vectors
      ↓
Cosine Similarity
      ↓
Top 5 Recommendations
      ↓
TMDB API
      ↓
Movie Details + Posters + Trailers
      ↓
Streamlit Application


### 2. Project Objective

```markdown
# 🎯 Project Objective

The objective of this project is to develop a **smart, interactive and user-friendly movie discovery platform** that can identify movies similar to a user's selected movie.

The project focuses on transforming movie metadata into meaningful machine-learning features and using similarity-based analysis to generate relevant recommendations.

### Core Objectives

- 🎬 Develop a **Content-Based Movie Recommendation Engine**.
- 🧠 Analyze multiple movie attributes including genres, keywords, cast and crew.
- 🔤 Apply **NLP-based text vectorization** using CountVectorizer.
- 📐 Calculate movie similarity using Cosine Similarity.
- 🎯 Generate the **Top 5 most similar movie recommendations**.
- 🌐 Integrate the **TMDB API** for dynamic movie information.
- 🖥️ Build an interactive **Streamlit web application**.
- 🔄 Demonstrate an end-to-end workflow from data preprocessing to application deployment.

### End Goal

```text
Raw Movie Data
      ↓
Feature Engineering
      ↓
NLP / Vectorization
      ↓
Similarity Analysis
      ↓
Recommendation Engine
      ↓
TMDB API
      ↓
Interactive Streamlit Application


### 3. Key Features

```markdown
# ✨ Key Features

The application provides the following major features:

### 🎯 Content-Based Recommendations
Recommends movies based on the similarity of their content and metadata.

### 🎭 Multi-Feature Movie Analysis
Uses multiple movie attributes:

- Genres
- Keywords
- Cast
- Crew

### 🧠 NLP-Based Recommendation Engine
Uses textual movie information to create meaningful feature representations.

### 🔤 CountVectorizer
Converts movie tags into numerical feature vectors.

### 📐 Cosine Similarity
Calculates similarity between movie vectors and ranks relevant movies.

### 🎬 Top-5 Recommendations
Returns the five movies with the highest similarity scores.

### 🌐 TMDB API Integration
Fetches dynamic movie information from TMDB.

### 🖼️ Dynamic Movie Posters
Displays posters for recommended movies.

### ⭐ Movie Information
Provides additional information such as ratings, genres, cast, crew and descriptions.

### ▶️ Trailer Integration
Displays available movie trailers when trailer information is available.

### 🖥️ Streamlit Interface
Provides an interactive web-based interface for users.

### 📓 Jupyter Notebook
Contains the complete machine learning and recommendation-system development workflow.

# 🏗️ System Architecture

The system follows a complete end-to-end machine learning architecture.

```text
                         ┌──────────────────────┐
                         │    Movie Dataset     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Data Preprocessing   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Feature Engineering  │
                         │                      │
                         │ • Genres             │
                         │ • Keywords           │
                         │ • Cast               │
                         │ • Crew               │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Movie Tags        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   CountVectorizer    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Feature Vectors    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Cosine Similarity   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Recommendation       │
                         │ Engine               │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      TMDB API        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Streamlit App     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                                  USER

### 5. How the Recommendation System Works

```markdown
# 🔄 How the Recommendation System Works

The recommendation process follows a sequence of data-processing and similarity-analysis steps.

### Step 1 — User Selects a Movie

The user selects a movie from the Streamlit movie selection interface.

### Step 2 — Find Movie Index

The system identifies the index of the selected movie in the movie dataset.

### Step 3 — Retrieve Similarity Scores

The corresponding row from the precomputed similarity matrix is retrieved.

### Step 4 — Rank Movies

Movies are sorted according to their similarity scores in descending order.

### Step 5 — Select Top 5

The selected movie itself is excluded and the next five most similar movies are returned.

### Step 6 — Fetch Movie Information

The TMDB API is used to retrieve additional information for the recommended movies.

### Step 7 — Display Results

The recommendations are displayed through the Streamlit interface.

```text
User Selects Movie
        ↓
Find Movie Index
        ↓
Retrieve Similarity Scores
        ↓
Sort Similarity Scores
        ↓
Remove Selected Movie
        ↓
Select Top 5 Movies
        ↓
Fetch TMDB Information
        ↓
Display Recommendations


### 6. Machine Learning Pipeline

```markdown
# 🤖 Machine Learning Pipeline

The machine learning workflow consists of multiple stages that transform raw movie metadata into a recommendation system.

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Cleaning
     ↓
Feature Selection
     ↓
Feature Engineering
     ↓
Movie Tag Creation
     ↓
Text Vectorization
     ↓
Cosine Similarity
     ↓
Similarity Matrix
     ↓
Recommendation Function
     ↓
Top-5 Recommendations

Pipeline Components
| Stage                  | Description                         |
| ---------------------- | ----------------------------------- |
| Data Loading           | Load movie metadata                 |
| Data Preprocessing     | Clean and prepare relevant columns  |
| Feature Selection      | Select useful movie attributes      |
| Feature Engineering    | Combine relevant metadata           |
| Tag Generation         | Create unified movie tags           |
| Vectorization          | Convert text into numerical vectors |
| Similarity Calculation | Calculate movie-to-movie similarity |
| Ranking                | Rank movies based on similarity     |
| Recommendation         | Return Top 5 movies                 |


### 7. Content-Based Filtering

```markdown
# 🎯 Content-Based Filtering

This project implements a **Content-Based Filtering** recommendation approach.

Instead of relying on user ratings, purchase history or other users' preferences, the system recommends movies based on the characteristics of the selected movie.

### Features Used

```text
Genres
   +
Keywords
   +
Cast
   +
Crew
   ↓
Movie Representation

If two movies have similar metadata, they are likely to receive a higher similarity score.
Example
Selected Movie
├── Action
├── Adventure
├── Sci-Fi
├── Space
└── Similar Cast

        ↓

Recommended Movie
├── Action
├── Adventure
├── Sci-Fi
├── Space
└── Similar Cast


### 8. Feature Engineering

```markdown
# 🛠️ Feature Engineering

Feature engineering is an important part of the recommendation system because the quality of the movie representation directly affects the quality of recommendations.

The project combines multiple movie attributes into a unified textual representation.

### Features Used

| Feature | Role |
|---|---|
| 🎭 Genres | Represents movie categories |
| 🔑 Keywords | Represents themes and concepts |
| 🎬 Cast | Represents actors associated with the movie |
| 🎥 Crew | Represents directors and other important crew information |

### Feature Combination

```text
Genres
   +
Keywords
   +
Cast
   +
Crew
   ↓
Combined Movie Tags

The resulting movie tags are then passed to the text-vectorization stage.

This allows the recommendation engine to compare movies using multiple dimensions instead of depending on a single attribute.


### 9. CountVectorizer

```markdown
# 🔤 CountVectorizer

The project uses **CountVectorizer** from Scikit-learn to convert textual movie tags into numerical feature vectors.

Machine learning algorithms cannot directly perform mathematical similarity calculations on raw text. Therefore, movie tags need to be transformed into numerical representations.

### Process

```text
Movie Tags
     ↓
Tokenization

     ↓
Vocabulary Creation
     ↓
Word Frequency Representation
     ↓
Numerical Feature Vectors

Implementation
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
vectors = cv.fit_transform(movies['tags'])


### 10. Cosine Similarity

```markdown
# 📐 Cosine Similarity

**Cosine Similarity** is used to calculate how similar two movie feature vectors are.

The method measures the cosine of the angle between two vectors.

### Formula

```text
              A · B
Similarity = ─────────
             ||A|| ||B||

Where:

A = Feature vector of Movie A
B = Feature vector of Movie B
A · B = Dot product
||A|| and ||B|| = Magnitudes of the vectors

Implementation
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

The resulting similarity matrix stores the similarity relationship between movies.
A higher similarity score indicates that two movies have more similar feature representations.


### 11. Recommendation Logic

```markdown
# 🎯 Recommendation Logic

The recommendation function uses the precomputed similarity matrix to identify movies that are most similar to the selected movie.

### Core Process

```python
movie_index = movies[movies['title'] == movie].index[0]

distance = similarity[movie_index]

movies_list = sorted(
    list(enumerate(distance)),
    reverse=True,
    key=lambda x: x[1]
)[1:6]

Logic Breakdown
Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Vector
      ↓
Pair Movie Index + Similarity Score
      ↓
Sort in Descending Order
      ↓
Exclude Selected Movie
      ↓
Select Top 5
      ↓
Return Recommendations

The recommendation engine therefore converts similarity scores into a ranked list of movies that are most closely related to the user's selection.


### 12. TMDB API Integration

```markdown
# 🌐 TMDB API Integration

The **TMDB API** is integrated into the application to enrich the machine learning recommendations with dynamic movie information.

The recommendation model determines **which movies are similar**, while TMDB provides additional information about those movies.

### Integration Flow

```text
Recommendation Engine
        ↓
Recommended Movie
        ↓
TMDB API Request
        ↓
JSON Response
        ↓
Movie Information
        ↓
Streamlit UI


### 13. Streamlit Application

```markdown
# 🖥️ Streamlit Application

The machine learning recommendation engine is integrated into an interactive **Streamlit web application**.

The application provides a simple interface where users can select a movie and generate recommendations without directly interacting with the underlying Python code.

### User Flow

```text
                 🎬 Movie Recommender
                         │
                         ▼
                 Select a Movie
                         │
                         ▼
                  Click Recommend
                         │
                         ▼
              Recommendation Engine
                         │
                         ▼
                  Top 5 Movies
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Posters         Details       Trailers
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                      User


