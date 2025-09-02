n=int(input("enter any number:"))
sum=0
temp=n
while(temp>0):
    r=temp%10
    sum=sum*10+r
    temp=temp//10
print("Reversed number is: ",sum)