import random
names = input("Enter the names of those who want to pay, spareted by camma \n")
name_list = names.split(", ")
rand_index = random.randint(0,len(name_list)-1)
print(name_list[rand_index])
