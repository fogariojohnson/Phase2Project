import html_generator
import movie_storage


def update_html_structure(movie_name, note):
    """ Creates the HTML structure
        Verify if a note is available to add

    Returns:
        output(str): HTML structure
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
        output += f'<a href ="{imd_url}">\n'
        output += '\t\t\t<img class="movie-poster"\n'
        if title == movie_name:
            output += f'\t\t\t\tsrc="{poster}"\n\t\t\t\ttitle="{note}" alt ="{movie_title}"/></a>\n'
        else:
            output += f'\t\t\t\tsrc="{poster}"\n\t\t\t\ttitle="" alt ="{movie_title}"/></a>\n'
        output += f'\t\t\t\t<img src={flag} alt="flag origin">\n'
        output += f'\t\t\t<div class="movie-title">{movie_title}</div>\n'
        output += f'\t\t\t<div class="movie-rating">Rating: {rating}</div>\n'
        output += f'\t\t\t<img src={character} alt="emoticon">\n'
        output += f'\t\t\t<div class="movie-year">{year}</div>\n'
        output += '\t\t</div>\n\t</li>\n'
    return output


def update_html_maker(movie_name, note):
    """ Creates the HTML file

    Args:
        movie_name(str): user input a movie title
        note(str): user input a description for the movie

    Returns:
        new_content(str): HTML structure
    """
    with open("_static/movie_app.html", "w") as new_file:
        old_data = html_generator.read_html_template()
        new_data = update_html_structure(movie_name, note)
        new_content = old_data.replace("__TEMPLATE_TITLE__", "My Collection of Movies")
        new_content = new_content.replace("__TEMPLATE_MOVIE_GRID__", new_data)
        new_file.write(new_content)
        return new_content


def update_css_structure():
    """ Creates a css style

    Returns:
        output(str): css style
    """
    output = ''
    output += '\n .movie-poster:hover .movie_postertext {\nvisibility: visible;\n'
    output += 'opacity: 1;\n}'
    return output


def read_css_template():
    """ Loads css file template

    Returns:
        data(str): css data
    """
    with open("_static/style.css", "r") as file_obj:
        data = file_obj.read()
        return data


def update_css_maker():
    """ Updates the css file

    Returns:
        new_content(str): CSS structure
    """
    old_data = read_css_template()
    new_data = update_css_structure()
    new_content = old_data + new_data
    with open("_static/style.css", "w") as file_obj:
        file_obj.write(new_content)
        return new_content
