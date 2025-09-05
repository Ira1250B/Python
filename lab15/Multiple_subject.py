import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Drop old tables if exist (for clean run)
cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS enrollment")

# Create a student table
cursor.execute('''CREATE TABLE student (
                    Enrollment INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL
                )''')

# Create an enrollment table
cursor.execute('''CREATE TABLE enrollment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Enrollment INTEGER,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    FOREIGN KEY (Enrollment) REFERENCES student (Enrollment)
                )''')

conn.commit()

# Insert 3 sample students
students = [
    (1, 'Ira'),
    (2, 'Saloni'),
    (3, 'Avani')
]
cursor.executemany("INSERT INTO student (Enrollment, Name) VALUES (?, ?)", students)

# Insert 3 subjects for each student (PWP, Maths, BEE)
enrollments = [
    (1, 'PWP', 85), (1, 'Maths', 90), (1, 'BEE', 88),
    (2, 'PWP', 78), (2, 'Maths', 82), (2, 'BEE', 80),
    (3, 'PWP', 92), (3, 'Maths', 87), (3, 'BEE', 89)
]
cursor.executemany("INSERT INTO enrollment (Enrollment, Subject, Mark) VALUES (?, ?, ?)", enrollments)

conn.commit()

# Fetch all student records with their subjects
cursor.execute('''SELECT student.Name, enrollment.Subject, enrollment.Mark
                  FROM student
                  JOIN enrollment ON student.Enrollment = enrollment.Enrollment''')

rows = cursor.fetchall()
print("All Student Records with Multiple Subjects:")
for row in rows:
    print(row)

# Calculate average marks per student
print("\nAverage Marks per Student:")
for sid, name in students:
    cursor.execute('SELECT AVG(Mark) FROM enrollment WHERE Enrollment = ?', (sid,))
    avg = cursor.fetchone()[0]
    print(f"{name}: {avg:.2f}")

# Calculate overall average mark
cursor.execute("SELECT AVG(Mark) FROM enrollment")
overall_avg = cursor.fetchone()[0]
print(f"\nOverall average mark: {overall_avg:.2f}")

conn.close()
