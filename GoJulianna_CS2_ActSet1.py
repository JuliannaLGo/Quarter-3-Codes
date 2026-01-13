student = {}

name = input("Enter your name: ")
student["Name"] = name
age = input("Enter your age: ")
student["Age"] = age
subj = input("Enter your favorite subject: ")
student["Favorite Subject"] = subj

print()
print("Student Record:")

for key, value in student.items():
    print(f"{key}: {value}")
