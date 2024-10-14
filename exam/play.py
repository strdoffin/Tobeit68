# def pyramid(height):
#     for i in range(height):
#         for _ in range(height - i-1):
#             print(" ", end="")
#         for _ in range(2 * i + 1):
#             print("*", end="")
#         print()
# pyramid(5)

# i = 0 
# def pyramid(i,height):
#     if i == height:
#         return height
#     else:
#         print(" " * (height - i - 1) , end='')
#         print("*" * (2 * i + 1))
#     return pyramid(i+1,height)
# pyramid(i,5)

# def pyramid(height):
#     for i in range(height):
#         print(" " * (height - i-1), end ="") 
#         print("*" * (2 * i + 1))

# pyramid(5)

print(bool([0]))