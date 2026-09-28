import random
import time
import math

def intro():
    name=input("would you like to tell me your name ? ")

    print(f"welcome,{name}")
    print("i am thinking of a number between 1 and 100")
    print("you have a total of 10 attempts")
    print("ALL THE BEST ! ")

def start_game():
    seceret=random.randint(1,100)
    attempts=0

    while attempts <=10:
        time.sleep(1)
        try:
            guess=int(input("\nwhat is your guess: "))
        except ValueError :
            print("warning please enter a number.")
            continue

        if guess > 100 or guess < 1:
            print("that number is not in the range provided in the instructions")
            print("pls enter a number between 1 and 100")
            continue
        
        attempts += 1
        if seceret==guess:
            print("YOU HAVE GUESSED CORRECT CONGRATULATIONS")
            break
        distance=math.fabs(seceret-guess)
        if distance <=5:
            print("you are VERY HOT")
        elif distance <=15:
            print("you are WARM")
        elif distance <=25:
            print("you are COLD")
        else:
            print("you are very cold")
    if attempts > 10 and guess != seceret:
        print(f"sorry you ran out of attempts the secret number is {seceret}")
    

    

         
intro()
start_game()

    

        