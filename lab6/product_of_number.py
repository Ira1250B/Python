n=int(input("Enter any number\n"))
temp=n
pro=1
while(temp>0):
    r=temp%10
    pro=pro*r
    temp=temp//10
print("The product of:",n,"is",pro)