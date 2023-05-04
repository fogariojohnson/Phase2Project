"""
===========================================================
                 Project Part 2
              Second Phase of the Project
              By Frelin C. Ogario-Johnson
===========================================================
"""

import statistics
import random
import sys
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import movie_storage
import html_generator
import update_generator


def exit_movie():
    """Exits the app"""
    print("Bye!")
    sys.exit()


def movie_list():
    """ Displays the dictionary of movies[key] and its rating(value)

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    print(f"{len(movies_stored)} movies in total")
    for key, value in movies_stored.items():
        print(f"\033[34m{key}\n\033[0mRating: {value['rating']}\nYear: {value['year']}")


def add_movie():
    """ Adds a movie title[key] and its rating(value)

    Returns:
        None
    """
    movie_name = input("Enter new movie name: ")
    imdb_url = input("Enter imdb url for the movie: ")
    movies_stored = movie_storage.list_movies()
    # Validating an update not an additional movie
    for name in list(movies_stored.keys()):
        if movie_name == name:
            print(f"{movie_name} is already in the movie app."
                  f" Do you want to update {movie_name}? ")
            user_input = input("Press 'Y' for Yes and 'N' for No: ")
            if user_input == "Y":
                movie_rating = float(input("Enter new movie rating (0-10): "))
                if movie_rating <= 10:
                    movies_stored[movie_name] = movie_rating
                    print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
                else:
                    print(f"\033[31m {movie_rating} is invalid.\033[0m")
            elif user_input == "N":
                run_manager()
        # Adding a new movie title and rating
        else:
            movie_storage.add_movie(movie_name, imdb_url)
    print(f"\033[34m Movie {movie_name} successfully added. \033[0m")


def delete_movie():
    """ Deletes a movie title[key] and its rating(value)

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    movie_name = input("Enter movie name to delete: ")
    if movie_name in movies_stored:
        movie_storage.delete_movie(movie_name)
        print(f"The movie {movie_name} successfully deleted")
    else:
        print(f"\033[31m Movie {movie_name} doesn't exist."
              f" Choose from the following movies \033[0m")
        movie_list()


def update_movie():
    """ Updates the rating(value) of a movie[key]

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    movie_name = input("Enter movie name: ")
    if movie_name in movies_stored:
        movie_note = input("Enter movie notes: ")
        update_generator.update_html_structure(movie_name, movie_note)
        update_generator.update_html_maker(movie_name, movie_note)
        update_generator.update_css_maker()
        print(f'The movie "{movie_name}" is successfully updated.')
    else:
        print(f"\033[31m Movie {movie_name} doesn't exist."
              f" Choose from the following movies \033[0m")
        movie_list()


def movie_average():
    """Calculates the average rating of all movies in the dictionary

    Returns:
        None
    """
    movie_stored = movie_storage.list_movies()
    total_rating = 0
    for movie in movie_stored.values():
        total_rating += movie["rating"]
    average_rating = total_rating / len(movie_stored)
    print(f"Average: {average_rating}")


def movie_median():
    """Identifies the median rating of all the movies in the dictionary

    Returns:
        None
    """
    movie_stored = movie_storage.list_movies()
    ratings = [value["rating"] for value in movie_stored.values()]
    median_rating = statistics.median(ratings)
    print(f"Median rating: {median_rating}")


def best_movie():
    """Identifies the highest rating of all the movies in the dictionary

    Returns:
        None
    """
    movie_stored = movie_storage.list_movies()
    key_ratings = [(key, value["rating"]) for key, value in movie_stored.items()]
    max_key, max_rating = max(key_ratings, key=lambda x: x[1])
    print(f"Best movie: {max_key} ({max_rating})")


def worst_movie():
    """Identifies the highest rating of all the movies in the dictionary

    Returns:
        None
    """
    movie_stored = movie_storage.list_movies()
    key_ratings = [(key, value["rating"]) for key, value in movie_stored.items()]
    min_key, min_rating = min(key_ratings, key=lambda x: x[1])
    print(f"Best movie: {min_key} ({min_rating})")


def movie_statistics():
    """Serves as the structure for the statistics of the movies dictionary

    Returns:
        None
    """
    movie_average()
    movie_median()
    best_movie()
    worst_movie()


def random_movie():
    """ Randomly choose a movie title[key]

    Returns:
        None
    """
    movie_stored = movie_storage.list_movies()
    key, value = random.choice(list(movie_stored.items()))
    print(f"Your movie tonight: {key}, it's rated {value['rating']}")


def search_movie():
    """ Search a movie title[key] and its possible matching string

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    movie_name = input("Enter a search term: ")
    lowercase_movie_name = movie_name.lower()
    found_movies = []
    for movie, rating in movies_stored.items():
        lowercase_movies = movie.lower()
        if lowercase_movie_name in lowercase_movies:
            found_movies.append((movie, rating['rating']))
    if found_movies:
        found_movies.sort(key=lambda x: x[1], reverse=True)
        for movie, rating in found_movies:
            print(f"{movie}, {rating}")
    else:
        print(f"The search term {movie_name} is not found")


