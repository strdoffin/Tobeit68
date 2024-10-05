# inputs = [int(x) for x in input().split(", ")]
# result = [2024 - value for value in inputs]
# n = len(result)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if result[j] > result[j+1]:
#             result[j], result[j+1] = result[j+1], result[j]
# print(", ".join(str(res) for res in result))

def generate_pattern(n):
    size = 2 * n - 1
    pattern = [[0] * size for _ in range(size)]
    
    for i in range(n):
        for j in range(i, size - i):
            pattern[i][j] = n - i
            pattern[size - i - 1][j] = n - i
            pattern[j][i] = n - i
            pattern[j][size - i - 1] = n - i
            
    for row in pattern:
        print(" ".join(f"{num:02d}" for num in row))

# Input
n = 4
generate_pattern(n)
