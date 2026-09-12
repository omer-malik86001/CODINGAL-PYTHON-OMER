import random
seceret_no=random.randint(1,100)
print("the game is about to begin guess the seceret number!")
while True:
    guess=int(input("what is your guess! "))
    if guess==seceret_no:
        print("CONGRATS U HAVE GUESSED THE CORRECT MUMBER!")
        break
    else:
        print("nice try but pls try again")

       # BNONUS::U CAN GIVE A HINT LIKE HOT OR COLD AND TELLL THE USER HOW CLOSE THEY ARE TO THE ANSWER.