# задание 1
def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"
print(to_float(52))
print(to_float(-4))
print(to_float(True))
print(to_float('День'))
# задание 2
def avg_5(a, b, c, d):
    return round((a + b + c + d) / 4, 5)
print(avg_5(3, 8, 5, 7))
# задание 3
def mul_to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res
print(mul_to_int(4, 4))
# задание 4
from math import pi
print ((3 * 19.32 / (4 * pi)) ** (1/3))
