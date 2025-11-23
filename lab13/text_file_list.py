filename = "example.txt"
lines_list = []

with open(r'C:\Users\bhoga\OneDrive\example.txt', 'r') as file:
    for line in file:
        lines_list.append(line.strip())

print("List of lines:")
print(lines_list)