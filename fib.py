print("Fibonacci Series")
n = int(input("Please input the number of digits required: "))

a=0
b=1
i=1

while i<=n:
  print(a, end=' ')
  a=a+b
  b=a-b
  i+=1