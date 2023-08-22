import random
import math
lower_limit= int(input("Enter lower limit : "))
upper_limit= int(input("Enter upper limit : "))
print("User limits are : ","[",lower_limit ,"-",upper_limit, "]")
minNumberOfGuess=math.log((upper_limit-lower_limit+1),2)
print("You have only {} count".format(minNumberOfGuess))
count=0
system_guess=random.randint(int(lower_limit),int(upper_limit))

while count<minNumberOfGuess:
    user_guess = int(input("Enter your guess: "))
    count+=1
    if system_guess==user_guess:
        print("You guess correct!")
        print("You guess correct after count ",count)
        break
    if system_guess>user_guess:
        print("Try again! You guessed too small")
    if system_guess<user_guess:
        print("Try Again! You guessed too high")

if count>minNumberOfGuess:
    print(" The number was ",system_guess)
    print(" Better luck next time! ")


