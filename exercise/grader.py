"""Grader"""
def main():
    """Grader"""
    a = float(input())
    b = float(input())
    c = float(input())
    total = a + b + c

    if 95 <= total <= 100:
        print("A")
    elif 90 <= total < 95:
        print("B+")
    elif 85 <= total < 90:
        print("B")
    elif 80 <= total < 85:
        print("C+")
    elif 75 <= total < 80:
        print("C")
    elif 70 <= total < 75:
        print("D+")
    elif 65 <= total < 70:
        print("D")
    elif 60 <= total < 65:
        print("F+")
    elif 0 <= total < 60:
        print("F")
    else:
        print("ERROR")

main()
