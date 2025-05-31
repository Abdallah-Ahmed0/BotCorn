# BotCorn





## Data Overview

The dataset used in this project is the **TMDB 9000+ Movie Genres Dataset**, which includes detailed information about over 9,000 movies. Each movie record contains metadata such as:

* `id`: Unique movie identifier
* `title`: Title of the movie
* `overview`: Brief description
* `release_date`: Date the movie was released
* `popularity`: Popularity score
* `vote_average`: Average user rating
* `genre_ids`: A list of numeric genre identifiers for each movie

This dataset is a great source for understanding movie trends, popularity metrics, and genre classification across thousands of films from The Movie Database (TMDB).

---

##  Data Preparation

The dataset underwent several data cleaning and preparation steps, including handling missing values, standardizing formats, and correcting data types.

###  Final Step – Mapping Genre IDs to Genre Names

The original dataset represents genres as lists of numeric IDs (`genre_ids`), which are not human-readable. To make the data more interpretable, we performed a mapping from these IDs to their corresponding genre names using a separate `genres` table.

However, the `genre_ids` column contained **stringified lists** (e.g., `"[18, 35]"`) instead of actual Python lists (`[18, 35]`). To resolve this:

1. We used `ast.literal_eval()` to safely convert these string representations into actual lists.
2. Then, we created a mapping dictionary from genre ID to genre name.
3. Finally, we applied a function to each row to replace genre IDs with readable genre names.


**Result**: The dataset now includes a `genre_names` column with clear, descriptive genre labels for each movie.

---

Perfect — here’s a clean **README section** (without code) describing the step you just completed:

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


