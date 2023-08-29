def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b,a%b)

a, b= map(int,input("Enter two integers: ").split())
if(a<b):
    a,b = b,a
print("GCD of",a,"and", b,"is",GCD(a,b))
print("LCM of",a,"and", b,"is",int(a*b/GCD(a,b)))
