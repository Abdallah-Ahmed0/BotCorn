import pandas as pd
import numpy as np
from dotenv import load_dotenv
import gradio as gr

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma

load_dotenv()

movies = pd.read_csv("data/movies_with_posters.csv")
movies["large_poster"] = movies["poster_url"] + "&fife=w800"

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


with open("data/tagged_overview.txt", "r", encoding="utf-8") as f:
    text = f.read()

raw_documents = [Document(page_content=text)]
text_splitter = CharacterTextSplitter(chunk_size= 0, chunk_overlap= 0, separator= "\n")
documnets = text_splitter.split_documents(raw_documents)
db_movies = Chroma.from_documents(
    documents=documnets,
    embedding=embedding_model
)


all_genres = [
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama',
    'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance',
    'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western'
]


def retrieve_semantic_recommendations(
    query: str,
    genre: str = "All",
    initial_top_k: int = 50,
    final_top_k: int = 24
) -> pd.DataFrame:
    
    recs = db_movies.similarity_search_with_score(query, k=initial_top_k)
    movie_list = [int(doc.page_content.strip('"').split()[0]) for doc, _ in recs]
    movie_recs = movies[movies["id"].isin(movie_list)]

    if genre != "All" and genre in all_genres:
        movie_recs = movie_recs[movie_recs["genre_names"].apply(lambda genres: genre in genres)]

    return movie_recs.head(final_top_k)



def recommend_movies(
    query: str,
    genre: str = None,
):
    
    recommendations = retrieve_semantic_recommendations(query, genre)
    results = []

    for _, row in recommendations.iterrows():
        overview = row["overview"]
        truncated_desc_split = overview.split()
        truncated_overview = " ".join(truncated_desc_split[:30]) + "..."

        
        caption = f"{row['original_title']} : {truncated_overview}"
        results.append((row["large_poster"], caption))
    return results

genre = ["All"] + all_genres

with gr.Blocks(theme=gr.themes.Glass()) as dashboard:
    gr.HTML("<h1 style='text-align:center; font-size:48px; margin-top:10px;'>🍿 BotCorn</h1>")

    with gr.Row():
        user_query = gr.Textbox(
            label="Please enter a description of a movie:",
            placeholder="e.g. A movie about war")
        category_dropdown = gr.Dropdown(
            choices=genre,
            value="All",
            label="Select a category:"
        )
        
        submit_button = gr.Button("Find recommendations")

    gr.Markdown("## Recommendations")
    output = gr.Gallery(
        label="Recommended Movies",
        columns=8,
        rows=3
    )

    submit_button.click(fn = recommend_movies,
                        inputs = [user_query, category_dropdown],
                        outputs = output)

   
if __name__ == "__main__":
    dashboard.launch()

    

    
        