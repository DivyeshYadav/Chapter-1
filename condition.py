#simple if statement
num = int(input("Enter a number"))
if num > 50:
    print("pass")
else:
    print("fail")  

#multiple if statement
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("A+")
elif marks == 50:
    print("A")
else:
    print("F")
#nested condition
age = float(input("Enter your age"))
if age > 0 :
    if age > 18 :
        print("adult")
    else:
        print("not  a adult")
else:
    print("invalid input")

