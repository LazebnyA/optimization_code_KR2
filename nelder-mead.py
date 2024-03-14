import matplotlib.pyplot as plt
import numpy as np


def func(x1, x2):
    return 2 * (x1 - 2) ** 2 + (x2 - 4) ** 2


# Задаем координаты точек
x = [5, 7, 5]
y = [4, 6, 6]

print("Ітерація 1.")
print("1 | 2 | 3")
for el in zip(x, y):
    if el == min(zip(x, y), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x, y), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

# x_2 max

x_mean = (
    (x[0] + x[2]) / 2,
    (y[0] + y[2]) / 2
)

x_new = (
    (2 * x_mean[0] - x[1]),
    (2 * x_mean[1] - y[1])
)

print(f"Пробне відображення альфа = 1: x_нов = {x_new}")
print(f"f{x_new} = {func(*x_new)}")

x_4 = (
    3 * x_mean[0] - 2 * x[1],
    3 * x_mean[1] - 2 * y[1]
)

print(f"Відображення гамма = 2: x_4 = {x_4}")
print(f"f{x_4} = {func(*x_4)}")
print(f"Залишимо x_4 = {tuple(x_new)}")

x_4 = x_new

print("1 | 2 | 3")
print("1 | 4 | 3")

print("_" * 50)

x2 = [5, 3, 5]
y2 = [4, 4, 6]

print("Ітерація 2.")
for el in zip(x2, y2):
    if el == min(zip(x2, y2), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x2, y2), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

# x_3 max

x_mean = (
    (x2[0] + x2[1]) / 2,
    (y2[0] + y2[1]) / 2
)

x_new = (
    (2 * x_mean[0] - x2[2]),
    (2 * x_mean[1] - y2[2])
)

print(f"Пробне відображення альфа = 1: x_нов = {x_new}")
print(f"f{x_new} = {func(*x_new)}")
print(f"Залишимо x_5 = {tuple(x_new)}")

x_5 = x_new

# print(f"Відображення гамма = 2: x_4 = {x_5}")
# print(f"f{x_5} = {func(*x_5)}")


print("1 | 2 | 3")
print("1 | 4 | 3")
print("1 | 4 | 5")
print("_" * 50)

x3 = [5, 3, 3]
y3 = [4, 4, 2]

x3_array = np.array(list(zip(x3, y3)))

print("Ітерація 3. Редукція")
for el in zip(x3, y3):
    if el == min(zip(x3, y3), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x3, y3), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

# # reduction related to (3, 4) - 2

x_6 = (x3_array[0] + x3_array[1]) / 2
x_7 = (x3_array[1] + x3_array[2]) / 2

print(f"x_6 = {tuple(x_6)}")
print(f"x_7 = {tuple(x_7)}")
print()

print("1 | 2 | 3")
print("1 | 4 | 3")
print("1 | 4 | 5")
print("_________")
print("6 | 4 | 7")

print("_" * 50)


print("Ітерація 4")

x4 = [4, 3, 3]
y4 = [4, 4, 3]
x4_array = np.array(list(zip(x4, y4)))

for el in zip(x4, y4):
    if el == min(zip(x4, y4), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x4, y4), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

x_mean = (x4_array[2] + x4_array[1]) / 2

x_new = 2 * x_mean - x4_array[0]

print(f"Пробне відображення альфа = 1: x_нов = {tuple(x_new)}")
print(f"f{x_new} = {func(*x_new)}")

x_8 = (3 * x_mean / 2) - 2 * x_6

print(f"Відображення гамма = 2: x_8 = {tuple(x_8)}")
print(f"f{tuple(x_8)} = {func(*x_8)}")
print(f"Залишимо x_8 = {tuple(x_new)}")

x_8 = x_new


print("1 | 2 | 3")
print("1 | 4 | 3")
print("1 | 4 | 5")
print("_________")
print("6 | 4 | 7")
print("8 | 4 | 7")

print("_" * 50)

print("Ітерація 5")

x5 = [2, 3, 3]
y5 = [3, 4, 3]

