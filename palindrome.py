a=int(input("enter an number"))
temp=a
sum=0
while a>0:
    r=a%10
    sum=sum*10+r
    a=a//10
if temp==sum:
    print("Palindrome")    

else:
    print("not palindrome")