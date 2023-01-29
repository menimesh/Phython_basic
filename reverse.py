# reverse number 
a=int(input("Enter a number"))

while a>0:
    r=a%10
    print(r,end="")
    a=a//10