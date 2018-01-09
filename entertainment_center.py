import media
import fresh_tomatoes

# Creates an object that contains: movie name, storyline, poster image, youtube
# trailer, cast, genre and duration
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels"
                         " about the true nature of his reality and his role"
                         " in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5"
                         "BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2l"
                         "tYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,6"
                         "65,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                         "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                         "Action, Sci-fi",
                         "2h 16min")

the_matrix_reloaded = media.Movie("The Matrix Reloaded",
                                  "Neo and the rebel leaders estimate that"
                                  " they have 72 hours until 250,000 probes"
                                  " discover Zion and destroy it and its"
                                  " inhabitants."
                                  " During this, Neo must decide how he can"
                                  " save Trinity from a dark fate in his"
                                  " dreams.",
                                  "https://images-na.ssl-images-amazon.com/"
                                  "images/M/MV5BYzM3OGVkMjMtNDk3NS00NDk5LWJ"
                                  "jZjUtYTVkZTIyNmQxNDMxXkEyXkFqcGdeQXVyNTA"
                                  "yODkwOQ@@._V1_SY1000_CR0,0,684,1000_AL_."
                                  "jpg",
                                  "https://www.youtube.com/watch?v=zmYE3tg26"
                                  "Qc",
                                  "Keanu Reeves, Laurence Fishburne, Carrie-"
                                  "Anne Moss",
                                  "Action, Sci-fi",
                                  "2h 18min")

the_matrix_revolutions = media.Movie("The Matrix Revolutions",
                                     "The human city of Zion defends itself"
                                     " against the massive invasion of the"
                                     " machines as Neo fights to end the war"
                                     " at another front while also opposing"
                                     " the rogue Agent Smith.",
                                     "https://images-na.ssl-images-amazon.com"
                                     "/images/M/MV5BNzNlZTZjMDctZjYwNi00NzljL"
                                     "WIwN2QtZWZmYmJiYzQ0MTk2XkEyXkFqcGdeQXVy"
                                     "NTAyODkwOQ@@._V1_SY1000_CR0,0,676,1000_"
                                     "AL_.jpg",
                                     "https://www.youtube.com/watch?v=psNlHck"
                                     "YlVs",
                                     "Keanu Reeves, Laurence Fishburne, Carri"
                                     "e-Anne Moss",
                                     "Action, Sci-fi",
                                     "2h 9min")

lord_of_the_rings_one = media.Movie("The Lord of the Rings: The Fellowship of"
                                    " the Ring",
                                    "A meek Hobbit from the Shire and eight"
                                    " companions set out on a journey to"
                                    " destroy the powerful One Ring and save"
                                    " Middle-earth from the Dark Lord Sauron.",
                                    "https://images-na.ssl-images-amazon.com/"
                                    "images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI"
                                    "0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDU"
                                    "zOTQ5MjY@._V1_SY999_CR0,0,673,999_AL_."
                                    "jpg",
                                    "https://www.youtube.com/watch?v=z_WZxJ"
                                    "pHzEE",
                                    "Elijah Wood, Ian McKellen, Orlando Bloom",
                                    "Adventure, Drama, Fantasy",
                                    "2h 58min")

lord_of_the_rings_two = media.Movie("The Lord of the Rings: The Two Towers",
                                    "While Frodo and Sam edge closer to Mordor"
                                    " with the help of the shifty Gollum, the"
                                    " divided fellowship makes a stand against"
                                    " Sauron's new ally, Saruman, and his"
                                    " hordes of Isengard.",
                                    "https://images-na.ssl-images-amazon.com"
                                    "/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExL"
                                    "TkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVy"
                                    "NjU0OTQ0OTY@._V1_.jpg",
                                    "https://www.youtube.com/watch?v=cvCktPU"
                                    "wkW0",
                                    "Elijah Wood, Ian McKellen, Orlando Bloom",
                                    "Adventure, Drama, Fantasy",
                                    "2h 59min")

lord_of_the_rings_three = media.Movie("The Lord of the Rings: The Return of"
                                      " the King",
                                      "Gandalf and Aragorn lead the World of"
                                      " Men against Sauron's army to draw his"
                                      " gaze from Frodo and Sam as they"
                                      " approach Mount Doom with the One"
                                      " Ring.",
                                      "https://images-na.ssl-images-amazon."
                                      "com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00N"
                                      "WIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGd"
                                      "eQXVyNDUyOTg3Njg@._V1_SY1000_SX668_AL_"
                                      ".jpg",
                                      "https://www.youtube.com/watch?v=KOQSQa"
                                      "GgJxs",
                                      "Elijah Wood, Ian McKellen, Orlando Blo"
                                      "om",
                                      "Adventure, Drama, Fantasy",
                                      "3h 21min")

# The movie objects has to be placed in an array
# to be called by the method open_movie_page()
movies = [the_matrix, the_matrix_reloaded, the_matrix_revolutions,
          lord_of_the_rings_one, lord_of_the_rings_two,
          lord_of_the_rings_three]

# Creates and starts the trailer movie page
fresh_tomatoes.open_movies_page(movies)
