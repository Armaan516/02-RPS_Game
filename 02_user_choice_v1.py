# Functions go here
def choice_checker(question):

  valid = False
  while not valid:

    # Ask user for choice
    response = input(question).lower() 

    if response == "rock" or response == "r":
      response = "rock"
      return response

    if response == "paper" or response == "p":
      response = "paper"
      return response

    if response == "scissors" or response == "s":
      response = "scissors"
      return response


# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

# Print out choice for comparison purposes
print("You chose {}".format(user_choice))