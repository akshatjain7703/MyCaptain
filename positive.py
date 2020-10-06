n=int(input("How many numbers do you want to add? \n"))

list=[]

i=0
while i<n:
  list.append(int(input("Number "+ str(i+1) + " : ")))
  i+=1

for i in list:
  if i>0:
    print(i, end=" ")