a=int(input("Enter First num:"))
b=int(input("Enter Second num:"))
c=int(input("Enter Third num:"))

if a>b:
      if a>c:
           print(a)
      else:
           print(c)
elif b>a:
    if b>c:
        print(b)
    else:
        print(c)

#x=(a>b)?((a>c)?a:c):((b>c)?b:c) In C Language Simplest Method.
z=(a if (a>c) else c) if (a>b) else (b if (b>c) else c)
print(z)
#This method is cumbersum but is more efficient as less number of comparisions.
