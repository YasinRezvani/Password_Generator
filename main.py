import random
from beautifultable import BeautifulTable

char = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLPOIUYTREWQ1234567890@#$%&*."

lens = int(input("What is the length of the password: "))

table = BeautifulTable()
for pas in range(0 , 5):
    password = ""
    for l in range(lens):
        password += random.choice(char)
    table.rows.append([password])                
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)         
    table.columns.header = ["Your Password"]
print(table)



# Made By Yasin Rezvani