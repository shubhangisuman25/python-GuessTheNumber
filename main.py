import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm tinking a number between 1 to 100.")

number = random.randint(1,100)
# print(f"the answer is {number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(level == 'easy'):
  attempts = 10
elif(level == 'hard'):
  attempts = 5

  
while (attempts > 0):
  guess = int(input("Make a guess: "))
  if(guess < number):
    print("Too low")
    attempts = attempts -1
  elif(guess > number):
    print("Too high")
    attempts = attempts -1
  elif(number == guess):
    print(f"You got it! The answer was {number}")
    break
  print(f"The attempts left {attempts}")