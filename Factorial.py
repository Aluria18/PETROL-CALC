def fact(n):
  if n==1:
    return n
  else:
    return n*fact(n-1)
x=int(input("Enter any integer:"))
fact(x)