import random
import time
from colorama import Fore

OPERATORS = ["+", "-", "*"]
MIN_NUM = 3
MAX_NUM = 15
correct = 0
wrong = 0
run = True
chance = 0
skips = 0
while run:

    left = random.randint(MIN_NUM, MAX_NUM)
    right = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(OPERATORS)
    

    if operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    elif operator == '*':
        result = left * right
    print(Fore.BLUE, "Question: ", str(left) + str(operator) + str(right))
    print(Fore.GREEN)
    user_input = input("Enter your answer: ")
    if str(user_input) == "q":
        run = False
    elif user_input == "":
        print(Fore.RED, "You lost a point for skipping!!")
        correct-=1
        skips+=1
        chance+=1
        continue
    elif int(user_input) == result:
        print(Fore.GREEN, "Correct!")
        correct+=1
        chance+=1
    else:
        print(Fore.RED, "Wrong Answer retry")
        wrong+=1
        chance+=1
print(Fore.BLACK, "-------------------------------------------------------------------------------------------")
print(Fore.MAGENTA, "Total chances = ", chance)
print("YOU SCORED ", correct, " OUT OF ", chance)
print("Wrong = ", wrong)
print("You skipped ", skips, " time(s)!!")
print(Fore.BLACK, "-------------------------------------------------------------------------------------------")

