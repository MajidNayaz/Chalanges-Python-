#this program can encrypt and decrypt the message by spacifice shift number

alphabit = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            #we doublecate the alphabit to avoid index error when we shift a z with a number

def ceaser(text, shift, action):
    cipher = ""
    if action == "decode":   #if the the user want to decode the message we must subtruction from position
        shift *= -1
    for letter in text:
        if letter in alphabit:
            position = alphabit.index(letter)
            new_position = position + shift
            cipher += alphabit[new_position]
        else:
            cipher += letter
   
    print(f"your {action}d massages is {cipher}")

should_continue = True

while should_continue:
    action = input("Enter 'encode' for encrypt and 'decode' for decrypt\n")
    massage = input("Enter your massage\n").lower()
    shift = int(input("Enter the shift number\n")) % 26
        
    ceaser(massage, shift, action)
    
    result = input("If you want to continue type yes, Otherwise type no\n")
    if result=="no":
        should_continue = False
        print("Good Buy")
