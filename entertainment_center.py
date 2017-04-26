import media
import fresh_tomatoes

# instantiation of six movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys comign to life",
                        "https://upload.wikimedia.org/wikipedia/en"
                        "/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story of Avatars",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0"
                     "/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

breakfast_at_tiffanys = media.Movie("Breakfast at Tiffany's",
                                    "A film with Audrey Hepburn",
                                    "http://www.nordicposters.com/p2"
                                    "/breakfast_at_tiffanys_61_2_poster.jpg",
                                    "https://www.youtube.com"
                                    "/watch?v=urQVzgEO_w8")

titanic = media.Movie("Titanic",
                      "About a sinking ship in 1912",
                      "https://upload.wikimedia.org/wikipedia/en/2/22"
                      "/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=ZQ6klONCq4s")

tarzan = media.Movie("Tarzan",
                     "About a man brought up by gorillas",
                     "https://s-media-cache-ak0.pinimg.com/236x/da/c4/06"
                     "/dac406f22c967aa58c22196ac031a8fa.jpg",
                     "https://www.youtube.com/watch?v=lfciC33t3M0")

frozen = media.Movie("Frozen",
                     "About a girl who has freezing powers",
                     "https://upload.wikimedia.org/wikipedia/en/0/05"
                     "/Frozen_(2013_film)_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

# storing all movies in array
movies = [toy_story, avatar, breakfast_at_tiffanys, titanic, tarzan, frozen]
# passing all movies to create static html
fresh_tomatoes.open_movies_page(movies)
