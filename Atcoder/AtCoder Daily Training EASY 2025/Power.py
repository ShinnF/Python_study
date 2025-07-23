def power(a_value, b_value):
    return a_value ** b_value

a_value, b_value = map(int, input().split())

print(power(a_value, b_value))