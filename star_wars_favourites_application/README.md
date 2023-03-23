Instructions to setup the project - 
1. Install Python3
2. Install flask - 
    a. Intall virtualenv using the command -> $ sudo python3 -m pip3 install virtualenv
    b. Create an environment using below commands -> 
        $ mkdir <project name>
        $ cd <project name>
        $ python3 -m venv <name of environment>
    d. Activate the environment -> $ source <name of environment>/bin/activate
    e. Install flask -> $ pip3 install flask
    f. Install requests -> pip3 install requests
4. Define the environment variable that specifies the script using the command below -> 
    $ export FLASK_APP=favourites_app.py
5. Use the command to run the flask application -> 
    $ flask -A favourites_app.py --debug run
6. After this open postman and use the following apis accordingly -> 
    a. /movies -> This api is to list down the movies
        i. Params -> user_id, query(filters on the title of movies)
        ii. Response -> List all movies on the basis of filter,if provided else returns list of all movies
        iii. Error response -> If user_id is not provided, return error message
    b. /planets -> This api is to list down the planets 
        i. Params -> user_id, query(filters on the name of planets)
        ii. Response -> List all planets on the basis of filter,if provided else returns list of all planets
        iii. Error response -> If user_id is not provided, return error message
    c. /add_favourite -> This api is to add any favourite movie or planet for the user
        i. Params -> user_id, id = id of movie/planet, custom_value = custom name/title of planet/movie, type = movie/planet(the favourite type)
        ii. Response -> Successful message of favourite being added
        iii. Error -> If user_id not found or if planet/movie id not found or type not found correct
        