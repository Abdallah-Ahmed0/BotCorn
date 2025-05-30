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

