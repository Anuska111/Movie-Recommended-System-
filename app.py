import streamlit as st
import pickle
import pandas as pd
import requests
import gzip


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# TMDB API
# =========================================================

API_KEY = "7e8ec4fdd2311743581c55ea1be32d7c"

BASE_URL = "https://api.themoviedb.org/3"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"


# =========================================================
# LOAD PICKLE FILES
# =========================================================

import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load movie dictionary
with open(os.path.join(BASE_DIR, "movie_dict.pkl"), "rb") as file:
    movie_dict = pickle.load(file)

movies = pd.DataFrame(movie_dict)

# Load similarity matrix
with gzip.open(os.path.join(BASE_DIR, "similarity.pkl.gz"), "rb") as file:
    similarity = pickle.load(file)


# =========================================================
# FETCH MOVIE DETAILS
# =========================================================

def fetch_movie_details(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print("TMDB Details Error:", e)

        return None


# =========================================================
# FETCH POSTER
# =========================================================

def fetch_poster(movie_id):

    movie_details = fetch_movie_details(movie_id)

    if movie_details is None:
        return None

    poster_path = movie_details.get("poster_path")

    if poster_path:

        return POSTER_BASE_URL + poster_path

    return None


# =========================================================
# FETCH TRAILER
# =========================================================

def fetch_trailer(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}/videos"

    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:

        print("TMDB Trailer Error:", e)

        return None

    videos = data.get("results", [])


    # -----------------------------------------
    # Official YouTube Trailer
    # -----------------------------------------

    for video in videos:

        if (
            video.get("site") == "YouTube"
            and video.get("type") == "Trailer"
            and video.get("official") is True
        ):

            return (
                f"https://www.youtube.com/watch?v="
                f"{video['key']}"
            )


    # -----------------------------------------
    # Any YouTube Trailer
    # -----------------------------------------

    for video in videos:

        if (
            video.get("site") == "YouTube"
            and video.get("type") == "Trailer"
        ):

            return (
                f"https://www.youtube.com/watch?v="
                f"{video['key']}"
            )


    # -----------------------------------------
    # Teaser if Trailer not available
    # -----------------------------------------

    for video in videos:

        if (
            video.get("site") == "YouTube"
            and video.get("type") == "Teaser"
        ):

            return (
                f"https://www.youtube.com/watch?v="
                f"{video['key']}"
            )


    return None


# =========================================================
# FETCH CAST AND CREW
# =========================================================

def fetch_cast_crew(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}/credits"

    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:

        print("TMDB Credits Error:", e)

        return [], []


    cast = data.get("cast", [])
    crew = data.get("crew", [])


    # -----------------------------------------
    # Top 5 Cast Members
    # -----------------------------------------

    cast_names = []

    for person in cast[:5]:

        if person.get("name"):

            cast_names.append(
                person["name"]
            )


    # -----------------------------------------
    # Director
    # -----------------------------------------

    director_names = []

    for person in crew:

        if person.get("job") == "Director":

            director_names.append(
                person["name"]
            )


    return cast_names, director_names


# =========================================================
# RECOMMEND MOVIES
# =========================================================

def recommend(movie):

    movie_index = movies[
        movies["title"] == movie
    ].index[0]


    # Similarity scores
    distance = similarity[movie_index]


    # Get top 5 similar movies
    movies_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]


    recommended_movies = []
    recommended_posters = []
    recommended_movie_ids = []


    for item in movies_list:

        movie_index = item[0]


        # Movie title
        movie_title = movies.iloc[
            movie_index
        ]["title"]


        # TMDB movie ID
        movie_id = int(
            movies.iloc[
                movie_index
            ]["movie_id"]
        )


        recommended_movies.append(
            movie_title
        )


        recommended_movie_ids.append(
            movie_id
        )


        # Poster
        poster = fetch_poster(
            movie_id
        )


        recommended_posters.append(
            poster
        )


    return (
        recommended_movies,
        recommended_posters,
        recommended_movie_ids
    )


