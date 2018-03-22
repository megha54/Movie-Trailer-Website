import webbrowser


class Movie():
    # a class that represents a movie
    __name__ = "Movie House"
    # Attributes are:title,storyline,poster_image and trailer

    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # it opens a trailer in the web browser
        webbrowser.open(self.trailer_youtube_url)
