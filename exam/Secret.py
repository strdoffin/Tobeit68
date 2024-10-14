textdict = {
    "0" : "O",
    "1" : "I",
    "2" : "Z",
    "3" : "E",
    "4" : "A",
    "5" : "S",
    "7" : "L"
}
dicttext = {
    "O" : "0",
    "I" : "1",
    "Z" : "2",
    "E" : "3",
    "A" : "4",
    "S" : "5",
    "L" : "7"
}
text = input()
typed = input()
output = ""
match typed:
    case "received":
        for i in text:
            if i in textdict:
                output += textdict[i]
            else:
                output += i
    case sent:
        for i in text:
            if i in dicttext:
                output += dicttext[i]
            else:
                output += i
print(output)