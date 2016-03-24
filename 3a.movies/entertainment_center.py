import media
import fresh_tomatoes

toy_story = media.Move("Toy Story",
                       "A story of a boy and his toys that comes to life",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Move("Avatar",
                    "A marin on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Move("School of Rock",
                            "Using rock music to learn",
                            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Move("Ratatouille",
                         "A rat is a chef in Paris",
                         "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Move("Midnight in Paris",
                               "Going back in time to meet authors",
                               "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                               "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Move("Hunger Games",
                          "A really real reality show",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)