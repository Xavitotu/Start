z = input("Pick addition (a), subtraction (s), multiplication (m), or division (d): ")

x = float(input("Now pick a number: "))


y = float(input("Now pick the second number: "))

if z == "a":
    print(x+y)

elif z == "s":
    print(x-y)

elif z == "m":
    print(x*y)

elif z == "d":
    print(x/y)

j = input("Continue? (y/n) ")

while j == "y":
    f = input("Pick addition (a), subtraction (s), multiplication (m), or division (d): ")
    w = float(input("Now pick a third number "))