import string
import random

print("---------------------------------------------")
print("             Password Generator")
print("---------------------------------------------")


length = int(input("Enter password length: "))
print("---------------------------------------------")
print("Choose character set for password from these:"
      "\n1. Digits\n2. Letters\n3. Special characters\n4. Pick randomly")
characterList = ""

while (True):
    ch = int(input("Pick a number "))
    if (ch == 1):
        characterList += string.ascii_letters
    elif (ch == 2):
        characterList += string.digits
    elif (ch == 3):
        characterList += string.punctuation
    elif (ch == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    characterList += string.ascii_letters + string.digits + string.punctuation
    randomchar = random.choice(characterList)
    password.append(randomchar)
    
print("---------------------------------------------")
print("The random password is " + "".join(password))
print("---------------------------------------------")
