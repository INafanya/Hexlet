def diff(angle_one, angle_two):
    result = abs(angle_one % 360 - angle_two % 360)
    print(f"Остаток_1: {angle_one % 360}")
    print(f"Остаток_2: {angle_two % 360}")
    if result > 180:

        result = 360 - result
    return result


print(diff(0, 45))
print(diff(0, 180))
print(diff(0, 190))
print(diff(120, 280))
print(diff(720, 0))