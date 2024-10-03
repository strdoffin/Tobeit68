"""How to calculate time zone difference."""
from datetime import datetime, timedelta
def main():
    """Calculate time zone difference."""
    time = input()
    gmtnow = float(input())
    minnow = (int(gmtnow) * 60) + (gmtnow % 1 * 100)
    gmtfind = float(input())
    minfind = (int(gmtfind) * 60) + (gmtfind % 1 * 100)
    gmtdiff = abs(minnow - minfind)
    if gmtnow < gmtfind:
        gmtdiff = int(gmtdiff / 60) + (gmtdiff % 60 / 100)
    else:
        gmtdiff = -1 * (int(gmtdiff / 60) + (gmtdiff % 60 / 100))
    time_obj = datetime.strptime(
        time.replace("P.M.", "PM").replace("A.M.", "AM"),
        "%I:%M %p"
    )
    time_to_subtract = timedelta(hours=int(gmtdiff),\
        minutes=(gmtdiff - int(gmtdiff)) * 100)
    new_time = time_obj + time_to_subtract
    new_time_str = new_time.strftime("%I:%M %p").replace("AM", "A.M.")\
        .replace("PM", "P.M.")
    print(new_time_str)
main()
