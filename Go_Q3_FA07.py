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

minimum = tscores[0][0]
maximum = tscores[0][0]

for i in range(len(students)):
    total = sum(tscores[i])
    average = total/len(tscores[i])
    minimum = min(tscores[i])
    maximum = max(tscores[i])
    print(f"{students[i]} | Total Score: {total} | Average: {average:.2f} | Min: {minimum} | Max: {maximum}")
    