# =========================================================
# STREAMLIT TITLE
# =========================================================

st.title("🎬 Movie Recommender System")

st.write(
    "Select a movie and get 5 similar movie recommendations."
)


# =========================================================
# MOVIE SELECTBOX
# =========================================================

selected_movie_name = st.selectbox(
    "Select a movie",
    movies["title"].values
)


# =========================================================
# RECOMMEND BUTTON
# =========================================================

if st.button("🎯 Recommend"):


    with st.spinner(
        "Finding recommendations..."
    ):

        names, posters, movie_ids = recommend(
            selected_movie_name
        )


    st.subheader(
        "🎬 Recommended Movies"
    )


    # =====================================================
    # CREATE 5 COLUMNS
    # =====================================================

    columns = st.columns(5)


    for index in range(5):

        with columns[index]:


            movie_name = names[index]

            poster = posters[index]

            movie_id = movie_ids[index]


            # =============================================
            # POSTER
            # =============================================

            if poster:

                st.image(
                    poster,
                    use_container_width=True
                )

            else:

                st.info(
                    "Poster not available"
                )


            # =============================================
            # MOVIE TITLE
            # =============================================

            st.markdown(
                f"### {movie_name}"
            )


            # =============================================
            # MOVIE DETAILS
            # =============================================

            movie_details = fetch_movie_details(
                movie_id
            )


            if movie_details:


                # -----------------------------------------
                # Rating
                # -----------------------------------------

                rating = movie_details.get(
                    "vote_average",
                    "N/A"
                )


                # -----------------------------------------
                # Release Date
                # -----------------------------------------

                release_date = movie_details.get(
                    "release_date",
                    "N/A"
                )


                # -----------------------------------------
                # Genres
                # -----------------------------------------

                genres = movie_details.get(
                    "genres",
                    []
                )


                genre_names = [
                    genre["name"]
                    for genre in genres
                ]


                # -----------------------------------------
                # Display Rating
                # -----------------------------------------

                if rating != "N/A":

                    st.write(
                        f"⭐ Rating: {rating:.1f}/10"
                    )

                else:

                    st.write(
                        "⭐ Rating: N/A"
                    )


                # -----------------------------------------
                # Release Date
                # -----------------------------------------

                st.write(
                    f"📅 Release: {release_date}"
                )


                # -----------------------------------------
                # Genres
                # -----------------------------------------

                if genre_names:

                    st.write(
                        "🎭 "
                        + ", ".join(
                            genre_names
                        )
                    )


            # =============================================
            # CAST AND CREW
            # =============================================

            cast, directors = fetch_cast_crew(
                movie_id
            )


            if cast:

                st.markdown(
                    "**🎭 Cast**"
                )

                st.write(
                    ", ".join(cast)
                )


            if directors:

                st.markdown(
                    "**🎬 Director**"
                )

                st.write(
                    ", ".join(directors)
                )


            # =============================================
            # MOVIE OVERVIEW
            # =============================================

            if movie_details:

                overview = movie_details.get(
                    "overview",
                    "Overview not available."
                )


                with st.expander(
                    "📖 Overview"
                ):

                    st.write(
                        overview
                    )
            # =============================================
            # TRAILER
            # =============================================

            trailer_url = fetch_trailer(movie_id)

            if trailer_url:

                video_key = trailer_url.split("v=")[1]

                st.markdown(
                    f"""
                    <iframe
                        width="100%"
                        height="180"
                        src="https://www.youtube.com/embed/{video_key}?autoplay=1&mute=1&controls=0&loop=1&playlist={video_key}"
                        title="Movie Trailer"
                        frameborder="0"
                        allow="autoplay; encrypted-media"
                        allowfullscreen>
                    </iframe>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.caption("🎞️ Trailer not available")
