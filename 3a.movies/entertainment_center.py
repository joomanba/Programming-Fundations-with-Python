import media

toy_story = media.Move("Toy Story",
                       "A story of a boy and his toys that comes to life",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story_jpg",
                       "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Move("Avatar",
                    "A marin on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)
avatar.show_trailer()
