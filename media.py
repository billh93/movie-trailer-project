import webbrowser


class Movie:
    """ This class provides a way to store movie related information. """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        This is the constructor method where we create our components for our
        movies instances.

        Attributes:
        movies (array): An array that contains instances of the Movie class.
        movie_title (str): This argument is our movie title.
        movie_storyline (str): This argument is our movie storyline.
        poster_image (str): This argument is our movie poster image url.
        trailer_youtube (str): This argument is our youtube video url.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This function opens up a new window/tab on our browser to the youtube
        url where it plays the specified movie trailer that you clicked on.
        """
        webbrowser.open(self.trailer_youtube_url)
