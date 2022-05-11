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
                print("Please enter a valid option!")

        except ValueError:
            print("Please enter a valid option!")

    return choice


# Movie Select Function
# Paramaters: dictionary
def movie_select(dictionary):
    pass
# Continues to loop until a movie is selected
# Asks user for an input
# Use try and except to make sure the input is a number
# Check if input is too short (less than 1 characters)
# Check if the input is an option, return it
# Otherwise print error message

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
# Parameters: dictionary, movie_selection
def edit_movie_length(dictionary, movie_selection):
    pass
# Assign movie info variables for updating dictionary
# Asks user for input
# Use try and except to make sure the input is a number
# Check if input is too short (less than 1 characters)
# Check if input is less than or equal to 0
# Check if input is more than 299
# Check if input is not equal to original length
# If true update dictionary
# Otherwise print error message

# Add Movie Function
# Parameters: dictionary
def add_movie(dictionary):
    pass
# Keep looping until input is allowed
# Ask user for movie_name input
# Check if input is too short (less than 1 characters)
# If not end loop
# Otherwise print error message
# Keep looping until input is allowed
# Ask user for movie_director input
# Check if input is too short (less than 1 characters)
# If not end loop
# Otherwise print error message
# Keep looping until input is allowed
# Ask user for mins input
# Use try and except to make sure the input is a number
# Check if input is too short (less than 1 characters)
# Check if input is less than or equal to 0
# Check if input is more than 299
# Check if input is not equal to original length
# If true end loop
# Otherwise print error message
# Use the length of the dictionary to determine
# the next movie id
# Add to dictionary

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
        if menu_option == 0:
            # If the menu_option was 0 end loop
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
            print("Please enter a valid option")
