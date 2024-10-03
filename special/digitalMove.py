"""digital move"""
def main():
    """digital move"""
    num1 =  int(input())
    num2 =  int(input())
    if not num1 and num2<=0:
        print("หลบแบบ digital")
        return
    cal_mode = input()
    if cal_mode == "Divide":
        try:
            print(f"{num1/num2:.2f}")
        except ZeroDivisionError:
            print("หลบแบบ digital")
    else:
        try:
            if num1**num2 < 0:
                print("หลบแบบ digital")
            else:
                print(f"{num1**num2:.2f}")
        except TypeError:
            print("หลบแบบ digital")
main()
