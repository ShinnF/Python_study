def sum_list(ln):
    sum_value = 0
    for value in ln:
        sum_value += value
    return sum_value

print(sum_list([10, 20, 30]) == 60)
print(sum_list([-1, 2, -3, 4, -5]) == -3)