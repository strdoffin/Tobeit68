"""binary to decimal"""
def main():
    """binary to decimal"""
    bi = input()
    output = 0
    for i in range(1,len(bi)+1):
        if bi[-i] == '1':
            output += 2**(i-1)
        elif bi[-i] == '0':
            output += 0
        else:
            print("Error")
            return
    print(output)
main()
