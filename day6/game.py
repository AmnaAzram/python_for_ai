import random

secret_number = random.randint(1,101)
attempt = 3

print("============Welcom To the number guessing game=========")

for i in range(0,5):
    user_input = int(input("enter the guess number [0-100] you have 3 attempts : "))
    if user_input == secret_number:
        print(f"Congrats you win the game in attempt {i+1}")
        break
    elif user_input < secret_number:
        attempt -=1
        print(f"Your guess is too low now you have {attempt} left")
        
    elif user_input > secret_number:
        attempt -=1 
        print(f"Your guess is too heigh you have {attempt} left")

    if attempt ==0:
        print(f"you don't have attempts you lose and your secret number was {secret_number}")
        break