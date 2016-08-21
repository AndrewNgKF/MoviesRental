from movie import Movie
from user import User


user = User.load_from_file('Andrew.txt')

print(user.name)
print(user.movies)