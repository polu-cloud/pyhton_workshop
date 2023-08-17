ch = input("Enter a character: ")
if (ch >= 'a' and ch <='z'):
    print(ch, "is a lower case character")
elif (ch >= 'A' and ch <= 'Z'):
    print(ch, "is a upper case character")
else:
    print(ch, "is not a alphabatic character")