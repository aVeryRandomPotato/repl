import random

my_name = "Chase"

print("Hello " + my_name)

age = 10

def ageChecker(x):
  if age > 12 and age < 20:
    print("You're a teenager - " + x)
  elif age <= 12:
    print("You're a pre-teen - " + x)
  elif age > 19 and age < 65:
    print("You're an adult - " + x)
  else:
    print("You're a senior - " + x)

ageChecker("var")

age = random.randint(10,90)

ageChecker("random")

print(age)

