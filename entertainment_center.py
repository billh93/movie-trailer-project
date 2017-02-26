import media
import fresh_tomatoes

'''
    We are creating 6 instances of movies that I like that contain the
    following information: Movie Title, Storyline, Poster Image and Youtube url

    With these instances we can populate our html page.
'''
great_gatsby = media.Movie("The Great Gatsby",
                           "A rich young man reconnects with his first love.",
                           "http://images.china.cn/attachement/jpg/site1002/"
                           "20130515/001ec94a271512fd88a014.jpg",
                           "https://www.youtube.com/watch?v=rARN6agiW7o")

iron_man_3 = media.Movie("Iron Man 3",
                         "Iron Man Finally Meets a Foe that causes him some"
                         " trouble.",
                         "https://s-media-cache-ak0.pinimg.com/736x/6a/15/87/"
                         "6a15871e9a1bc03bd763909bd8100a80.jpg",
                         "https://www.youtube.com/watch?v=2CzoSeClcw0")

wolf_of_wall_street = media.Movie("The Wolf Of Wall Street",
                                  "Jordan Belfort builds an empire by defraud"
                                  "ing wealthy investors out of millions.",
                                  "https://images-na.ssl-images-amazon.com/"
                                  "images/I/71--vKV8gVL._AC_UL320_SR214,"
                                  "320_.jpg",
                                  "https://www.youtube.com/watch?v=iszwuX1AK6A"
                                  "")

transformers = media.Movie("Transformers",
                           "The Autobots and Decepticons are at war over a "
                           "mystical artifact.",
                           "http://imedia.kenhhd.tv/xce8xh5dlwy9/ro-bot-dai-"
                           "chien-transformers-2007-b395ffc247.jpg",
                           "https://www.youtube.com/watch?v=KrUhwet0ngg")

spider_man_3 = media.Movie("Spiderman 3",
                           "Spider-Man suit turns black and takes control of"
                           " him.",
                           "https://upload.wikimedia.org/wikipedia/en/7/7a/"
                           "Spider-Man_3,_International_Poster.jpg",
                           "https://www.youtube.com/watch?v=PCmMLfXdURs")

the_social_network = media.Movie("The Social Network",
                                 "A story about how Mark Zuckerberg built "
                                 "Facebook.",
                                 "http://pic.pimg.tw/nikola1202/c82dbc44980b"
                                 "0a124a3914279c6312d3.jpg?v=1289124008",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

# This movies array contains our list of movies with their information
movies = [great_gatsby, iron_man_3, wolf_of_wall_street, transformers,
          spider_man_3, the_social_network]

# This code lets us see the list of movies we have written down on this file.
fresh_tomatoes.open_movies_page(movies)
