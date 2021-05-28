# Functions go here
def check_rounds(question, error):

  valid = False
  while True:
    response = input(question)
    
    if response != "":
      try:
        response = int(response)

        if response < 1: 
          print(error)
          print()
          continue

      except ValueError:
        print(error)
        print()
        continue

    return response
    
  

# Main routine goes here
rounds_played = 0 
choose_instruction = "Please choose rock (r), paper (p), or scissors (s) "

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds("How many rounds: ", "Please type either <enter> or an integer that is more than 0 ") 

end_game = "no"
while end_game == "no":
  
  # Rounds Heading 
  print()
  if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    print(heading)

    choose = input("{} or 'quit' to end: ".format(choose_instruction))

    if choose == "quit":
      break
  
  else:
    heading = "Round {} of Round {}".format(rounds_played + 1, rounds)
    print(heading)

    choose = input(choose_instruction)

    if rounds_played == rounds - 1:
      end_game = "yes"

  print("You chose {}".format(choose))

  rounds_played += 1

print("Thank you for playing")

