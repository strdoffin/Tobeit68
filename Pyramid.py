"""Pyramid"""
def main():
    """Pyramid"""
    floor = int(input())
    n = int(input())
    for i in range(1, floor+1):
        for _ in range(0, n):
            for _ in range(1, floor-i+1):
                print(" ", end="")
            for _ in range(1, 2*i):
                print("*", end="")
            for _ in range(1, floor-i+1):
                print(" ", end="")
        print()
main()
