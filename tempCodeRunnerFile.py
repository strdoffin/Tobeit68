tiers={
    "1":1,
    "2":3,
    "3":3,
    "4":6,
    "5":6,
    "6":9,
    "7":9,
    "8":12,
    "9":12,
    "10":15,
    "11":15,
}
inv_size = {
    "S":3,
    "M":9,
    "L":15,
    "None":0
}
maximum = int(input())
minions = int(input())
typed = input()
summ = 0
if (maximum <= minions):
    n = maximum
else:
    n = minions
for i in range(0,n):
    mtier , invsize , compactor  = input().split(" ")
    if(compactor == "Yes"):
        cap = (tiers[mtier] + inv_size[invsize])*9*64
    else:
        cap = (tiers[mtier] + inv_size[invsize])*64
    summ += cap
match typed:
    case "item":
        print("Item:",int(summ))
    case "block":
        print("Block:",int(summ/9))
    case "enchanted item":
        print("Enchanted Item:",int(summ/160))
    case "enchanted block":
        print("Enchanted Block:",int(summ/160/160))