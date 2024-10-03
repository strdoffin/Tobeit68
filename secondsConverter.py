"""SecondsConverter"""
def main():
    """SecondsConverter"""
    seconds = int(input())
    minutes = seconds//60
    hours = minutes//60
    days = hours//24
    print(
        f"{days}:"
        f"{"0"+str(hours%24) if hours%24 < 10 else hours%24}:"
        f"{"0"+str(minutes%60) if minutes%60 < 10 else minutes%60}:"
        f"{"0"+str(seconds%60) if seconds%60 < 10 else seconds%60}")
main()
