H=31
legs=181
C=0
flag=0
while H>=0:
    if H*4+C*2==legs:
        flag=0
        break
    H=H-1
    C=C+1
if flag==0:
    print(H,C)
else:
    print("not possible")
        
