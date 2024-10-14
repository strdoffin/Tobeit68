"""time convert"""
def main():
    """time convert"""
    try:
        time , half = input().split()
        hr, minute = time.split(':')
        minute = int(minute)
        if int(minute) >= 60:
            print("ERROR")
            return
        if minute < 10:
            minute = '0' + str(minute)
        if 0 <= int(hr) < 12 and half == 'AM':
            if int(hr) < 10:
                print(f"0{int(hr)}:{minute}")
            else:
                print(f"{int(hr)}:{minute}")
        elif 0 < int(hr) < 12 and half == 'PM':
            print(f"{int(hr)+12}:{minute}")
        elif int(hr) == 12 and half == 'PM':
            print(f"12:{minute}")
        elif int(hr) == 12 and half == 'AM':
            print(f"00:{minute}")
        else:
            print("ERROR")
    except ValueError:
        print("ERROR")

main()
