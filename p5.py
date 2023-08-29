def reverseDigit(n):
    return n[::-1]
n = int(input("Enter a numeber: "))
if n == int(reverseDigit(str(n))):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")