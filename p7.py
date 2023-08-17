num = int(input("Number of calls: "))
sum = 200
if num > 100 :
    sum = sum + (num-100)*0.6
if num > 150 :
    sum = sum + (num-150)*0.5
if num > 200:
    sum = sum + (num-200)*0.4
print("The cost for", num, "calls is:", sum)