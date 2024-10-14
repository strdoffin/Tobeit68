#new
vowel = "aeiou"

text = input()
if text[-1] == "e":
    print(text + "d")
elif text[-1] == "y":
    if text[-2] in vowel:
        print(text + "ed")
    else:
        print(text[:-1] + "ied")
elif len(text) >= 3 and text[-3] not in vowel and text[-2] in vowel and text[-1] not in vowel:
    print(text + text[-1] + "ed")
else:
    print(text + "ed")
#เดิม
vowel = "aeiou"

text = input()
if text[-1] == "e":
    print(text[-1] + "d")
elif text[-1] == "y":
    if text[-2] in vowel:
        print(text+"ed")
    else:
        print(text[:-1] + "ied")
elif len(text) >= 3 and text[-3] not in vowel and text[-2] in vowel and text[-1] not in vowel:
    print(text + text[-1] + "ed")
else:
    print(text+"ed")