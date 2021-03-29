s="abc"
l=[]
for i in range(1,len(s)+1):
    for j in range(0,i):
        print(s[j:len(s)-i:i])
