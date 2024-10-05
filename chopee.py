"""Chopee discount calculation."""
def main():
    """Chopee discount calculation."""
    k = float(input())
    l = float(input())
    m = float(input())
    n = float(input())
    if k >= l:
        total_ship = k
    else:
        total_ship = k+m
    
    total_ship_discount = (k+m)*(1-n/100)

    if total_ship > total_ship_discount:
        print(2)
        print(total_ship_discount)
    elif total_ship_discount > total_ship:
        print(1)
        print(total_ship)
    elif total_ship == total_ship_discount:
        print(1)
        print(total_ship)
main()
