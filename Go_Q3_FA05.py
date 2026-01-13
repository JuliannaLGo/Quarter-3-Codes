days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

totals = []

for l in range(len(days)):
    total = sum(steps[i][l] for i in range(len(steps)))
    totals.append(total)
    print(f"{days[l]}: {total} steps")

max_total = max(totals)  
active_day = days[totals.index(max_total)]

print(f"The most active day is {active_day} with {max_total} steps.")
    
    
    
