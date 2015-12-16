"""This module only contains the Movie class"""

import webbrowser


class Movie():
    """A structure that stores all the basic information of a movie"""
        
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube, lead_actors, imdb_rating):
        """"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube
        self.lead_actors = lead_actors
        self.imdb_rating = imdb_rating
			
    def show_trailer(self):
        """Opens webbrowser to the trailer url"""       
        webbrowser.open(self.trailer_youtube_url)

    def show_actors(self):
        """Prints all the actors as a comma separated list"""
        print(', '.join(self.actors))