x5_array = np.array(list(zip(x5, y5)))

for el in zip(x5, y5):
    if el == min(zip(x5, y5), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x5, y5), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

x_mean = (x5_array[0] + x5_array[1]) / 2
x_new = 2 * x_mean - x5_array[2]

print(f"Пробне відображення альфа = 1: x_нов = {tuple(x_new)}")
print(f"f{x_new} = {func(*x_new)}")

x_9 = (3 * x_mean / 2) - 2 * x_7

print(f"Відображення гамма = 2: x_9 = {tuple(x_9)}")
print(f"f{tuple(x_9)} = {func(*x_9)}")
print(f"Залишимо x_9 = {tuple(x_new)}")

x_9 = x_new


print("1 | 2 | 3")
print("1 | 4 | 3")
print("1 | 4 | 5")
print("_________")
print("6 | 4 | 7")
print("8 | 4 | 7")
print("8 | 4 | 9")

print("_" * 50)
print("Ітерація 6. Редукція")

x6 = [2, 3, 2]
y6 = [3, 4, 4]

x6_array = np.array(list(zip(x6, y6)))

for el in zip(x6, y6):
    if el == min(zip(x6, y6), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x6, y6), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

# reduction
x_10 = (x_9 + x_4) / 2
x_11 = (x_8 + x_9) / 2

print(f"x_10 = {x_10}")
print(f"x_11 = {x_11}")

print("1 | 2 | 3")
print("1 | 4 | 3")
print("1 | 4 | 5")
print("_________")
print("6 | 4 | 7")
print("8 | 4 | 7")
print("8 | 4 | 9")
print("11 | 10 | 9")
print("_"*50)

# FINAL
print("Ітерація 7.")

x7 = [2, 2.5, 2]
y7 = [3.5, 4, 4]

for el in zip(x7, y7):
    if el == min(zip(x7, y7), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    l")
    elif el == max(zip(x7, y7), key=lambda x: func(x[0], x[1])):
        print(f"f{el} = {func(*el)}    -    h")
    else:
        print(f"f{el} = {func(*el)}    -    g")

x7_array = np.array(list(zip(x7, y7)))

print("_"*50)

x_mean = (x7_array[0] + x7_array[1] + x7_array[2]) / 3

print(f"x_сер = {tuple(map(lambda x: round(x, 3), x_mean))}")

x_related = [
    (func(*x7_array[0]) - func(*x_mean)) ** 2,
    (func(*x7_array[1]) - func(*x_mean)) ** 2,
    (func(*x7_array[2]) - func(*x_mean)) ** 2
]

print(f"(f(x_11) - f(x_ceр)) ^ 2 = {round(x_related[2], 3)}\n"
      f"(f(x_10) - f(x_ceр)) ^ 2 = {round(x_related[1], 3)}\n"
      f"(f(x_9) - f(x_ceр)) ^ 2 = {round(x_related[0], 3)}\n")

criteria = ((x_related[0] + x_related[1] + x_related[2]) / 3) ** (1 / 2)

print(round(criteria, 3))


# Построение многоугольника
plt.fill(x, y, color='lightblue', label="Iteration 1")
plt.plot(x, y, color='blue')
plt.fill(x2, y2, color='yellow', label="Iteration 2")
plt.plot(x2, y2, color='lightblue')
plt.fill(x3, y3, color='grey', label="Iteration 3")
plt.plot(x3, y3, color='black')
plt.fill(x4, y4, color='orange', label="Iteration 4")
plt.plot(x4, y4, color='red')
plt.fill(x5, y5, color='blue', label="Iteration 5")
plt.plot(x5, y5, color='black')
plt.fill(x6, y6, color='green', label="Iteration 6")
plt.plot(x6, y6, color='lightgreen')
plt.fill(x7, y7, color='red', label="Iteration 7")
plt.plot(x7, y7, color='black')

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.legend()
plt.xlabel('x1')
plt.ylabel('x2')
plt.savefig('myplot.png', dpi=300)
plt.show()
