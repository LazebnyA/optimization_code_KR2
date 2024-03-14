import math


def func(x1, x2):
    return round((x1 - 2) ** 2 + 4 * x2 ** 2, 3)


def generate_second_half(point, growth_val_x2):
    second_half = [
        (
            point[1] + growth_val_x2,
            func(point[0], point[0] + growth_val_x2)
        ),
        (
            point[1] - growth_val_x2,
            func(point[0], point[0] - growth_val_x2)
        )
    ]

    return list(map(lambda x: tuple(map(lambda y: round(y, 3), x)), second_half))


base_point = (6, 9)
growth_value = (0.6, 0.8)

endpoint = 3

# 1 Iteration

# Exploratory search

prev_base_point = base_point
prev_prev_base_point = prev_base_point

cur_base_lst = []

for _ in range(endpoint):

    search_lst = [
        (
            base_point[0] + growth_value[0],
            func(base_point[0] + growth_value[0], base_point[1])
        ),
        (
            base_point[0] - growth_value[0],
            func(base_point[0] - growth_value[0], base_point[1])
        )
    ]

    search_lst = list(map(lambda x: tuple(map(lambda y: round(y, 3), x)), search_lst))
    basis_func = func(*base_point)

    print(f"f{base_point} = {basis_func}")

    current_base_point = base_point

    for el in search_lst:
        current_point = el[0], current_base_point[1]
        is_success = func(*current_point) < basis_func
        is_min = func(*current_point) < func(*current_base_point)
        print(f"x_1 = {el[0]},     f{current_point} = {func(*current_point)}.       {is_success}")
        if is_min:
            current_base_point = (el[0], current_base_point[1])

    second_hf = generate_second_half(current_base_point, growth_value[1])
    for el in second_hf:
        current_point = current_base_point[0], el[0]
        is_success = func(*current_point) < basis_func
        is_min = func(*current_point) < func(*current_base_point)
        print(f"x_2 = {el[0]},     f{current_point} = {func(*current_point)}.       {is_success}")
        if is_min:
            current_base_point = (current_base_point[0], el[0])

    cur_base_lst.append(current_base_point)

    print("Current base point: ", current_base_point)
    print(f"f{current_base_point} = {func(*current_base_point)}")
    print("Base point: ", prev_base_point)
    print(f"f{prev_base_point} = {func(*prev_base_point)}")

    x_p = (round((2 * current_base_point[0]) - prev_base_point[0], 3),
           round((2 * current_base_point[1]) - prev_base_point[1], 3))

    print("x_p = ", x_p)
    print("f(x_p) = ", func(*x_p))

    if func(*current_base_point) > func(*prev_base_point):
        print(2)
    else:
        prev_base_point = current_base_point
        prev_prev_base_point = base_point
        base_point = x_p

    print("_" * 50)




norm = math.sqrt(growth_value[0] ** 2 + growth_value[1] ** 2)

print(norm)

print("_" * 50)

top_value = math.sqrt((cur_base_lst[-1][0] - cur_base_lst[-2][0]) ** 2 + (cur_base_lst[-1][1] - cur_base_lst[-2][1]) ** 2)
bot_value = math.sqrt(cur_base_lst[-1][0] ** 2 + cur_base_lst[-1][1] ** 2)

print(round(top_value, 3))
print(round(bot_value, 3))

print(round(top_value / bot_value, 3))

func_val_3 = func(*cur_base_lst[-1])
func_val_2 = func(*cur_base_lst[-2])

print("_" * 50)

top_value = abs(func_val_3 - func_val_2)
bot_value = abs(func_val_2)

print(round(top_value, 3))
print(round(bot_value, 3))

print(round(top_value / bot_value, 3))

