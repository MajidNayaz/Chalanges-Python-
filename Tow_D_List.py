list1 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list2 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list3 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list4 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list5 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list6 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list7 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list8 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]
list9 = ["❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️","❤️️",]

list10 = [list1, list2, list3, list4, list5, list6, list7, list8, list9]

option = input("Which one do wanna change sperated with one space between row and colomn\n").split(" ")
row = int(option[0])
colomn =int(option[1])

if row < 10 and colomn < 10:
     list10[row-1][colomn-1] = "😜"
     print(f"{list1}\n{list2}\n{list3}\n{list4}\n{list5}\n{list6}\n{list7}\n{list8}\n{list9}")
else:
    print("you're intered wrong number! \n")



