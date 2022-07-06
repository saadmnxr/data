from re import I


i=int(input("Enter your number:"))
rev=0
x=i

while (i>0):
    rev=(rev*10)+i%10
    i=i//10
print("reverse of number is",rev)

if (x==rev):
    print("Number is palindrome")
else:
    print("number is not palindrome")


