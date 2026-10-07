while True:
  a=input("name and number")
  if a=="stop":
    break
  with open("contacts.txt","a")as f:
      f.write(a+"\n")
with open("contacts.txt","r")as f:
  for line in f:
    line =(line.strip())
    line= (line.split(","))
    print("name is:",line[0].strip())
    print("phone is:",line[1].strip())