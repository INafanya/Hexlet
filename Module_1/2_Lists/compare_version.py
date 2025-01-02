def compare_version(version1, version2):
    v1_1, v1_2 = version1.split('.')
    v2_1, v2_2 = version2.split('.')
    if int(v1_1) == int(v2_1):
        if int(v1_2) == int(v2_2):
            return 0
        elif int(v1_2) > int(v2_2):
            return 1
        else:
            return -1
    elif int(v1_1) > int(v2_1):
        return 1
    else:
        return -1



# print(compare_version("0.1", "0.2"))  # -1
# print(compare_version("0.2", "0.1"))  # 1
# print(compare_version("4.2", "4.2"))  # 0
# print(compare_version('0.2', '0.12')) # -1
# print(compare_version('3.2', '4.12')) # -1
print(compare_version('3.2', '2.12')) # 1