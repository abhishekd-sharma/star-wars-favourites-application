import requests

# Load data from the Star Wars API
BASE_URL = "https://swapi.dev/api"
PLANETS_URL = "{0}/planets/".format(BASE_URL)
MOVIES_URL = "{0}/films/".format(BASE_URL)

def get_planets():
    response = requests.get(PLANETS_URL)
    return response.json().get("results", [])

def get_movies():
    response = requests.get(MOVIES_URL)
    return response.json().get("results", [])

def movie_response(favorites_data, movie, user_id):
    return {
        'title': favorites_data.get(user_id, {}).get(movie['url'], {}).get('title', movie['title']),
        'release_date': movie['release_date'],
        'created': movie['created'],
        'updated': movie['edited'],
        'URL': movie['url'],
        'is_favourite': favorites_data.get(user_id, {}).get(movie['url'], {}).get('is_favourite', False)
    }

def planet_response(favorites_data, planet, user_id):
    return {
        'name': favorites_data.get(user_id, {}).get(planet['url'], {}).get('name', planet['name']),
        'created': planet['created'],
        'updated': planet['edited'],
        'URL': planet['url'],
        'is_favourite': favorites_data.get(user_id, {}).get(planet['url'], {}).get('is_favourite', False)
    }

def movie_data(movie, custom_value):
    return {
            movie['url']: {
                'title': custom_value if check_custom_value(custom_value) else movie['title'],
                'release_data': movie['release_date'],
                'created': movie['created'],
                'updated': movie['edited'],
                'URL': movie['url'],
                'is_favourite': True
            }
        }

def planet_data(planet, custom_value):
    return {
            planet['url']: {
                'name': custom_value if check_custom_value(custom_value) else planet['name'],
                'created': planet['created'],
                'updated': planet['edited'],
                'URL': planet['url'],
                'is_favourite': True
            }
        }

def check_custom_value(custom_value):
    if custom_value=='' or custom_value is None:
        return False
    return True