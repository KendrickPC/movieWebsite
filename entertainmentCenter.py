import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)
# print(toy_story.storyline)

spirited_away = media.Movie("Spirited Away",
						"During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.", 
						"http://vignette2.wikia.nocookie.net/studio-ghibli/images/6/64/Spirited_Away_%28Svensk_DVD%29.jpg/revision/latest?cb=20140116135517",
						"https://www.youtube.com/watch?v=ByXuk9QqQkk"
	)
# spirited_away.show_trailer()

howls_moving_castle = media.Movie("Howl's Moving Castle",
						"When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.",
						"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-1uvi0ti_281fe89f.jpeg?region=0%2C0%2C1000%2C1363",
						"https://www.youtube.com/watch?v=iwROgK94zcM"
	)
# howls_moving_castle.show_trailer()

princess_mononoke = media.Movie("Princess Mononoke",
						"On a journey to find the cure for a Tatarigami's curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.",
						"https://vignette4.wikia.nocookie.net/toonami/images/c/c6/Princess_Mononoke.jpg/revision/latest?cb=20130829185423",
						"https://www.youtube.com/watch?v=4OiMOHRDs14"
	)

my_neighbor_totoro = media.Movie("My Neighbor Totoro",
						"When two girls move to the country to be near their ailing mother, they have adventures with the wondrous forest spirits who live nearby.",
						"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-1uvi0ti_281fe89f.jpeg?region=0%2C0%2C1000%2C1363",
						"https://www.youtube.com/watch?v=B6B_nuHksvs"
	)

grave_of_the_fireflies = media.Movie("Grave of the Fireflies",
						"A young boy and his little sister struggle to survive in Japan during World War II.",
						"http://static.rogerebert.com/uploads/movie/movie_poster/grave-of-the-fireflies-1988/large_bwVhmPpydv8P7mWfrmL3XVw0MV5.jpg",
						"https://www.youtube.com/watch?v=4vPeTSRd580"
	)

movies = [toy_story, spirited_away, howls_moving_castle, princess_mononoke, my_neighbor_totoro, grave_of_the_fireflies]
fresh_tomatoes.open_movies_page(movies)