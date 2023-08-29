def intToBin(n):
    if n>0:
        return intToBin(int(n/2))*10 + n%2
    else:
        return 0
n = int(input("Enter a number: "))
print(intToBin(n))