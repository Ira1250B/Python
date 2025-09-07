s=input("Enter a sentence\n")
st=s.split()
long=""
for word in st:
    if(len(word)>len(long)):
        long=word
print("The longest word in sentence is: \n",long)