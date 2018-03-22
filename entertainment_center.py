# it stores the details of the movies and displays it on the website.
import fresh_tomatoes
import media

# Creating various instances for the class movie
inception = media.Movie(
                    "INCEPTION",
                    """A thief, who steals corporate secrets through the use of
                    dream-sharing technology, is given the inverse task of
                    planting an idea into the mind of a CEO.""",
                    "inception.jpg",
                    "https://www.youtube.com/watch?v=d3A3-zSOBT4")


gravity = media.Movie(
               "GRAVITY",
               """Two astronauts work together to survive after an accident
               which leaves them stranded in space.""",
               "gravity.jpg",
               "https://www.youtube.com/watch?v=OiTiKOy59o4")

the_social_networking = media.Movie(
                         "THE SOCIAL NETWORKING",
                         """Harvard student Mark Zuckerberg creates the social
                         networking site that would become known as Facebook,
                         but is later sued by two brothers who claimed he stole
                         their idea, and the co-founder who was later squeezed
                         out of the business.""",
                         "social.jpg",
                         "https://www.youtube.com/watch?v=lB95KLmpLR4")

the_theory_of_everthing = media.Movie(
                           "THE THEORY OF EVERYTHING",
                           """Stephen Hawking, an excellent astrophysics student
                           working on his research, learns that he suffers from
                           motor neurone disease and has around two years to
                           live.""",
                           "theory.jpg",
                           "https://www.youtube.com/watch?v=Salz7uGp72c")

the_pursuit_happiness = media.Movie(
                           "THE PURSUIT OF HAPPINESS",
                           """Chris Gardner takes up an unpaid internship in a
                           brokerage firm after he loses his life's earnings
                           selling a product he invested in.His wife leaves him
                            and he is left with the custody of his son""",
                           "happiness.jpg",
                           "https://www.youtube.com/watch?v=DMOBlEcRuw8")

bolt = media.Movie(
        "BOLT",
        """Bolt is a dog who stars in a superhit television show in which he
        possesses superpowers. He believes his powers are for real and embarks
        on a purposeful mission.""",
        "bolt.jpg",
        "https://www.youtube.com/watch?v=IBsg00NnzGg")

movies = [
    inception, gravity, the_social_networking, the_theory_of_everthing,
    the_pursuit_happiness, bolt]

# using the python fresh tomatoes for opening our website.
fresh_tomatoes.open_movies_page(movies)
