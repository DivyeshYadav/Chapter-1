#Variable for the for loop
str = "DIVYESH"
#For loop:
for charc in str:
    print(charc)

#Nested Looping
adv = ["red","healthy","tasty"]
fruit = ["apple","banana","cherry"]

for x in adv:
    for y in fruit:
        print(x,y)

#Table of 5
for i in range(1,11):
    print(5 * i )

#Star Pattern
for i in range(1,11):
    for j in range(i):
        print("*",end="  ")
    print("\n")

    