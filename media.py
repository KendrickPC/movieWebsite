# The webbrowser module provides a high-level interface to allow displaying
# Web-based documents to users. Under most circumstances, simply calling
# the open(), on line # 12, function from this module will do the right thing.
import webbrowser
# The constructor method is used here. Instance variables in class Movies():
#  have the following outputs: title, storyline, poster image, and trailer
# url.  The inputs are self (call itself first), movie title,
# movie storyline, poster image url, and trailer youtube url.

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image,
	trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
# The show trailer function calls the webrowser to open the video.
# The webrowser module is imported at the top of this page.
# Simply calling the "open" function will open the video in a popup viewer.
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
