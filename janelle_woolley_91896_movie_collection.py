##
# janelle_woolley_91896_movie_collection.py
# Allows user to Add, Edit, and Print Movie's and Movie length
#
# Author: Janelle Woolley
# 09/05/22 Version_1


# Menu Function
def get_menu_option():
    """
    Ask user to select an option
    Returns selected option
    """
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
            print("\nPlease enter your option as a number e.g. 2\n")

    return choice


# Movie Select Function
def movie_select(dictionary):
    """
    Ask user to select a key then returns it
    """
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
            print("\nPlease enter your option as a number e.g. 2")

    return movie_selected


# Mins to Hours Function
def mins_to_hours(dictionary):
    """
    Converts runtime in minutes to runtime in hours & minutes
    Adds to new dictionary and returns new dictionary
    """
    AMOUNT_MINS_IN_HOURS = 60
    ADD_HOUR = 1
    hours_dictionary = {}

    # Loops through the dictionary
    for key in dictionary.keys():
        movie_info = dictionary[key]
        mins_runtime = movie_info["Run Time"]

        # Will keep looping until mins are under 60
        getting_hours = True
        hours_count = 0
        while getting_hours:
            if mins_runtime > 60:
                # Is taking 60 away from the minutes and is adding
                # to the hour count each time it loops
                mins_runtime = mins_runtime - AMOUNT_MINS_IN_HOURS
                hours_count = hours_count + ADD_HOUR
            else:
                getting_hours = False

        # Takes hours and mins and puts them in string
        runtime_string = "{}h {}m".format(hours_count, mins_runtime)

        # Assigns variables to movie info for adding to new dictionary
        movie = movie_info["Title"]
        director = movie_info["Director"]

        # Add to new dictionary
        hours_dictionary.update({key: {"Title": movie,
                                       "Director": director,
                                       "Run Time": runtime_string}})

    return hours_dictionary


# Print Functions
def print_functions(menu_option, movie_selection, dictionary):
    """
    Prints movie info for showing options, printing movie length
    and printing all movie info
    """
    # Checks if the print function is being called to show options
    if movie_selection == "Show Options":
        # Loops through dictionary printing movie name and key
        for key in dictionary.keys():
            movie_info = dictionary[key]
            movie = movie_info["Title"]
            print("{}\t{}".format(key, movie))

    # Checks if the print function is being called for option 3
    # and isn't to show options
    elif menu_option == 3 and movie_selection != "Show Options":
        # Prints name and runtime
        movie_info = dictionary[movie_selection]
        movie = movie_info["Title"]
        runtime = movie_info["Run Time"]
        print("\n{}\t{}\t{}".format(movie_selection, movie, runtime))

    # Checks if the print function is being called for option 4
    elif menu_option == 4:
        # loops through dictionary printing out
        # movie name, director and runtime
        for key in dictionary.keys():
            movie_info = dictionary[key]
            movie = movie_info["Title"]
            director = movie_info["Director"]
            runtime = movie_info["Run Time"]
            print("{}\t{}\t{}\t{}".format(key, movie,
                                          director, runtime))

    else:
        print("Sorry Something Has Gone Wrong Try Again Later \(*~*)/")


# Edit Movie Length Function
def edit_movie_length(dictionary, key):
    """
    Asks user for a new run time then updates dictionary
    """
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
            # Check if the new runtime is equal to the old runtime
            elif new_runtime == runtime:
                print("\nThe movie already has that runtime"
                      " please enter a new runtime")
            # Input meets all the requirements so end loop
            else:
                getting_runtime = False

        except ValueError:
            print("\nPlease enter the time as a number e.g. 60")

    # Update dictionary
    dictionary.update({key: {"Title": movie,
                             "Director": director,
                             "Run Time": new_runtime}})


# Add Movie Function
def add_movie(dictionary):
    """
    Ask user for movie name, director, and length
    Then adds them to the dictionary
    """
    MIN_MOVIE_NAME_LENGTH = MIN_RUNTIME = ADD_TO_GET_KEY = 1
    MIN_DIRECTOR_NAME_LENGTH = 5
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

    # Does the same as above but for getting director name
    getting_director = True
    while getting_director:
        director = input("Please enter the name of the director: ")
        if len(director) > MIN_DIRECTOR_NAME_LENGTH:
            getting_director = False
        else:
            print("\nPlease enter a valid name!")

    # Keeps looping until input is allowed
    getting_runtime = True
    while getting_runtime:
        # Use try and except to make sure the input is a number
        try:
            runtime = int(input("Please enter the movie's"
                                " runtime in minutes: "))

            # Check is runtime is between the min and max
            if runtime in range(MIN_RUNTIME, MAX_RUNTIME):
                getting_runtime = False
            # Otherwise print error message
            else:
                print("\nPlease enter a time between 1 and 299 mins")

        except ValueError:
            print("\nPlease enter the time as a number e.g. 60")

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
            print_functions(menu_option, "Show Options", movies)
            movie_selection = movie_select(movies)
            edit_movie_length(movies, movie_selection)
        # If menu_option is 3 call functions to print movie length
        elif menu_option == 3:
            print_functions(menu_option, "Show Options", movies)
            movie_selection = movie_select(movies)
            movies_with_hours = mins_to_hours(movies)
            print_functions(menu_option, movie_selection,
                            movies_with_hours)
        # If menu_option is 4 call functions to print movies
        elif menu_option == 4:
            movies_with_hours = mins_to_hours(movies)
            print_functions(menu_option, "N/A",
                            movies_with_hours)
        # Otherwise print error message
        else:
            print("\nPlease enter a valid option!\n")
