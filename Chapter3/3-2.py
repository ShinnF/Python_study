def bmi(height, weight):
    return weight / (height / 100.0) ** 2
print(bmi(188.0, 104.0))