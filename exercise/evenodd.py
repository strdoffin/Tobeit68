"""even or odd"""
def main():
    """even or odd"""
    try:
        num = float(input())
    except ValueError:
        print("Error")
        return
    if num%1 > 0:
        print("Error")
        return
    if not num % 2:
        print("Even")
    else:
        print("Odd")
main()
