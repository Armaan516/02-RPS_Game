import random

# Functions go here
def check_rounds(question, error):

  valid = False
  while True:
    response = input(question)
    
    # If infinite mode not chosen, check response is an iteger more than 0
    if response != "":
      try:
        response = int(response)

        # If response is too low, go back to the start of the loop
        if response < 1: 
          print(error)
          print()
          continue
      
      # If response is not an integer, go back to start of loop
      except ValueError:
        print(error)
        print()
        continue

    return response

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

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "quit"]


# Ask user if they have played before, if 'yes,' show instructions



# Ask user for # of rounds then loop
rounds_played = 0 

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds("How many rounds: ", "Please type either <enter> or an integer that is more than 0 ") 

end_game = "no"
while end_game == "no":
  
  # Start of Game Play Loop

  # Rounds Heading 
  print()
  if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played + 1)

  else:
    heading = "Round {} of Round {}".format(rounds_played + 1, rounds)

    if rounds_played == rounds - 1:
      end_game = "yes"
    
  print(heading)

  choose_instruction = "Please choose rock, paper, or scissors or 'quit' to exit: "
  choose_error = "Please choose rock, paper or scissors (or type 'quit' or 'q' to quit the game)"

  # Ask user for choice and check it's valid
  user_choice = choice_checker(choose_instruction, rps_list, choose_error)
  print("You Chose: ", user_choice)

  # Get computer choice
  comp_choice = random.choice(rps_list[:-1])
  print("Comp Choice: ", comp_choice)

  # Compare choices
  if user_choice == comp_choice:
    result = "draw"
  elif user_choice == "rock" and comp_choice == "scissors":
    result = "win"
  elif user_choice == "scissors" and comp_choice == "paper":
    result = "win"
  elif user_choice == "paper" and comp_choice == "rock":
    result = "win"
  else:
    result = "lose"

  # End Game if exit code is typed
  if user_choice == "quit":
      break

  print("You chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, result))
  rounds_played += 1


# Ask user if they want to see their game history, if 'yes' show game history

# Show game statistics