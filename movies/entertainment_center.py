import media
import fresh_tomatoes

#Addid movies to our catalog using the Class Movie
toy_story = media.Movie ("Toy Story",
                         "A story of a bout and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie ("Avatar",
                         "A marine on an alien planet",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=5PSNL1qE6VY")
titanic = media.Movie ("Titanic",
                         "Romantic movie about the distaster of the RMS Titanic",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg",
                         "https://www.youtube.com/watch?v=5d9ILag7mRA")
ratatouille = media.Movie ("Ratatouille",
                         "A rat is a chef in Paris",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=niD-jahFURU")
school_of_rock = media.Movie ("School of Rock",
                         "Using rock music to learn",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                         "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
star_wars = media.Movie ("Star Wars Episove IV",
                         "First release in the Star Wars franchise",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                         "https://www.youtube.com/watch?v=9gvqpFbRKtQ")
#Creating an array with all the movies we want to add to our website                         
movies = [toy_story, avatar, titanic, ratatouille, school_of_rock, star_wars]
#Calling the script that will create the HTML site based on our 'movies' array

fresh_tomatoes.open_movies_page(movies)
#print(titanic.storyline)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
