#importing libraries
import pandas as pd
import streamlit as st
import pickle
import requests

#function for recommending 5 most similar movies
def recommend(movie_show):
    movie_idx = movies_shows[movies_shows['title'] == movie_show].index[0]
    movie_similarity = similarity[movie_idx]
    movies_list = sorted(list(enumerate(movie_similarity)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies_shows.iloc[i[0]].id
        recommended_movies.append(movies_shows.iloc[i[0]].title)
    return recommended_movies

#loading final DataFrame
movies_shows_final = pickle.load(open('movies_shows.pkl','rb'))
movies_shows = pd.DataFrame(movies_shows_final)

#loading 'similarity' matrix
similarity = pickle.load(open('similarity.pkl','rb'))

#selecting a title
st.title('Recommender System - Netflix TV Shows and Movies')

#defining user selection
selected_movie_name = st.selectbox("Please select a movie/show to get the recommendations:",movies_shows['title'].values)

#displaying 5 recommended movies
if st.button("Recommend"):
    names = recommend(selected_movie_name)
    st.text(names[0])
    st.text(names[1])
    st.text(names[2])
    st.text(names[3])
    st.text(names[4])