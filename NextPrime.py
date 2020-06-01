'''
n=int(input("Enter a num"))
n=n+1
isPrime=False
while(isPrime==False):
    i=2
    while(i<n):
      if n%i==0:
           n=n+1
           break
      i=i+1
    if i==n:
        isPrime=True
        break
print(i)'''

def nextPrime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n
