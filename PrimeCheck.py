n=int(input("Enter a num"))
i=2
isPrime=True
while(i<n):
 if n%i==0:
  isPrime=False
  break
 i=i+1

if isPrime==True:
 print("Num is Prime")
else:
    print("Not Prime")
