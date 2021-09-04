n=int(input())
for i in range(n):
    first=input()
    chunks = first.split(' ')
    second=input()
    dis=0
    sta=0
    for j in second:
        if(j=='0'):
            dis=dis+(1*int(chunks[1]))
            
        else:
            
            sta=sta+(1*int(chunks[2]))
    print(int(sta)+int(dis))