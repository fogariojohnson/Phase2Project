import movie_storage


def html_structure():
    """
    Creates the HTML structure

    Returns:
         output: HTML structure
    """
    movies = movie_storage.list_movies()
    output = ''
    for title, stat in movies.items():
        poster = stat["poster url"]
        flag = stat["flag"]
        imd_url = stat["imdb_link"]
        movie_title = title
        rating = stat["rating"]
        year = stat["year"]
        character = stat["character"]
        output += '\t<li>\n'
        output += '\t\t<div class="movie">\n'
        output += f'<a href ="{imd_url}"\n>'
        output += '\t\t\t<img class="movie-poster"\n'
        output += f'\t\t\t\tsrc="{poster}"\n\t\t\t\ttitle="" alt ="{movie_title}"/></a>\n'
        output += f'\t\t\t\t<img src={flag} alt="flag origin">\n'
        output += f'\t\t\t<div class="movie-title">{movie_title}</div>\n'
        output += f'\t\t\t<div class="movie-rating">Rating: {rating}</div>\n'
        output += f'\t\t\t<img src={character} alt="emoticon">\n'
        output += f'\t\t\t<div class="movie-year">{year}</div>\n'
        output += '\t\t</div>\n\t</li>\n'
    print("Website was generated successfully")
    return output


def read_html_template():
    """
    Loads HTML file template

    Returns:
        data(dict): the movies' dictionary
    """
    with open("_static/index_template.html", "r") as file_obj:
        data = file_obj.read()
        return data


def html_maker():
    """ Creates the HTML file

    Returns:
        new_content(str): HTML structure
    """
    with open("_static/movie_app.html", "w") as new_file:
        old_data = read_html_template()
        new_data = html_structure()
        new_content = old_data.replace("__TEMPLATE_TITLE__", "My Collection of Movies")
        new_content = new_content.replace("__TEMPLATE_MOVIE_GRID__", new_data)
        new_file.write(new_content)
        return new_content
