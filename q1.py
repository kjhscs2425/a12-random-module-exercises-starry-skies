
"""
    Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """


  #YOUR CODE HERE
import random

def spin_twister_spinner():
  colors = ["red", "green", "yellow", "blue"]
  random_colors = random.choice(colors)
  sides = ["left", "right"]
  random_sides = random.choice(sides)
  appendage = ["hand", "foot"]
  random_app = random.choice(appendage)
  spin = [random_colors, random_sides, random_app]
  return f"{random_colors} {random_sides} {random_app}"

for i in range(10):
    print(spin_twister_spinner())

