# Movie Recommendation System 
 
# Getting user information
age = int(input("Please enter your age: "))
type_of_movie = input("What type of movie do you want to watch? (Animation, Action, Comedy, Horror): ")

# Recommending animation movies for everyone
if type_of_movie == "animation":
    print("You might like Toy Story or Finding Nemo.")

# Recommending action movies based on age
elif type_of_movie == "action" and age < 16:
    print("You might like The Avengers or Spider-Man.")
elif type_of_movie == "action" and age >= 16:
    print("You might like John Wick or Mad Max: Fury Road.")

# Recommending comedy movies based on age
elif type_of_movie == "comedy" and age < 13:
    print("You might like The LEGO Movie or Despicable Me.")
elif type_of_movie == "comedy" and age >= 13:
    print("You might like The Hangover, The Truman Show or Superbad.")

# Recommending horror movies based on age
elif type_of_movie == "horror" and age < 18:
    print("You are too young to watch horror movies.")
elif type_of_movie == "horror" and age >= 18:
    print("You might like The Conjuring or A Quiet Place.")

# Handling invalid movie type input
else:
    print("Sorry, we don't have recommendations for what you requested.")