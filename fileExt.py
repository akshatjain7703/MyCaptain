filename= input("Input the Filename: ")
fn= filename.split('.')
ext = fn[len(fn)-1].lower()

if len(fn)==1:
  print("No extension found")

else:
  print("The extension of the file is :", end='')
  if ext=="py":
   print("'Python'")
  elif ext=="c": 
   print("'C'")
  elif ext=="cpp":
   print("'C++''")
  elif ext=="java":
   print("'Java'")
  else:
    print(ext.upper())