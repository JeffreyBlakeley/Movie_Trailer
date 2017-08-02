import fresh_tomatoes
import media


def main():
    intersellar = media.Movie(
        "Intersellar",
        "A team of explorers travel through a wormhole in"
        "space in an attempt to ensure humanity's survival.",
        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=0vxOhd4qlnA")

    arrival = media.Movie(
        "Arrival",
        "When twelve mysterious spacecraft appear around the world,"
        " linguistics professor Louise Banks is tasked with interpreting the"
        " language of the apparent alien visitors.",
        "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

    the_martian = media.Movie(
        "The Martian",
        "A man is stuck on Mars",
        "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=lQqhfq87FgY")

    rogue_one = media.Movie(
        "Rogue One: A Star Wars Story",
        "The Rebel Alliance makes a risky move to steal the plans for the"
        " Death Star, setting up the epic saga to follow.",
        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # NOQA
        "https://www.youtube.com/watch?v=frdj1zb9sMY")

    # Stores the movie objects into a list
    movies = [intersellar, arrival, the_martian, rogue_one]
    # This opens the website
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
