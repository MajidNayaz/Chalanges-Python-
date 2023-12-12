print("Welcome to Love Calculator!")

your_name = input("Enter your name! ")
their_name = input("Enter their name! ")
sum_names = (your_name + their_name).lower()

t = sum_names.count("t")
r = sum_names.count("r")
u = sum_names.count("u")
e = sum_names.count("e")

true = t + r + u + e

l = sum_names.count("l")
o = sum_names.count("o")
v = sum_names.count("v")
e = sum_names.count("e")

love = l + o + v + e
total_score = int(str(true) + str(love))

if total_score >= 90 or total_score <= 10:
    print(f"your score is {total_score} and you're like coke and mentos")
elif total_score >= 40 and total_score <= 50:
    print(f" your score is {total_score} your are alright togather")
else:
    print(f"your score is {total_score}")

