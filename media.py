import webbrowser


# define a class Movie.

class Movie():

    # define __init__ with the given 4 arguements.
    def __init__(self, movie_title, movie_poster_image, movie_trailer):
        # initializing class Movie variables.

        self.title = movie_title
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer

    # defining a fuction a to open the movie trailer.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
