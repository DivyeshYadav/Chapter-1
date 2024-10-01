def fib_Series(nterms):
  n1 = 0
  n2 = 1
  count = 0
  while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

nterms = int(input("How many terms"))
if nterms <= 0:
  print("Please Enter a Positve Number")

elif nterms == 1:
  print("Fibonacci Series",nterms,":")
  fib_Series(nterms)

else:
  print("Fibonacci Series")
  fib_Series(nterms)