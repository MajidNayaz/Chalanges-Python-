#this program can calculate the being prime or not of a integer number 
#by using a function and for loop

def is_prime(number):    #function for calcualting 
    is_pirme = True
    for i in range(2, number):   #check from 2 until number-1
        if number % i == 0:
            is_pirme = False     #if it is devideable on one number that it is not prim
    
    if is_pirme:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

n = int(input("Enter the number "))
is_prime(number=n)