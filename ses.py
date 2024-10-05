"""ses"""
def main():
    """ses"""
    text = input()
    vowel = ["a","e","i","o","u"]
    checkstateone =text[-1] == "s" or text[-1] == "x" or text[-1] == "z" or text[-1] == "o"
    if len(text)<1:
        print(text)
        return
    if len(text) == 1:
        if checkstateone:
            print(text + "es")
        else:
            print(text + "s")
        return
    if( checkstateone or (text[-2] == "s" and text[-1] == "h")
        or (text[-2] == "c" and text[-1] == "h" ) ):
        print(text + "es")
    elif(text[-1] == "y" and text[-2] not in vowel):
        print(text[:-1] + "ies")
    else:
        print(text + "s")
main()
