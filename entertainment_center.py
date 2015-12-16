#!/usr/bin/python
"""This is the main executable module that contains the main function"""

import media
import fresh_tomatoes


def main():
    """
    This is the first function that is executed.  It constructs various movies
    using the Movie class found in media.  It then organizes all the movies
    into a list, and then shows them in a web page, using fresh tomatoes
    """

    shawshank_redemption = media.Movie(
        "The Shawshank Redemption", ("Two imprisoned men bond over a number of "
         "years, finding solace and eventual redemption through acts of common "
         "decency."), "http://goo.gl/vSx29c",
        "https://www.youtube.com/watch?v=evINraaYqxM", ["Tim Robbins",
         "Morgin Freeman", "Bob Gunton"], 9.3
    )

    dark_knight = media.Movie(
        "The Dark Knight", ("When the menace known as the Joker wreaks havoc "
         "and chaos on the people of Gotham, the caped crusader must come to "
         "terms with one of the greatest psychological tests of his ability to "
         "fight injustice."), "http://goo.gl/1MRMQe",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY", ["Christopher Bale",
         "Heath Ledger", "Aaron Eckhart"], 9.0
    )

    return_of_the_king = media.Movie(
        "The Lord of the Rings: The Return of the King", ("Gandalf and Aragorn "
         "lead the World of Men against Sauron's army to draw his gaze from "
         "Frodo and Sam as they approach Mount Doom with the One Ring."),
        "http://goo.gl/tLHu3K", "https://www.youtube.com/watch?v=7JgpXiMcmJk",
        ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"], 8.9
    )

    fight_club = media.Movie(
        "Fight Club", ("An insomniac office worker, looking for a way to "
         "change his life, crosses paths with a devil-may-care soap maker, "
         "forming an underground fight club that evolves into something much, "
         "much more..."), "http://goo.gl/G4gDR7",
        "https://www.youtube.com/watch?v=SUXWAEX2jlg", ["Brad Pitt",
         "Edward Norton", "Helena Bonham Carter"], 8.9
    )

    inception = media.Movie(
        "Inception", ("A thief who steals corporate secrets through use of "
         "dream-sharing technology is given the inverse task of planting an "
         "idea into the mind of a CEO."), "http://goo.gl/xUE3lN",
        "https://www.youtube.com/watch?v=8hP9D6kZseM", ["Leonardo DiCaprio",
         "Jospeh Gordon-Levitt", "Ellen Page"], 8.8
    )

    the_matrix = media.Movie(
        "The Matrix", ("A computer hacker learns from mysterious rebels about "
         "the true nature of his reality and his role in the war against its "
         "controllers."), "http://goo.gl/nUOX8T",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU", ["Keanu Reeves",
         "Laurence Fishburne", "Carrie-Anne Moss"], 8.7
    )

    movies = [shawshank_redemption, dark_knight, return_of_the_king,
              fight_club, inception, the_matrix]
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()

