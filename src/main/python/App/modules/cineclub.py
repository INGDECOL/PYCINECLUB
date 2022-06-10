from App.models.model import Db, get_data


def get_movies():
    movies_title = get_data()
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:

    def __init__(self, movie_title):
        self.movie_title = movie_title.title()
        self.db = Db()

    def __str__(self):
        return self.movie_title

    def add_movies(self):
        movies = get_data()
        if self.movie_title not in movies:
            movies.append(self.movie_title)
            self.db.write(movies)
            return True
        return False

    def remove_movie(self):
        # movies = list(filter(lambda mv: mv != movie, self.db.get_data()))
        movies = get_data()
        if self.movie_title in movies:
            movies.remove(self.movie_title)
            self.db.write(movies)


if __name__ == '__main__':
    movie = Movie("harry hessian")
    movie.add_movies()
    movie1 = Movie("harry potter")
    movie1.add_movies()
    movie2 = Movie("Barry potter1")
    movie2.add_movies()
    movie3 = Movie("Barry potter2")
    movie3.add_movies()
    movie4 = Movie("Barry potter3 HOUSMAN&&")
    movie4.add_movies()
    movie.remove_movie()
