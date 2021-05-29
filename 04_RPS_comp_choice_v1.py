# RPS Component 1 - generate computer choice

import random

rps_list = ["rock", "paper", "scissors"]

for x in range(0, 20):
  comp_choice = random.choice(rps_list)
  print(comp_choice, end='\t')