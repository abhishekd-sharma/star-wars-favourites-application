from flask import Flask, request
import requests

import utils

app = Flask(__name__)

'''
favourites data to maintain favourites per user
    favourites = {
        user_id : {
            url : {
                'title/name': ,
                'url' : ,
                'created': ,
                'updated': ,
                'is_favourite': 
            }
        }
    }
'''
favorites_data = {} 
planets_data = utils.get_planets()
movies_data = utils.get_movies()

@app.route('/welcome')
def welcome():
    return {'message':'Welcome to Favourites app for Star Wars collection'}, 200

@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Returns the list of movies with the specified fields.
    If the 'query' parameter is provided, returns the movies that match the search query.
    """
    data = request.get_json()
    user_id = data['user_id']
    query = data['query'] or None
    movies = []
    if not user_id:
        return {'message': 'User not found, please enter correct user id.'}, 400
    if query is not None:
        search_query = query.lower()
        for movie in movies_data:
            if search_query == favorites_data.get(user_id, {}).get(movie['url'], {}).get('title', '').lower() or search_query == movie.get('title').lower():
                movies.append(utils.movie_response(favorites_data, movie, user_id))
    else:
        for movie in movies_data:
            movies.append(utils.movie_response(favorites_data, movie, user_id))
    return {'movies': movies}, 200

@app.route('/planets', methods=['GET'])
def get_planets():
    """
    Returns the list of planets with the specified fields.
    If the 'query' parameter is provided, returns the planets that match the search query.
    """
    data = request.get_json()
    user_id = data['user_id']
    query = data['query'] or None
    planets = []
    if not user_id:
        return {'message': 'User not found, please enter correct user id.'}, 400
    if query is not None:
        search_query = query.lower()
        for planet in planets_data:
            if search_query == favorites_data.get(user_id, {}).get(planet['url'], {}).get('name', '').lower() or search_query == planet.get('name').lower():
                planets.append(utils.planet_response(favorites_data, planet, user_id))
    else:
        for planet in planets_data:
            planets.append(utils.planet_response(favorites_data, planet, user_id))
    return {'planets': planets}, 200

@app.route('/add_favourite', methods = ['POST'])
def add_favourite():
    """
    Add favourite movies/planets
    If the 'custom_value' parameter is provided, set the name/title for planets/movie.
    """
    data = request.get_json()
    user_id = data.get('user_id', '')
    if not user_id:
        return {'message': 'User not found, please enter correct user id.'}, 400
    custom_value = data.get('custom_value', None)
    type = data.get('type', '')
    if type == 'movie':
        movie_id = str(data.get('id', ''))
        if not movie_id:
            return {'error': 'Please enter movie id to add it to favourites'}
        
        movie = requests.get(utils.MOVIES_URL+movie_id).json()
        movie_data = utils.movie_data(movie, custom_value)
        favorites_data.setdefault(user_id, {}).update(movie_data)
        return {'message': 'Your movie is added into your favourites'}, 200
    elif type == 'planet':
        planet_id = str(data.get('id', ''))
        if not planet_id:
            return {'error': 'Please enter planet id to add it to favourites'}
        
        planet = requests.get(utils.PLANETS_URL+planet_id).json()
        planet_data = utils.planet_data(planet, custom_value)
        favorites_data.setdefault(user_id, {}).update(planet_data)
        return {'message': 'Your planet is added into your favourites'}, 200

    return {'error': 'Favourite type does not matched, please enter correct type.'}, 200
