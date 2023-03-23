Instructions to setup the project - 
1. Install Python3
2. Install flask - 
    1. Intall virtualenv using the command -> $ sudo python3 -m pip3 install virtualenv
    2. Create an environment using below commands -> 
        1. $ mkdir </project name/>
        2. $ cd </project name/>
        3. $ python3 -m venv </name of environment/>
    3. Activate the environment -> $ source </name of environment/>/bin/activate
    4. Install flask -> $ pip3 install flask
    5. Install requests -> pip3 install requests
4. Define the environment variable that specifies the script using the command below -> 
    1. $ export FLASK_APP=favourites_app.py
5. Use the command to run the flask application -> 
    1. $ flask -A favourites_app.py --debug run
6. After this open postman and use the following apis accordingly -> 
    1. /movies -> This api is to list down the movies
        1. Params -> user_id, query(filters on the title of movies)
        2. Response -> List all movies on the basis of query filter and user_id,if provided else returns list of all movies for the given user_id
        3. Error response -> If user_id is not provided, return error message
    2. /planets -> This api is to list down the planets 
        1. Params -> user_id, query(filters on the name of planets)
        2. Response -> List all planets on the basis of query filter and user_id,if provided else returns list of all planets for the given user_id
        3. Error response -> If user_id is not provided, return error message
    3. /add_favourite -> This api is to add any favourite movie or planet for the user
        1. Params -> user_id, id = id of movie/planet, custom_value = custom name/title of planet/movie, type = movie/planet(the favourite type)
        2. Response -> Successful message of favourite being added
        3. Error -> If user_id not found or if planet/movie id not found or type not found correct
        
