##
# janelle_woolley_91896_movie_collection.py
# Allows user to Add, Edit, and Print, Movie's and Movie length
#
# Author: Janelle Woolley
# 09/05/22 Version_1

# Add movie (Title, director, length): Mins
# Edit movie length: Mins
# Print movie length: Hours + Mins
# Print movie (Title, director, length): Hours + Mins
# Quit

# Max length of movie is 299 Mins / 4:59 Hours

# Menu Function
def get_menu_option():
    MINIMUM_LENGTH = 1
    choices = [1, 2, 3, 4, 0]
    # Contiues to loop until an option is chosen
    getting_choice = True
    while getting_choice:
        # Use try and except to make sure the input is a number
        try:        
            # Ask user for input
            choice = int(input("\nPlease chose an option\n"
                               "1: Add Movie\n"
                               "2: Edit Movie Length\n"
                               "3: Print Movie Length\n"
                               "4: Print Movies\n"
                               "0: Quit\n"))

            # Check if the input is an option, if so end loop
            if choice in choices:
                getting_choice = False

            # Otherwise print error message
            else:
                print("\nPlease enter a valid option!\n")

        except ValueError:
            print("\nPlease enter a valid option!\n")

    return choice


# Movie Select Function
def movie_select(dictionary):
    # Continues to loop until a movie is selected
    getting_movie_selection = True
    while getting_movie_selection:
        # Use try and except to make sure the input is a number
        try:
            # Asks user for an input
            movie_selected = int(input("Please enter the key for the movie "
                                       "you would like to select: "))
            
            # Check if the input is an option, if so end loop
            if movie_selected in dictionary:
                getting_movie_selection = False

            # Otherwise print error message
            else:
                print("\nPlease enter a valid option!")

        except ValueError:
            print("\nPlease enter a valid option!")

    return movie_selected


# Mins to Hours Function
# Parameters: dictionary
def mins_to_hours(dictionary):
    pass
# MINS_TO_HOURS = 60
# Loops through the dictionary
# Converts mins to hours
# hours = mins * MINS_TO_HOURS
# Assigns variables to movie info for adding to new hours_dictionary
# Add to new hours_dictionary
# Return hours_dictionary

# Print Functions
# FUNCTION FOR:
# selection for edit(name, mins)
# selection for print solo(name)
# print solo(name, hours + mins)
# print all(name, director?, hours + mins)
# FUNCTION NEEDS:
# menu_option, dictionary
# menu_option, dictionary
# menu_option, movie_selection, hours_dictionary
# menu_option, hours_dictionary
def print_functions(menu_option, movie_selection,
                    dictionary, hours_dictionary):
    pass

# Print Movie Function
# Parameters: hours_dictionary
def print_movies(hours_dictionary):
    pass
# Loops through the dictionary
# Assigns variables to the movie info for printing
# Prints out movie info

# Print Movie Length Function
# Parameters: hours_dictionary, movie_selection
def print_movie_length(hours_dictionary, movie_selection):
    pass
# Assigns variable to the movie length for the movie selection
# Prints out movie_length


# Edit Movie Length Function
def edit_movie_length(dictionary, key):
    MIN_RUNTIME = 1
    MAX_RUNTIME = 300

    # Assign movie info variables for updating dictionary
    movie_info = dictionary[key]
    movie = movie_info["Title"]
    director = movie_info["Director"]
    runtime = movie_info["Run Time"]

    # Keep looping until input meets criteria
    getting_runtime = True
    while getting_runtime:
        # Use try and except to make sure the input is a number
        try:
            # Asks user for input
            new_runtime = int(input("Please enter the movie's"
                                " runtime in minutes: "))

            # Check is runtime is between the min and max
            if new_runtime not in range(MIN_RUNTIME, MAX_RUNTIME):
                print("\nPlease enter a time between 1 and 299 mins")

            # Check if input is not equal to original length
            elif new_runtime != runtime:
                getting_runtime = False

            # Otherwise print error message
            else:
                print("\nPlease enter a time between 1 and 299 mins")
            
        except ValueError:
            print("\nPlease enter the time in minutes")

    # Update dictionary
    dictionary.update({key: {"Title": movie,
                             "Director": director,
                             "Run Time": new_runtime}})


# Add Movie Function
def add_movie(dictionary):
    MIN_MOVIE_NAME_LENGTH = MIN_RUNTIME = ADD_TO_GET_KEY = 1
    MIN_DIRECTOR_NAME_LENGTH = 3
    MAX_RUNTIME = 300
    # Keep looping until input is allowed
    getting_movie_name = True
    while getting_movie_name:
        # Ask user for movie_name input
        movie_name = input("Please enter the name of the movie: ")
        # Check if input is too short (less than 1 characters)
        if len(movie_name) > MIN_MOVIE_NAME_LENGTH:
            # If not end loop
            getting_movie_name = False
        # Otherwise print error message
        else:
            print("\nPlease enter a movie name!")

    getting_director = True
    while getting_director:
        director = input("Please enter the name of the director: ")
        if len(director) > MIN_DIRECTOR_NAME_LENGTH:
            getting_director = False
        else:
            print("\nPlease enter a valid name!")

    getting_runtime = True
    while getting_runtime:
        # Use try and except to make sure the input is a number
        try:
            runtime = int(input("Please enter the movie's"
                                " runtime in minutes: "))

            # Check is runtime is between the min and max
            if runtime in range(MIN_RUNTIME, MAX_RUNTIME):
                getting_runtime = False
            else:
                print("\nPlease enter a time between 1 and 299 mins")
            
        except ValueError:
            print("\nPlease enter the time in minutes")

    # Use the length of the dictionary to determine the movie key
    key = len(dictionary) + ADD_TO_GET_KEY

    # Add to dictionary
    dictionary.update({key: {"Title": movie_name.title(),
                             "Director": director.title(),
                             "Run Time": runtime}})


if __name__ == "__main__":
    movies = {1: {"Title": "We Can Be Heroes",
                  "Director": "Robert Rodriguez",
                  "Run Time": 100},
              2: {"Title": "Enola Holmes",
                  "Director": "Harry Bradbeer",
                  "Run Time": 124},
              3: {"Title": "Feel the Beat",
                  "Director": "Elissa Down",
                  "Run Time": 110}}

    # Keeps looping so the menu will apear again
    # after an option is complete
    code_running = True
    while code_running:
        # Get a menu option by running function
        menu_option = get_menu_option()
        # If the menu_option was 0 end loop
        if menu_option == 0:
            code_running = False
        # If menu_option is 1 call functions to add a movie
        elif menu_option == 1:
            add_movie(movies)
        # If menu_option is 2 call functions to edit movie length
        elif menu_option == 2:
            movie_selection = movie_select(movies)
            edit_movie_length(movies, movie_selection)
        # If menu_option is 3 call functions to print movie length
        elif menu_option == 3:
            movie_selection = movie_select(movies)
            movies_with_hours = mins_to_hours(movies)
            print_movie_length(movies_with_hours, movie_selection)
        # If menu_option is 4 call functions to print movies
        elif menu_option == 4:
            movies_with_hours = mins_to_hours(movies)
            print_movies(movies_with_hours)
        # Otherwise print error message
        else:
            print("\nPlease enter a valid option!\n")
