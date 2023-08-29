a,b = map(int, input("Enter base and power: ").split())
pow= 1
for i in range(0,b):
    pow = pow*a;
print("The power of ", a, "^", b, " = ", pow, sep = '')