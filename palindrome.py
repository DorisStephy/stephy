num=(input("enter a number:"))
num=int()
temp=num
rev=0
while temp!=0:
  rev=(rev*0)+(temp%10)
  temp=temp//10
if temp==rev:
  print("yes")
else:
  print("no")
