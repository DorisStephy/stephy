num=int(input("enter a number:"))
if num>1:
  for i in range(2,num):
    if (i%2)==0:
        print("not a prime no")
        break
  else:
    print("yes")
else:
  print("no")
