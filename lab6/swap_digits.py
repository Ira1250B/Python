n = input("Enter any number\n")

if len(n) == 1:
    swapped = n   # single digit, nothing to swap
else:
    swapped = n[-1] + n[1:-1] + n[0]   # last + middle + first

print("The number with swapped first and last digits is:", swapped)
