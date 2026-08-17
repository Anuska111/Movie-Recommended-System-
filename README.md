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
<p align="center">

<a href="https://movierecommendsystemnew.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Open%20Streamlit%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

<a href="https://github.com/Anuska111/Movie-Recommended-System-">
  <img src="https://img.shields.io/badge/💻%20Source%20Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
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

The recommendation engine follows a complete Machine Learning pipeline, starting from movie metadata preprocessing and ending with personalized movie recommendations.

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
```

---

# 🖥️ Streamlit Application

The trained recommendation model is integrated into an interactive **Streamlit web application**, allowing users to select a movie and instantly explore similar movies with detailed information.

## 🔄 User Flow

```mermaid
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
```

---

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

---

# 📊 End-to-End Workflow

The complete workflow combines the Machine Learning recommendation engine, optimized model storage, Streamlit interface, and TMDB API.

```mermaid
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
```

---

# ⚠️ Current Limitations

| Limitation | Description |
|---|---|
| 👤 **No User Personalization** | Recommendations are based on movie content and do not currently learn individual user preferences. |
| ⭐ **No User Rating History** | The system does not use personal ratings, likes, dislikes, or watch history. |
| 🤝 **Content-Based Only** | The current recommendation engine relies primarily on content similarity rather than collaborative filtering. |
| 🎬 **Metadata Dependency** | Recommendation quality depends on the availability and quality of genres, keywords, cast, and crew information. |
| 🌐 **TMDB API Dependency** | Posters, ratings, cast, trailers, and other movie details depend on TMDB API availability. |
| 📊 **Limited Ranking Signals** | Ranking is primarily based on content similarity and does not currently combine popularity, ratings, or user behavior. |
| 🆕 **Cold-Start for Preferences** | Since user history is not collected, the system cannot initially adapt recommendations to a specific user's taste. |
| 🔄 **Static Recommendation Model** | Similarity data is precomputed and does not continuously learn from new user interactions. |

---

# 🔮 Future Improvements

| Future Enhancement | Description |
|---|---|
| 🤝 **Hybrid Recommendation** | Combine Content-Based Filtering with Collaborative Filtering for better recommendations. |
| 👤 **Personalized Profiles** | Learn individual preferences from ratings, likes, dislikes, and watch history. |
| ⭐ **User Rating System** | Allow users to rate movies and use those ratings to improve recommendations. |
| ❤️ **Favorites & Watchlist** | Allow users to save movies for later viewing. |
| 🔍 **Advanced Search & Filters** | Filter movies by genre, rating, release year, language, popularity, and runtime. |
| 🤖 **LLM Integration** | Add natural-language movie recommendations through a conversational AI assistant. |
| 🧠 **Hybrid AI Ranking** | Combine similarity, popularity, ratings, and user preferences into a unified ranking system. |
| 📊 **Recommendation Analytics** | Add analytics for popular genres, recommendation frequency, and user preferences. |
| 🌎 **Multi-Language Support** | Extend movie discovery across multiple languages and regions. |
| 🔄 **Dynamic Learning** | Continuously update recommendations based on new user interactions. |

---

# 🚀 Future AI Architecture

A future version can evolve from a traditional content-based recommender into a more personalized **AI-powered recommendation platform**.

```mermaid
flowchart TD
    A["👤 User"] --> B["💬 Natural Language Query"]

    B --> C["🤖 LLM"]
    C --> D["🎯 Extract User Preferences"]

    D --> E["🧠 Recommendation Engine"]

    E --> F["🎭 Content Similarity"]
    E --> G["⭐ User Ratings"]
    E --> H["📊 Popularity"]
    E --> I["👤 Watch History"]

    F --> J["🏆 Hybrid Ranking"]
    G --> J
    H --> J
    I --> J

    J --> K["🎬 Personalized Recommendations"]
    K --> L["🌐 TMDB API"]
    L --> M["🖼️ Posters + Details + Trailers"]
```

---

# 🎯 Key Takeaways

| Area | Implementation |
|---|---|
| 🧠 **Recommendation** | Content-Based Filtering |
| 📐 **Similarity** | Cosine Similarity |
| 🔤 **Text Processing** | NLP / Vectorization |
| 🎬 **Movie Information** | TMDB API |
| 🌐 **Application** | Streamlit |
| 🗜️ **Optimization** | Gzip Compression |
| ☁️ **Deployment** | Streamlit Cloud |

# 👩‍💻 Author

<p align="center">

### **Anuska Biswas**

🎓 **Indian Institute of Technology (BHU), Varanasi**  
⚙️ **Mechanical Engineering Department**

</p>

---

<p align="center">
  <b>🎬 Built with Python • Machine Learning • Streamlit • TMDB API</b>
</p>
