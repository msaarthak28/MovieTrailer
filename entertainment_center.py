# import the media file where class Movie is defined
import media
# import fresh_tomatoes file which gives output as a web age
import fresh_tomatoes

# print the movie title, show poster and trailer.
yeh_jawani_hai_diwani = media.Movie("Yeh jawaani hai deewani",
                                    "https://upload.wikimedia.org/wikipedia/en/1/15/Yeh_jawani_hai_deewani.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=Rbp2XUSeUNE")  # noqa
# print the movie title, show poster and trailer
sanju = media.Movie("Sanju",
                    "https://upload.wikimedia.org/wikipedia/en/e/e5/Sanju_-_Theatrical_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=1J76wN0TPI4")

# print the movie title, show poster and trailer.
dangal = media.Movie("Dangal",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

# print the movie title, show poster and trailer.
bajrangi_bhaijaan = media.Movie("Bajrangi Bhaijaan",
                                "https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=4nwAra0mz_Q")

# print the movie title, show poster and trailer.
bajirao_mastani = media.Movie("Bajirao Mastani",
                              "https://upload.wikimedia.org/wikipedia/en/c/c0/Bajirao_Mastani_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=eHOc-4D7MjY")
# print the movie title, show poster and trailer.
welcome_back = media.Movie("Welcome Back",
                           "https://upload.wikimedia.org/wikipedia/en/f/f8/Welcome_Back_First_Look_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=_EPPfT7qkKM")

# give the input to fresh_tomatoes file as a list of movies.
movies = [yeh_jawani_hai_diwani, sanju, dangal, bajrangi_bhaijaan, bajirao_mastani, welcome_back]  # noqa
fresh_tomatoes.open_movies_page(movies)
