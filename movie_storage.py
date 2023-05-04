import json
import requests


def emoticon_maker(name):
    """ Creates country code based from user input

    Args:
        name(str): Emoticon to display

    Returns:
        character(str): A link to the character image
    """
    api_key = "RRhRnIM0DDVn6BbmwULBzQ==n9DVxWtNtkN2nwH5"
    api_url = 'https://api.api-ninjas.com/v1/emoji?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    list_options = response.json()
    for char in list_options:
        character = char["image"]
        return character


def get_country_code():
    """ Creates country code based from user input

    Returns:
        country_dict(dict): A dictionary of countries and its code
    """
    api_key_holiday = "a47a88cb-3005-44d5-99d8-81710c7975cb"
    country_list = requests.get(f"https://holidayapi.com/v1/countries?pretty&key={api_key_holiday}")
    res = country_list.json()
    countries = res["countries"]
    country_dict = {}
    for country in countries:
        country_entry = country['name']
        code_entry = country['code']
        country_dict[country_entry] = code_entry
    return country_dict


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    with open("data.json", "r") as file_obj:
        file = json.loads(file_obj.read())

    movies = {}
    for movie, stat in file.items():
        rating = stat["rating"]
        year = stat["year"]
        url = stat["poster url"]
        imdb = stat["imdb_link"]
        flag = stat["flag"]
        character = stat["character"]
        info = {
            "rating": rating,
            "year": year,
            "poster url": url,
            "imdb_link": imdb,
            "flag": flag,
            "character": character
             }
        movies[movie] = info
    return movies


def add_movie(title, imdb_url):
    """
    Adds a movie to the movies' database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.

    Args:
        title(str): user input for a movie title to add
        imdb_url(str): user input for imdb link

    Raises:
        KeyError: If movie title is not found in the database
        Exception: Covers all the other error that might occur and explains user the reason.
    """
    api_key = "e2e17332"
    url_omd = f"http://www.omdbapi.com/?apikey={api_key}&t="

    try:
        with open("data.json", "r") as file_obj:
            movies = json.load(file_obj)

        add_url = url_omd + title
        movie = requests.get(add_url)
        res = movie.json()
        rating_values = [float(rating['Value'][0][:3]) for rating in res['Ratings']]
        rating = rating_values[0]
        country = res["Country"]

        # To create the flag variable
        if "," in country:
            country = country.split(",")[0]
        country_code = get_country_code()
        country_origin = country_code[country]

        # To create an emoticon for the character variable
        if rating >= 6:
            emoticon = "smiling face"
        else:
            emoticon = "sad"
        character = emoticon_maker(emoticon)
        new_movie = {
            res["Title"]: {
                "rating": rating,
                "year": res["Year"],
                "poster url": res["Poster"],
                "imdb_link": imdb_url,
                "flag": f"https://flagsapi.com/{country_origin}/shiny/64.png",
                "character": character
            }
        }

        movies.update(new_movie)

        with open("data.json", "w") as new_info:
            json.dump(movies, new_info)
    except KeyError:
        print("Sorry, movie title does not exist!")
    except Exception as e:
        print(f"Error, API is not accessible. Possible reasons: {e}")


def delete_movie(title):
    """
    Deletes a movie from the movies' database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.

    Args:
        title(str): user input for a movie title to delete
    """

    with open("data.json", "r") as file_obj:
        movies = json.load(file_obj)

    del movies[title]

    with open("data.json", "w") as new_file:
        json.dump(movies, new_file)


def update_movie(title, rating):
    """
    Updates a movie from the movies' database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.

    Args:
        title(str): user input for a movie title to update
        rating(float): the updated rating of the movie
    """
    with open("data.json", "r") as file_obj:
        movies = json.load(file_obj)

    movies[title]["rating"] = rating

    with open("data.json", "w") as new_info:
        json.dump(movies, new_info)
