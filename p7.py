def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        
n = int(input("Enter the number of Fibonacci numbers: "))
print("Fibonacci numbers upto", n, "terms")
fibo(n)