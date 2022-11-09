import pandas as pd

# Data set source
# https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset

df = pd.read_csv('/Users/adam/Downloads/IMDb_All_Genres_etf_clean1.csv', header=0)
new_headers = ['Movie_Title', 'Year', 'Director']
dataset = pd.DataFrame(df, columns=new_headers)
print("")

# Show the top 10 most common director's names
common_directors = pd.Series(' '.join(dataset['Director']).split()).value_counts()[:10]
print(common_directors)
print("")

# Print the top 10 most common movie release years
common_years =  pd.Series(' '.join(dataset['Year']).split()).value_counts()[10:]
print(common_years)
print("")