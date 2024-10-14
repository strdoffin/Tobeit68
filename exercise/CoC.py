"""Curse of Confusion"""
def main():
    """Curse of Confusion"""
    x= int(input())
    y= int(input())
    text= input()
    for i in text:
        match i:
            case 'U':
                y -=1
            case 'D':
                y +=1
            case 'L':
                x +=1
            case 'R':
                x -=1
    print(x,y)
main()
