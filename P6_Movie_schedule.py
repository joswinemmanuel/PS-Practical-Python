current_movies = {"movie 1" : "11.00 am", "movie 2" : "1:00 pm", "movie 3" : "5:00 pm"}

print("We're showing the following movies : ")
for i in current_movies:
    print(i)

print()

movie = input("What movie would you like showtime for ? : ")
showtime = current_movies.get(movie)

if(showtime == None):
    print("Requested movie is not playing")
else:
    print(f"{movie} is playing at {showtime}")


# We're showing the following movies : 
# movie 1
# movie 2
# movie 3

# What movie would you like showtime for ? : movie 2
# movie 2 is playing at 1:00 pm