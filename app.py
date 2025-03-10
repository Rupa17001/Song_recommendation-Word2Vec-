import streamlit as st
import requests
import pandas as pd

st.title("🎶 Music Recommendation System")

# Input field for song ID
song_id = st.text_input("Enter a Song ID:")

if st.button("Get Recommendations"):
    if song_id:
        # Fetch recommendations from FastAPI
        response = requests.get(f"https://song-recommendation-word2vec.onrender.com/recommend/{song_id}")
        
        if response.status_code == 200:
            data = response.json()

            if "recommendations" in data:
                recommendations = data["recommendations"]

                # Convert recommendations to DataFrame
                df = pd.DataFrame(recommendations)

                # Display recommendations in a table
                st.subheader("📋 Recommended Songs")
                st.dataframe(df, use_container_width=True)
            else:
                st.error("No recommendations found!")
        else:
            st.error("Song ID not found!")
