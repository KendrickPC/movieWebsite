import media

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)
print(toy_story.storyline)

spirited_away = media.Movie("Spirited Away",
						"During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.", 
						"http://vignette2.wikia.nocookie.net/studio-ghibli/images/6/64/Spirited_Away_%28Svensk_DVD%29.jpg/revision/latest?cb=20140116135517",
						"https://www.youtube.com/watch?v=ByXuk9QqQkk"
	)

print(spirited_away.trailer_youtube_url)