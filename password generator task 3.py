import string
import random
 
# Getting password length
print("Recommented atleast 8 characters to generate strong password ! ")
length = int(input("Enter password length: "))

while True:

    try:
        char_num = int(length)

        if char_num < 8:
            print("Your number should be at least 8.")
            length = int(input("Please, Enter your number again:")) 
        
        else:
            break

    except:
        print("Please, Enter numbers only.")

        
print(" Choose character set for password from these : ")
print(" 1.Digits ")
print(" 2.Letters ")         
print(" 3.Special characters ")         
print(" 4.Generate the password ")        
 
charlist = ""
 
# Getting character set for password
while True:
    choice = int(input("Pick a number "))

    if choice == 1:
        print("selecting letters from A to Z and a to z")
        charlist += string.ascii_letters

    elif choice == 2:
        print("selecting numbers from 0 to 9")
        charlist += string.digits

    elif choice == 3:
        print("selecting punctuation ")
        charlist += string.punctuation
    elif choice == 4:
        print("Generating strong PASSWORD according to your wish. ")
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    randomchar = random.choice(charlist)

    password.append(randomchar)
 
print("The random  password is " + "".join(password))