# RPS Component 3 - Compare user and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
  user_index = 0
  for item in rps_list:
    user_choice = rps_list[user_index]
    comp_choice = rps_list[comp_index]

    # Compare options
    if user_choice == comp_choice:
      result = "draw"
    elif user_index == comp_index+1 or user_index == comp_index-2:
      result = "win"
    else:
      result = "lose"

    print("You chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, result))

    user_index += 1 
  
  comp_index += 1
  print()
