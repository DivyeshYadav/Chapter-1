#function without intro
def intro(name):
    print("Good morning I am Divyesh")

user_name = input("Enter your name")
intro(user_name)

#FUNCTION WITH RETURN STATEMENT AND RECURSION
def rec_factorial(n):
    if n == 1:
      print("The factorial of  0 is 1")
      return n
    else:
       return n*rec_factorial(n-1)
    
num = int(input("Enter your number"))

if  num < 0:
   print("Sorry, factorial does not exist for negative numbers")    
elif num == 0:
   print("Factorial is  1")
else:
  print("The factorial of", num, "is", rec_factorial(num))
