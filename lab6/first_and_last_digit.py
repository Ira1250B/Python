n=int(input("Enter any number\n"))
last_digit=n%10
first_digit=n
while(first_digit>=10):
    first_digit=first_digit//10
print("The first and last digit of",n,"are: ",first_digit," ",last_digit)
