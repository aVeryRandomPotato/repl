import random

my_name = "Chase"

print("Hello " + my_name)

age = 10

def ageChecker(x):
  if age > 12 and age < 20:
    print("You're a teenager - " + x)
  elif age <= 12:
    print("You're a pre-teen - " + x)
  else:
    print("You're an adult - " + x)

ageChecker("var")

age = random.randint(10,20)

ageChecker("random")

print(age)