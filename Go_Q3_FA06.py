student = {}

name = input("Enter your name: ")
name = name.capitalize()
student["Name"] = name
age = input("Enter your age: ")
student["Age"] = age
subj = input("Enter your favorite subject: ")
subj = subj.capitalize()
student["Favorite Subject"] = subj

print()
print("Student Record:")

for key, value in student.items():
    print(f"{key}: {value}")
