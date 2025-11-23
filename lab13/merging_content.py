with open("file1.txt", "w") as f:
    f.write("ICT DEPARTMENT")

with open("file2.txt", "w") as f:
    f.write("Python is Fun")

with open("file1.txt", "r") as f1:
    content1 = f1.read()

with open("file2.txt", "r") as f2:
    content2 = f2.read()

with open("merged.txt", "w") as merged_file:
    merged_file.write(content1)
    merged_file.write(content2)

print("Files merged successfully ")

with open("merged.txt", "r") as merged_file:
    print("Content of merged.txt:")
    print(merged_file.read())