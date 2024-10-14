"""Camphub"""

def main():
    """Camphub"""
    list_level = ["Senior High School","Vocational Certificate"]
    level = input().title()
    money = int(input())
    money = money >= 250
    onsite = input().title() == "True"
    
    if not onsite:
        pdpa = False
    else:
        pdpa = input().title() == "True"

    if level in list_level:
        if onsite:
            if pdpa and money:
                print("Yes")
            else:
                print("No")
        else:
            if money:
                print("Yes")
            else:
                print("No")
    else:
        print("No")