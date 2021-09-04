n=int(input())
for i in range(n):
    ip=input()
    chunks = ip.split(' ')
    A=int(chunks[0])
    B=int(chunks[1])
    C=int(chunks[2])
    D=int(chunks[3])
    E=int(chunks[4])
    if((A+B)<=D) and (C<=E):
        value="YES"
    elif((A+B)<=E) and (C<=D):
        value="YES"
    elif((A+C)<=E) and (B<=D):
        value="YES"
    elif((A+C)<=D) and (B<=E):
        value="Yes"
    elif((C+B)<=E) and (A<=D):
        value="Yes"
    elif((C+B)<=D) and (A<=E):
        value="YES"
    else:
        value="NO"
    print(value)
        
        