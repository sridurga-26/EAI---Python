import csv 
students = []  
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))
    students.append({"RollNo": roll, "Name": name, "Department": dept, "Mark": mark})

course_name = input("\nEnter course name: ")
credits = int(input("Enter credits: "))
course = (course_name, credits)
print("Course Tuple:", course) 
with open("students.txt", "w") as file: 
    for student in students: 
        file.write(str(student) + "\n") 
with open("students.csv", "w", newline="") as file: 
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields) 
    writer.writeheader() 
    writer.writerows(students) 
print("\n--- Records from CSV ---") 
with open("students.csv", "r") as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        print(row["RollNo"], row["Name"], 
              row["Department"], row["Mark"]) 
