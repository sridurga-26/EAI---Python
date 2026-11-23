import pandas as pd

n = int(input("Enter number of students: "))

rollno = []
names = []
departments = []
marks_list = []

for i in range(n):
    print(f"\n--- Student {i + 1} ---")
    rollno.append(int(input("Enter Roll No: ")))
    names.append(input("Enter Name: "))
    departments.append(input("Enter Department: "))
    marks_list.append(float(input("Enter Mark: ")))
marks = pd.Series(marks_list, index=names)

print("\n--- Pandas Series ---")
print(marks)

data = {
    "RollNo": rollno,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

threshold = float(input("\nEnter the mark threshold: "))
print(f"\nStudents scoring above {threshold}:")
print(df[df["Mark"] > threshold])