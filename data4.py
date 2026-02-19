import pandas as pd

# ===============================
# Load Dataset
# ===============================
book = pd.read_csv('book.csv')

# ===============================
# Basic Information About Dataset
# ===============================
print("========== Dataset Preview ==========")
print(book.head(5))

print("\n========== Dataset Shape ==========")
print("Rows and Columns:", book.shape)

print("\n========== Dataset Info ==========")
print(book.info())

# ===============================
# Overall Rating Analysis
# ===============================
print("\n========== Overall Rating ==========")
overall_mean = book['Rating'].mean()
print("Average Rating:", overall_mean)

# ===============================
# Rating by Genre
# ===============================
print("\n========== Average Rating by Genre ==========")
genre_rating = book.groupby('Genre')['Rating'].mean()
print(genre_rating)

# ===============================
# Best and Worst Ratings
# ===============================
print("\n========== Best and Worst Ratings ==========")
best_rating = book['Rating'].max()
worst_rating = book['Rating'].min()

print("Best Rating:", best_rating)
print("Worst Rating:", worst_rating)

# ===============================
# Book(s) with Maximum Pages
# ===============================
print("\n========== Longest Book(s) ==========")
max_pages = book['Pages'].max()
print("Maximum Pages:", max_pages)

longest_books = book[book['Pages'] == max_pages]
print(longest_books)

# ===============================
# Best and Worst Genre Based on Average Rating
# ===============================
print("\n========== Genre Performance ==========")

best_genre = genre_rating.idxmax()
best_genre_score = genre_rating.max()

worst_genre = genre_rating.idxmin()
worst_genre_score = genre_rating.min()

print("Best Genre:", best_genre)
print("Average Rating:", best_genre_score)

print("Worst Genre:", worst_genre)
print("Average Rating:", worst_genre_score)