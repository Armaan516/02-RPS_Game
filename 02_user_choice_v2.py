# Version 2 - error message included when calling function


# Functions go here
def choice_checker(question, error):

  valid = False
  while not valid:

    # Ask user for choice
    response = input(question).lower() 

    # Check for rock / paper / scissors
    if response == "rock" or response == "r":
      response = "rock"
      return response
    elif response == "paper" or response == "p":
      response = "paper"
      return response
    elif response == "scissors" or response == "s":
      response = "scissors"
      return response

    # Check for exit code
    elif response == "quit" or response == "q":
      response = "quit"
      return response

    else:
      print(error)


# Main routine goes here
user_choice = ""
while user_choice != "quit":

  # Ask user for choice and check it's valid
  user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", "Please choose rock, paper or scissors (or type 'quit' or 'q' to quit the game)")

  # Print out choice for comparison purposes
  print("You chose {}".format(user_choice))