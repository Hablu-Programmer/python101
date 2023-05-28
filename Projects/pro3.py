import random

RandomNumber = random.randrange(1,200)

userInput = int(input("Guess the number:"))

if userInput > RandomNumber :

    print("the number is to high")
elif RandomNumber>userInput :
    print(RandomNumber)
    print("the number is too low")

else:
    print(RandomNumber)
    print("yes, you matched the number")



