a,b = map(int, input("Ente The range: ").split())
for i in range(a,b+1):
    if i%3 == 0:
        print(i, end = ' ')