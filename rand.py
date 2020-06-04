import os
import os.path 

userInput=raw_input("Type your name:")


print(userInput)

names=["Emmanuel","Dalilah","Sandra","Kassandra","Rudy","Jonathan","Alex","Ori"]

for i in names:
    print(i)

dir=os.getcwd()

print(dir)
