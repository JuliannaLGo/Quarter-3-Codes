students = ["Raine", "Rhys", "Lemuel", "Julianna", "Maxene"]
subjects = ["Biology", "Chemistry", "Physics"]

tscores = [
    [93, 67, 78],
    [90, 89, 95],
    [92, 95, 87],
    [98, 97, 99],
    [90, 76, 67]
]

print("Student | Biology | Chemistry | Physics")
for i in range(len(students)):
    print(students[i], "|", tscores[i])

print()

print("Lemuel's Chemistry score:", tscores[2][1])
print("Julianna's scores...", tscores[3])
tscores[3][2] = 100
print("Updating Julianna's Physics score to 100")
print("Julianna's updated score:", tscores[3][2])

