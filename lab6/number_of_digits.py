n=int(input("Enter any number\n"))
count=0
while(n!=0):
    n=n//10
    count+=1
print("Number of digits are:",count)