people = input().split(" ")
kingpos = people.index("KingNice")
try:
    if "KingNice" == people[0]:
        print(people[1])
    elif "KingNice" == people[-1]:
        print(people[-2])
    else:
        print(people[kingpos - 1],people[kingpos + 1])
except IndexError:
    print("")