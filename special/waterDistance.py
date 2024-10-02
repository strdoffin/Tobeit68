"""_Water Rising!_"""
def main():
    water = int(input())
    x = int(input())
    y= int(input())
    waterDistance = water/3.14159
    peopleDistance = x**2+y**2
    if waterDistance >= peopleDistance:
        print(0)
    else:
        print(int((peopleDistance * 3.14159)/water))
main()
