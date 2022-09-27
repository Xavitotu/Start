import random

a = int(input("Pick a low number: "))
b = int(input("Now pick a high number: "))
random = random.randrange(a, b)
x = int(input("Now guess a number between the two numbers you choose!"))

if x == random:
    print("Correct! ඩ")
elif x > random:        
    print(f"Nope, try again (Maybe try a higher number, the answer was {random})")
    
    print(random)

elif x < random:
    print(f"Nope, try again (Maybe try a lower number, the answer was {random})")

    print(random)
