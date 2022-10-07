n=int(input("Enter the number:"))
if (n>0 and n<=999):
    a=int(n/100)
    b=int(n%100)
    c=int(b/10)
    d=int(b%10)
    print(a,c,d)
    print(a,d,c)
    print(c,a,d)
    print(c,d,a)
    print(d,a,c)
    print(d,c,a)
if(n<0):
    print("Positive number required!")
if(n>=1000):
    print("Enter number is bigger than expected!")
