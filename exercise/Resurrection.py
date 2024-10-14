"""Resurrection"""
def main():
    """Resurrection"""
    text = input().split(", ")
    n = len(text)
    for i in range(n):
        text[i] = 2024-int(text[i])
    for j in range(n):
        for k in range(n - j - 1):
            if text[k] > text[k + 1]:
                text[k], text[k + 1] = text[k + 1], text[k]
    for l in range(n):
        if text[l] == text[-1]:
            print(text[l])
            break
        print(text[l], end=", ")
main()
