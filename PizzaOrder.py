size = input("What size of Pizza do you want? S, M or L")
add_pepparoni = input("Do you pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
price = 0
if size == "S":
    price = 15
    if add_pepparoni == "Y":
        price += 2

elif size == "M":
    price = 20

    if add_pepparoni == "Y":
        price += 3

elif size == "L":
    price = 25
    
    if add_pepparoni == "Y":
        price +=3

else:
    print("please intter a valiad choice!!")

if extra_cheese == "Y":
    price += 1

print(f"Your total Bill is {price}")

