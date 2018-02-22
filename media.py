import webbrowser


# movie class defined below
class Movie():
    """ Defining Movie Class with attributes defining the movie object """
    # defining constructor for Movie class
    def __init__(this, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        """ This is constructor which will take argument and create object """
        this.title = movie_title
        this.storyline = movie_storyline
        this.poster_image_url = poster_image_url
        this.trailer_youtube_url = trailer_youtube_url

    # this function shows youtube trailer of listed movies.
    def showTrailer(this):
        """ This is showTrailer function and it will show movies tailer """
        webbrowser.open(this.trailer_youtube)
