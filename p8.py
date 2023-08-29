a,b = map(int, input("Enter the range: ").split())

for i in range(a,b+1):
    if i<=3:
        if i>1:
            print(i, end = ' ')
        continue
    ch = 0
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            ch += 1
    if ch==0:
        print(i, end = ' ')