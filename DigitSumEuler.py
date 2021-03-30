n=1
s=0
while(n<50):
    cn=n
    mdx=0
    mposfl=0
    pos=0
    nod=0
    while(cn>0):
        ld=cn%10
        nod=nod+1
        if(ld>mdx):
            mdx=ld
            mposfl=pos
        cn=cn/10
        pos=pos+1

    apos=nod-mposfl
    
    i=0
    sr=0
    while(n>0):
        if(i==apos):
            continue
        else:
            sr=sr+(n%10)
        n=n/10
        
    if(sr==mdx):
        print(mdx)

    n=n+1
    
        
    
    
    
    
    n=n+1
    
