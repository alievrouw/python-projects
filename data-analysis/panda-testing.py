import pandas as pd

# Data set source
# https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset

IMDb = '/Users/adam/Downloads/IMDb_All_Genres_etf_clean1.csv'
df = pd.read_csv(IMDb)

print("")
print(df.columns)

my_headers = ['Movie_Title', 'Year', 'Director', 'main_genre']
ds = pd.DataFrame(df, columns=my_headers)
print("")

# Show the top 10 most common director's names
common_directors = ds['Director'].value_counts().nlargest(10)
# common_directors = pd.Series(' '.join(ds['Director']).split()).value_counts()[:10]
print(common_directors)
print("")

# Print the top 10 most common movie release years
common_years = ds['Year'].value_counts().nlargest(10)
print(common_years)
print("")

# grouped_df = df.groupby(['Year']).max()
# print(grouped_df['Movie_Title'])
# print("")

# ds.groupby('Movie_Title', 'Year', 'main_genre').