# Hi Guys This is my project for python beginner or developer.
# Practice Exercise in Python for Beginners. Create a Guess the Number game


import random

secret = random.randrange(1,50)

guess = 0
tries = 0
while guess != secret:
    guess = int(input("Guess the number 1 to 50: "))
    tries += 1
    if guess>secret:
        print("Too High Guess Again")
    elif guess<secret:
        print("Too Low Guess Again")
    
print("You Win correctly Guess!!!" "\n",tries,"times you trying")

print("THANKYOU FOR PLAYING NEXT PROJECT COMMING SOON....")
