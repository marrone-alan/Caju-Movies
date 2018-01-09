import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_cast, movie_genre, movie_duration):
        """Constructor

        Keyword arguments:
        movie_title -- the title of the movie
        movie_storyline -- a short narrative of the movie
        poster_image -- the link to the poster
        trailer_youtube -- the link to the youtube trailer
        movie_cast -- some of the stars of the movie
        movie_genre -- some of the categories of the movie
        movie_duration -- the duration of the movie
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = movie_cast
        self.genre = movie_genre
        self.duration = movie_duration
