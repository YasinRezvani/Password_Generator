import random

char = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLPOIUYTREWQ1234567890@#$%&*."

lens = int(input("What is the length of the password: "))
print("\nYour Password:")
print("---------------------------------")

for pas in range(0 , 5):
    password = ""
    for l in range(lens):
        password += random.choice(char)
       
    print(password)    

print("---------------------------------")

# Made By Yasin Rezvani