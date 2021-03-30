T=int(input()) #Input for number of test cases

for t in range(T):
    I=int(input()) #Number of Elements in Array
    vals=list(map(int,input().split())) #List of integers
    total=0
    for i in range(1,I-1): #Iterate till I-1
        mini=vals.index(min(vals[i:]))  #Find min Index
        total+=mini-i+1   #Calculate Cost
        temp=vals[i:mini+1]  #Reverse List
        temp.reverse()
        vals[i:mini+1]=temp
    print('Case #{}:{}'.format(t+1,total))#Print Output
