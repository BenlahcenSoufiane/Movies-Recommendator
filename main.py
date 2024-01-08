from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import requests
import re
app = Flask(__name__)

# Charger les données
users = pd.read_csv('users.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])
movies = pd.read_csv('Ratting.csv', usecols=['movie_id','title','genres','rating'])


# Préparer la matrice TF-IDF
movies['genres'] = movies['genres'].str.split('|')
movies['genres'] = movies['genres'].fillna("").astype('str')

# Correction du paramètre min_df pour TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', token_pattern=r"(?u)\b\w[\w-]*\w\b", ngram_range=(1, 1), min_df=1, stop_words='english')
tfidf_matrix = tf.fit_transform(movies['genres'])

# Calculer la similitude cosinus
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])

# Fonction de recommandation de genre
def genre_recommendations(title, M, items, k=14):
    if title not in M.index:
        return "Film non trouvé."
    ix = M.loc[:, title].to_numpy().argpartition(range(-1, -k, -1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(title, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
######
###
def get_movie_poster_url(movie_title):
    tmdb_api_key = 'd068096d3c09b740ead5107377ef29c9'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': tmdb_api_key, 'query': movie_title}

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'results' in data and data['results']:
        # Assuming the first result is the most relevant
        poster_path = data['results'][0]['poster_path']
        if poster_path:
            return f'https://image.tmdb.org/t/p/w500/{poster_path}'

    # If no valid poster URL is found, return None
    return None

# Update your home route to include movie posters
def clean_movie_title(title):
    # Use regular expression to remove year in parentheses at the end of the title
    cleaned_title = re.sub(r'\(\d{4}\)$', '', title.strip())
    return cleaned_title

# Update your home route to include movie posters
@app.route('/', methods=['GET', 'POST'])
def home():
    top_rated_movies = movies.sort_values(by='rating', ascending=False).head(4)

    for index, row in top_rated_movies.iterrows():
        movie_title = row['title']
        cleaned_title = clean_movie_title(movie_title)
        poster_url = get_movie_poster_url(cleaned_title)

        if poster_url:
            # Append the poster URL to the DataFrame
            top_rated_movies.at[index, 'poster_url'] = poster_url
        else:
            # Set a default poster URL if not found
            top_rated_movies.at[index, 'poster_url'] = 'https://th.bing.com/th/id/R.795cb58050fdc49e032b51a18b640ae8?rik=E7U1xE2qtjlH0A&riu=http%3a%2f%2fgraphicdesignjunction.com%2fwp-content%2fuploads%2f2012%2f05%2flarge%2fmovie-poster-15.jpg&ehk=qZXiHOmcMXCoiZRB%2b5xkS6g8P1gXlv7QP1H7BEu52lE%3d&risl=&pid=ImgRaw&r=0'

    return render_template('index.html', top_rated_movies=top_rated_movies)


   

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        recommendations = genre_recommendations(movie_title, cosine_sim_df, movies[['title', 'genres']])
        ###################################################################################################
        for index, row in recommendations.iterrows():
            movie_title2 = row['title']
            cleaned_title2 = clean_movie_title(movie_title2)
            poster_url2 = get_movie_poster_url(cleaned_title2)

            if poster_url2:
                # Append the poster URL to the DataFrame
                recommendations.at[index, 'poster_url'] = poster_url2
            else:
                # Set a default poster URL if not found
                recommendations.at[index, 'poster_url'] = 'https://th.bing.com/th/id/R.795cb58050fdc49e032b51a18b640ae8?rik=E7U1xE2qtjlH0A&riu=http%3a%2f%2fgraphicdesignjunction.com%2fwp-content%2fuploads%2f2012%2f05%2flarge%2fmovie-poster-15.jpg&ehk=qZXiHOmcMXCoiZRB%2b5xkS6g8P1gXlv7QP1H7BEu52lE%3d&risl=&pid=ImgRaw&r=0'
        ##################################################################################################
        return render_template('recommendations.html', recommendations=recommendations, movie_title2=movie_title2, poster_url2=poster_url2)
    
    return render_template('recommendations.html', recommendations=None)



@app.route('/about-us', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)