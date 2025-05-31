# BotCorn





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

