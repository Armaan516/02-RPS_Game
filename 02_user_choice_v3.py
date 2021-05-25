# Version 3 - checks response is in a given list


# Functions go here
def choice_checker(question, valid_list, error):

  valid = False
  while not valid:

    # Ask user for choice and put it in lowercase
    response = input(question).lower() 

    # Loops through the list and if the response is in the list (or the first letter of the response is a item in the list), the full name of the item is returned

    for item in valid_list:
      if response == item[0] or response == item:
        return item

    # Error if item is not in list
    print(error)
    print()



# Main routine goes here


# List for checking responses
rps_list = ["rock", "paper", "scissors", "quit"]

# Looping for testing purposes
user_choice = ""
while user_choice != "quit":

  # Ask user for choice and check it's valid
  user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list, "Please choose rock, paper or scissors (or type 'quit' or 'q' to quit the game)")

  # Print out choice for comparison purposes
  print("You chose {}".format(user_choice))