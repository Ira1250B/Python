filename = "example.txt"

lines = 0
words = 0
characters = 0

with open(r'C:\Users\bhoga\OneDrive\example.txt', 'r') as file:
    for line in file:
        lines += 1
        characters += len(line)
        words += len(line.split())

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)