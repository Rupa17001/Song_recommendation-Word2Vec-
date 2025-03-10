from fastapi import FastAPI
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
import uvicorn

app = FastAPI()

# Load the model and dataset
model = Word2Vec.load("word2vec_model.bin")
songs_df = pd.read_csv(r"C:\Users\Rupa Bisht\Desktop\Hands-on LLM\songs.csv")  # Save your songs_df to a CSV first

@app.get("/")
def home():
    return {"message": "Music Recommendation API"}

@app.get("/recommend/{song_id}")
def recommend(song_id: int):
    try:
        similar_songs = np.array(
            model.wv.most_similar(positive=[str(song_id)], topn=5)
        )[:, 0]
        recommendations = songs_df.iloc[similar_songs].to_dict(orient="records")
        return {"recommendations": recommendations}
    except KeyError:
        return {"error": "Song ID not found in the model"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
