# BotCorn

🎬 **BotCorn** is a smart movie recommendation system that uses semantic search and genre filtering to help users discover movies based on natural language descriptions.  
It leverages NLP, vector similarity, and TMDB metadata to offer accurate, visually engaging suggestions through an interactive Gradio dashboard.

<p align="center">
  <img src="https://github.com/Abdallah-Ahmed0/BotCorn/blob/main/image.png" width="600"/>
</p>





## Data Overview

The dataset used in this project is the **TMDB 9000+ Movie Genres Dataset**, which includes detailed information about over 9,000 movies. Each movie record contains metadata such as:

* `id`: Unique movie identifier
* `title`: Title of the movie
* `overview`: Brief description
* `genre_ids`: A list of numeric genre identifiers for each movie

This dataset is a great source for understanding movie trends, popularity metrics, and genre classification across thousands of films from The Movie Database (TMDB).

---

##  Data Preparation

The dataset underwent several data cleaning and preparation steps, including handling missing values, standardizing formats, and correcting data types.
### Cleaning & preparation

### Mapping Genre IDs to Genre Names

The original dataset represents genres as lists of numeric IDs (`genre_ids`), which are not human-readable. To make the data more interpretable, I performed a mapping from these IDs to their corresponding genre names using a separate `genres` table.

However, the `genre_ids` column contained **stringified lists** (e.g., `"[18, 35]"`) instead of actual Python lists (`[18, 35]`). To resolve this:

1. I used `ast.literal_eval()` to safely convert these string representations into actual lists.
2. Then, created a mapping dictionary from genre ID to genre name.
3. Finally, applied a function to each row to replace genre IDs with readable genre names.


**Result**: The dataset now includes a `genre_names` column with clear, descriptive genre labels for each movie.

---


## 🖼️ Adding Poster URLs via TMDb API

After the data cleaning step, I enriched the dataset by retrieving poster images for each movie using the [TMDb API](https://www.themoviedb.org/documentation/api).

### What has done

* Queried TMDb's search endpoint using each movie's title.
* Extracted the poster path from the top search result.
* Constructed full image URLs and added them as a new column in the dataset.

### 🔐 API Key

I securely loaded the TMDb API key from a `.env` file using `python-dotenv`.


### Output

A new column `poster_url` was added to the dataset, containing direct links to high-quality poster images for most movies. This enables visual enhancements in dashboards, reports, or apps.

---

## 🔍 Semantic Search Implementation

The project implements a semantic book recommendation system using advanced NLP techniques:

### Core Components
- **Vector Database**: Uses LangChain's Chroma for efficient similarity search
- **Embedding Model**: Implements Sentence-BERT's `all-MiniLM-L6-v2` model from Hugging Face
  - A lightweight and efficient sentence transformer model
  - Optimized for generating text embeddings
  - 384-dimensional dense vector representations
  - Excellent balance of speed and accuracy
  - Trained on over 1 billion sentence pairs
- **Search Algorithm**: Semantic similarity matching with customizable results

### Features
- Natural language query processing
- Contextual understanding of book descriptions
- Customizable number of recommendations
- Returns complete book metadata
- Fast and efficient similarity matching


---


## Final Step: Interactive Movie Recommendation Dashboard with Gradio

To provide an intuitive and user-friendly interface for exploring movie recommendations, i built an interactive dashboard using **Gradio**.

### What it does:

* **User Input:** Allows users to enter a natural language description of a movie plot or theme.
* **Genre Filter:** Provides a dropdown menu for users to filter recommendations by movie genre, including an "All" option.
* **Semantic Search:** Uses a semantic similarity search over movie plot embeddings to find relevant movies matching the user query.
* **Dynamic Filtering:** Applies genre-based filtering on the recommended movies if a specific genre is selected.
* **Results Display:** Presents recommended movies as a visually appealing gallery of posters with centered, larger movie titles and truncated descriptions.

### Key Features:

* **Powered by LangChain & HuggingFace Embeddings:** For robust text understanding and similarity search.
* **Real-Time Recommendations:** Updates results instantly based on user input and genre selection.
* **Visual Output:** Displays movie posters alongside formatted captions for easy browsing.
* **Responsive UI:** Built with Gradio’s Blocks interface and customizable themes.

### How to run:

1. Ensure dependencies are installed (`pandas`, `gradio`, `langchain`, `huggingface` libraries).
2. Prepare your dataset (`movies_with_posters.csv`) and text embeddings.
3. Run the dashboard script:

   ```bash
   python dashboard.py
   ```
4. Open the local URL provided by Gradio in your browser.
5. Enter a movie description, select a genre, and get personalized movie recommendations instantly.

---

### 📦 Installation

Make sure Python 3.8+ is installed on your machine.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/botcorn.git
   cd botcorn
   ```

2.**Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

---

### 📁 Project Structure

```bash
botcorn/
│
├── data/
│   ├── movies_with_posters.csv
│   └── tagged_overview.txt
│__ notebooks/
|   |__ data_exploration.ipynb
|   |__ posters_scrapping.ipynb
|   |__ vector_search.ipynb
|
├── dashboard.py
├── .env
├── README.md
└── requirements.txt
```

---
```bash
git clone https://github.com/Abdallah-Ahmed0/MyBookLlm
cd my_project
pip install -r requirements.txt
```
---
