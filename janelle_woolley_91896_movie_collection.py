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
# Contiues to loop until an option is chosen
# Ask user for input
# Use try and except to make sure the input is a number
# Check if input is too short (less than 1 characters)
# Check if the input is an option, return it
# Otherwise print error message

# Movie Select Function
# Paramaters: dictionary
# Continues to loop until a movie is selected
# Asks user for an input
# Use try and except to make sure the input is a number
# Check if input is too short (less than 1 characters)
# Check if the input is an option, return it
# Otherwise print error message

# Mins to Hours Function
# Parameters: dictionary
# MINS_TO_HOURS = 60
# Loops through the dictionary
# Converts mins to hours
# hours = mins * MINS_TO_HOURS
# Assigns variables to movie info for adding to new hours_dictionary
# Add to new hours_dictionary
# Return hours_dictionary

# Print Movie Function
# Parameters: hours_dictionary
# Loops through the dictionary
# Assigns variables to the movie info for printing
# Prints out movie info

# Print Movie Length Function
# Parameters: hours_dictionary, movie_selection
# Assigns variable to the movie length for the movie selection
# Prints out movie_length

# Edit Movie Length Function
# Parameters: dictionary, movie_selection
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

# Keeps looping so the menu will apear again
# after an option is complete
# Get a menu option by running function
# If menu_option is 1 call functions to add a movie
# If menu_option is 2 call functions to edit movie length
# If menu_option is 3 call functions to print movie length
# If menu_option is 4 call functions to print movies
# If the menu_option was 0 end loop
# Otherwise print error message
