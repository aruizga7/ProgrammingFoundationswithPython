import webbrowser

# Creation of the class movie
class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    #Creation of the constructor Movie, that contains 4 instance variables
    def __init__ (self, movie_title,movie_storyline, poster_image,
                trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Intance method to display the Movie trailer on your Web-browser      
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
