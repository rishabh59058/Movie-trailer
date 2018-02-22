import media
import fresh_tomatoes

# Avtar movie object
a = ("Avatar, marketed as James Cameron's Avatar, is a 2009 American[7][8] "
     "epic science fiction film directed, written, "
     "produced, and co-edited by James Cameron, and starring Sam Worthington,"
     "Zoe Saldana, Stephen Lang, Michelle Rodriguez, and Sigourney Weaver.")
Avatar = media.Movie("Avatar",
                     a,
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Dunkirk movie object
b = ("Dunkirk is a 2017 war film written, directed, and co-produced by "
     "Christopher Nolan that depicts the Dunkirk evacuation of World War II. "
     "Its ensemble cast includes Fionn Whitehead, Tom Glynn-Carney, "
     "Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry "
     "Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, and Tom Hardy.")
Dunkirk = media.Movie("Dunkirk",
                      b,
                      ("https://upload.wikimedia.org/wikipedia/en/1/15/Dunki"
                       "rk_Film_poster.jpg"),
                      "https://www.youtube.com/watch?v=XRtZUkAR2u4")

# Hunger Games movie object
c = ("The Hunger Games is a 2012 American post-apocalyptic science fiction "
     "action adventure film directed by Gary Ross and based on the novel "
     "of the same name by Suzanne Collins.")
HungerGame = media.Movie("The Hunger Games",
                         c,
                         ("https://upload.wikimedia.org/wikipedia/commons/"
                          "thumb/7/79/The_hunger_games.svg/313px-The_hunger"
                          "_games.svg.png"),
                         "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Gravity movie object
d = ("Gravity, or gravitation, is a natural phenomenon by which all things "
     "with mass are brought toward (or gravitate toward) one another, "
     "including objects ranging from atoms and photons, to planets and st"
     "ars. Since energy and mass are equivalent, all forms of energy "
     "(including light) cause "
     "gravitation and are under the influence of it.")
Gravity = media.Movie("Gravity",
                      d,
                      ("https://upload.wikimedia.org/wikipedia/en/f/f6/"
                       "Gravity_Poster.jpg"),
                      "https://www.youtube.com/watch?v=ufsrgE0BYf0")

# John Carter movie object
e = ("John Carter is a 2012 American science fiction action film directed "
     "by Andrew Stanton from a screenplay written by Stanton, Mark Andrews, "
     "and Michael Chabon.")
JohnCarter = media.Movie("John Carter",
                         e,
                         ("https://upload.wikimedia.org/wikipedia/en/a/aa/"
                          "John_carter_poster.jpg"),
                         "https://www.youtube.com/watch?v=nlvYKl1fjBI")

# 3 Idiots movie object
f = ("3 Idiots is a 2009 Indian coming-of-age comedy-drama film, directed "
     "and written by Rajkumar Hirani, and produced by Vidhu Vinod Chopra, "
     "with screenplay by Abhijat "
     "Joshi, inspired by the novel Five Point Someone by Chetan Bhagat.")
ThreeIdiots = media.Movie("3 Idiots",
                          f,
                          ("https://upload.wikimedia.org/wikipedia/en/d/df/"
                           "3_idiots_poster.jpg"),
                          "https://www.youtube.com/watch?v=K0eDlFX9GMc")

# Phir Hera Pheri movie object
z = ("Hera Pheri ended with the trio of Raju (Akshay Kumar),Shyam "
     "Sunil Shetty, and Baburao Ganapatrao Apte ( Paresh Rawal ) rich and '\'"
     "rolling in money.")
PhirHeraPheri = media.Movie("Phir Hera Pheri",
                            z,
                            ("https://upload.wikimedia.org/wikipedia/en/thum"
                             "b/3/3a/Still-phir-hera-phir.jpg/220px-Still-"
                             "phir-hera-phir.jpg"),
                            "https://www.youtube.com/watch?v=1rJQQCZcq2s")
# creates an array of movies
movies = ([Avatar, Dunkirk, HungerGame, Gravity, JohnCarter, ThreeIdiots,
          PhirHeraPheri])
# send movies array to create_movie_tiles_content function in fresh_tomatoes
fresh_tomatoes.create_movie_tiles_content(movies)
# send movies array to open_movies_page function in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
