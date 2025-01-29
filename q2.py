# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = ["cow", "pig", "chicken", "goat", "sheep", "duck"]
animal_rand = random.choice(animal)
# Age (integer)
age = ["6 months old", "3 months old", '2 years old', '3 years old', '10 years old', 'a newborn']
age_rand = random.choice(age)
# Color (at least 3 choices, string)
color = ["black", "white", "brown", "tan", "speckled"]
color_rand = random.choice(color)
# Weight (float)
weight = ["10 lbs", "15lbs", "25lb", "100lb", "50lb"]
weight_rand = random.choice(weight)
pronoun = ""
gender = ["She", "He"]
gender_rand = random.choice(gender)

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal_rand}! {gender_rand} is {age_rand}, weighs {weight_rand}, and has {color_rand} skin!")
      