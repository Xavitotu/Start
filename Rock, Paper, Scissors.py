import random

a = 1
b = 2
c = 3

x = int(input("Pick rock (1), paper (2), or scissors (3): "))

random = random.randrange(1, 4)

if x == random:
    print("It's a tie!")
    print(random)

elif random == a and x == b:
    print("You Win!")
    print("I chose Rock")
    
elif random == b and x == c:
    print("You Win!")
    print("I chose Paper")

elif random == c and x == a:
    print("You Win!")
    print("I chose Scissors")

elif random == a and x == c:
    print("You Lose!")
    print("I chose Rock")

elif random == b and x == a:
    print("You Lose!")
    print("I chose Paper")

elif random == c and x == b:
    print("You Lose!")
    print("I chose Scissors")