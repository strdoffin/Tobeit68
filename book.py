costs = []
free = 0
while True:
    text = input()
    if text == "ENTER":
        break
    costs.append(int(text))
    if len(costs) < 6:
        free = 0
    elif len(costs) < 12:
        free = 1
    elif len(costs) < 20:
        free = 2
    else:
        free = 4 + (len(costs) - 20) // 5

costs = sorted(costs)
print(sum(costs[free:]))