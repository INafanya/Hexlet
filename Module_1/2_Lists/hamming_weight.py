def hamming_weight(num: int) -> int:
    num_bin = bin(num)[2:]
    weight = 0
    for i in num_bin:
        weight += int(i)
    return weight


hamming_weight(1) # 1
hamming_weight(5) # 2
hamming_weight(10) # 2
hamming_weight(101) # 4
hamming_weight(12345) # 6