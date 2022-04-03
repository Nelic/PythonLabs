import math

# print("Input Alpha ")
# a = float(input()) * 180 / math.pi
# print("Input Beta ")
# b = float(input()) * 180 / math.pi
# z = math.sin(a + b) * math.sin(a - b)
# print("Result ",z)


# M = float(input("Input some km per day "))
# K = float(input("Input percent "))
# i = 0
# while M < 50:
#     i += 1
#     M += M * (K / 100)
#
# print(i)
# print(M)


array = []
for i in range(int(input())):
    array.append(int(input()))

multiply = 1
array.reverse()
for i in array:
    if i != 0:
        print(i, end=" ")
        if i < 0:
            multiply *= i
print('\n', "Multiply", multiply)

array.sort()
for i in reversed(array):
    if i < 0:
        print("Biggest negative number ", i)
        break