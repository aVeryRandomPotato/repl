import random

my_name = "Chase"

print("Hello " + my_name)

age = 10

def ageChecker(x):
  if age > 12:
    print("You're a teenager - " + x)
  else:
    print("You're a pre-teen - " + x)

ageChecker("var")

age = random.randint(10,20)

ageChecker("random")