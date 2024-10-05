"""passkey"""
def main():
    """passkey"""
    text = input()
    output = ""
    for i in text:
        try:
            n = int(i)
            output += str(n)
        except ValueError:
            output += " "
            continue
    print(output)
    numbers = [int(num) for num in output.split()]
    print(numbers)
    print(sum(numbers))
main()
