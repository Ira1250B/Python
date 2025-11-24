import re
def validate_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    return False
def validate_pan_number(pan):
    pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern,pan):
        return True
    return False
pan=input("Enter pan number\n")
email=input("Enter Email ID\n")
if validate_pan_number(pan)&validate_email(email):
    print("Both Email and PAN numbers are valid\n")
elif validate_pan_number(pan):
     print("Only PAN is valid\n")
elif validate_email(email):
    print("Only E-mail is valid\n")
else:
    print("None is valid\n")