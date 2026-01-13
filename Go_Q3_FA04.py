names = ["Julianna", "Maxene", "Raine"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

totals = []

max_total = None
min_total = None
max_person = ""

for i in range(len(names)):
    total = sum(steps[i])
    totals.append(total)
    print(f"{names[i]}: {total} steps")

    if max_total is None or total > max_total:
        max_total = total
        max_person = names[i]

    if min_total is None or total < min_total:
        min_total = total
    
diff = max_total - min_total

print(f"{max_person} had the highest with {max_total} steps.")
print(f"Difference between highest and lowest total: {diff}.")
