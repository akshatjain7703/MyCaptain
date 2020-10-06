def most_frequent(word):
  word = word.upper()
  dict = {}
  for i in word:
    dict[i]=0
  for i in word:
    dict[i]+=1

  i=len(word)
  while i>0:
    for j in dict:
      if dict[j]==i:
        print(j," = ",str(i).rjust(2,'0')) 
    i-=1
      

word = input("Please enter a string \n")
most_frequent(word)