def search_movie_distance(movie_name):
    """ Search for a matching movie title

     Args:
        movie_name(str): Input user for searching term

    """
    movies_stored = movie_storage.list_movies()
    close_movie_match = []
    for movie, stat in movies_stored.items():
        ratio = fuzz.token_set_ratio(movie_name.lower(), movie.lower())
        if ratio >= 55:
            close_movie_match.append((movie, stat["rating"]))
    if close_movie_match:
        close_movie_match.sort(key=lambda x: x[1], reverse=True)
        print(f"The movie {movie_name} does not exist. Did you mean: ")
        for movie, rating in close_movie_match:
            print(f"{movie}, {rating}")
        validation = input("Press 'Y' for Yes and 'N' for No: ")
        if validation == "Y":
            for movie, rating in close_movie_match:
                print(f"{movie}, {rating}")
        elif validation == "N":
            print(f"Sorry, the movie '{movie_name}' doesn't exist")
        else:
            print("Sorry wrong input")
    else:
        print(f"Sorry, the movie '{movie_name}' doesn't exist")


def sorted_movie():
    """ Sorts the movie title[key] based on its rating(value) in descending order

     No Args:
        dict: It is using the dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    sorted_movies = dict(sorted(movies_stored.items(),
                                key=lambda x: x[1]['rating'], reverse=True))
    for key, value in sorted_movies.items():
        print(f"{key}: {value['rating']}")


def movie_histogram():
    """ Allows user to save the histogram of ratings in different file type specified

    Returns:
        None
    """
    movies_stored = movie_storage.list_movies()
    rating_list = []
    for value in movies_stored.values():
        rating_list.append(value['rating'])
    plt.hist(rating_list, bins=5)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.title("Movie Rating")
    filename = input("Choose a filename for your histogram: ")
    filetype = input("In which filetype do you want to save the histogram as? ")
    # Checking the supported format
    if filetype in "eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff":
        file_name = filename + "." + filetype
        plt.savefig(file_name)
        print(f'"{file_name}" is successfully created')
    else:
        print("Format is not supported. Please try a different file format")
        run_manager()


def end_prompt():
    """Prompts user to press Enter key every end of the method or function"""
    enter = input("\033[33m" + "Please enter to continue " + "\033[0m")
    if enter == "":
        run_manager()
    else:
        print("\033[31m" + "Error! Please press Enter key to continue" + "\033[0m")
        run_manager()


def run_manager():
    """
    Displays a menu and allows the user to choose from a list of options.
    """
    while True:
        print("\033[36m Menu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n"
              "4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n"
              "8. Movies sorted by rating\n9. Creating Rating Histogram\n"
              "10. Generate website\033[0m")
        # Define the functions for each choice
        functions = {
            0: exit_movie,
            1: movie_list,
            2: add_movie,
            3: delete_movie,
            4: update_movie,
            5: movie_statistics,
            6: random_movie,
            7: search_movie,
            8: sorted_movie,
            9: movie_histogram,
            10: html_generator.html_maker
        }

        # Get the user's choice
        choice = int(input("Enter your choice: "))

        if choice in functions:
            functions[choice]()
            end_prompt()
        else:
            print("\033[31m" + "Error! Please choose from numbers 0 to 10." + "\033[0m")
            run_manager()


if __name__ == "__main__":
    run_manager()
