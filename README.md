# 🎬 Movie Recommendation System

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Content%20Based-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn">
</p>

<p align="center">
  <b>An end-to-end Machine Learning Movie Recommendation System</b>
  <br>
  <i>Discover movies similar to your favorites using Content-Based Filtering.</i>
</p>

<p align="center">
  <a href="YOUR_STREAMLIT_APP_LINK">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge">
  </a>
  <a href="https://github.com/Anuska111/Movie-Recommended-System-">
    <img src="https://img.shields.io/badge/💻%20Source%20Code-GitHub-181717?style=for-the-badge&logo=github">
  </a>
</p>

---

## 📌 Overview

The **Movie Recommendation System** is an end-to-end Machine Learning application that recommends movies based on the similarity of their content and metadata.

The system follows a **Content-Based Filtering** approach and uses important movie attributes such as:

- 🎭 Genres
- 🔑 Keywords
- 👥 Cast
- 🎬 Crew / Director

These features are processed and transformed into numerical representations. **Cosine Similarity** is then used to identify the most similar movies and generate the **Top 5 recommendations**.

The application is integrated with the **TMDB API** to provide rich movie information such as posters, ratings, genres, cast, director, release date, overview, and trailers.

<p align="center">

<a href="https://movierecommendsystemnew.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Open%20Streamlit%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

<a href="https://github.com/Anuska111/Movie-Recommended-System-">
  <img src="https://img.shields.io/badge/💻%20Source%20Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

</p>
---

# 🚀 Project Highlights

| Feature | Description |
|---|---|
| 🎯 Recommendation | Top 5 similar movies |
| 🧠 ML Approach | Content-Based Filtering |
| 📐 Similarity | Cosine Similarity |
| 🔤 NLP | Text feature processing |
| 🎬 Movie Data | TMDB API |
| 🖼️ Posters | Dynamic TMDB posters |
| ⭐ Ratings | TMDB movie ratings |
| 👥 Cast | Movie cast information |
| 🎥 Director | Director information |
| ▶️ Trailer | YouTube trailer integration |
| 🌐 Interface | Streamlit Web App |
| 🗜️ Optimization | Compressed similarity data |
| ☁️ Deployment | Streamlit Cloud |

---

# 🧠 How the Recommendation System Works

The recommendation engine follows a complete Machine Learning pipeline:

```mermaid
flowchart TD

    A["🎬 Movie Dataset"] --> B["🧹 Data Preprocessing"]

    B --> C["⚙️ Feature Engineering"]

    C --> C1["🎭 Genres"]
    C --> C2["🔑 Keywords"]
    C --> C3["👥 Cast"]
    C --> C4["🎬 Crew / Director"]

    C1 --> D["🔗 Feature Combination"]
    C2 --> D
    C3 --> D
    C4 --> D

    D --> E["🔤 Text Vectorization"]

    E --> F["📐 Cosine Similarity"]

    F --> G["📊 Similarity Ranking"]

    G --> H["🏆 Top 5 Recommendations"]

    H --> I["🌐 Streamlit Application"]

    I --> J["🎬 TMDB API"]

    J --> K["🖼️ Posters"]
    J --> L["⭐ Ratings"]
    J --> M["👥 Cast & Director"]
    J --> N["📖 Overview"]
    J --> O["▶️ Trailer"]

🖥️ Streamlit Application
The Machine Learning model is converted into an interactive web application using Streamlit.

User Flow
flowchart LR

    A["👤 User"] --> B["🎬 Select Movie"]

    B --> C["🔘 Recommend"]

    C --> D["🧠 Recommendation Engine"]

    D --> E["🏆 Top 5 Movies"]

    E --> F["🌐 TMDB API"]

    F --> G["🖼️ Movie Cards"]

    G --> H["⭐ Rating"]

    G --> I["🎭 Genre"]

    G --> J["👥 Cast"]

    G --> K["🎬 Director"]

    G --> L["▶️ Trailer"]

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| 🐍 **Programming Language** | Python |
| 🐼 **Data Processing** | Pandas, NumPy |
| 🤖 **Machine Learning** | Scikit-learn |
| 🧠 **NLP / Text Processing** | Text Vectorization |
| 📐 **Recommendation Algorithm** | Cosine Similarity |
| 🎬 **Movie Data & API** | TMDB API |
| 🌐 **Web Framework** | Streamlit |
| 💾 **Model Serialization** | Pickle |
| 🗜️ **Data Compression** | Gzip |
| 🔧 **Version Control** | Git |
| 🐙 **Repository** | GitHub |
| ☁️ **Deployment** | Streamlit Cloud |

**📊 End-to-End Workflow**
flowchart TD

    A["📂 Dataset"] --> B["🧹 Preprocessing"]
    B --> C["⚙️ Feature Engineering"]
    C --> D["🔤 Text Vectorization"]
    D --> E["📐 Cosine Similarity"]
    E --> F["💾 Save Similarity Data"]
    F --> G["🗜️ Compress similarity.gz"]

    G --> H["🌐 Streamlit App"]

    H --> I["👤 User Selects Movie"]
    I --> J["🏆 Generate Recommendations"]

    J --> K["🎬 TMDB API"]

    K --> L["🖼️ Posters"]
    K --> M["⭐ Ratings"]
    K --> N["🎭 Genres"]
    K --> O["👥 Cast"]
    K --> P["🎬 Director"]
    K --> Q["▶️ Trailer"]

# ⚠️ Current Limitations

| Limitation | Description |
|---|---|
| 👤 **No User Personalization** | Recommendations are based on movie content and do not currently learn individual user preferences. |
| ⭐ **No User Rating History** | The system does not use personal ratings, likes, dislikes, or watch history. |
| 🤝 **Content-Based Only** | The current recommendation engine relies primarily on content similarity rather than collaborative filtering. |
| 🎬 **Metadata Dependency** | Recommendation quality depends on the availability and quality of genres, keywords, cast, and crew information. |
| 🌐 **TMDB API Dependency** | Posters, ratings, cast, trailers, and other movie details depend on TMDB API availability. |
| 📊 **Limited Ranking Signals** | The current ranking is primarily based on content similarity and does not combine popularity, ratings, or user behavior. |
| 🆕 **Cold-Start for Preferences** | Since user history is not collected, the system cannot initially adapt recommendations to a specific user's taste. |
| 🔄 **Static Recommendation Model** | The similarity data is precomputed and does not continuously learn from new user interactions. |

👩‍💻 Author
Anuska Biswas
🎓 Mechanical Engineering | IIT (BHU) Varanasi
