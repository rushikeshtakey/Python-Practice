# Get a character input and print a character befor it and after it as per its ASCII value
mid=ord(input("Enter a character:"))
print(chr(mid-1),chr(mid),chr(mid+1))

# Get a character input and print 4 characters befor it and 4 characters after it as per its ASCII value
mid=ord(input("Enter a character:"))

for i in range(-4,5):
    print(chr(mid+i),end=" ")