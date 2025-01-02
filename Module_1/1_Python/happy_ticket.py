def diff(ticket_number: str) -> bool:
    le = int(len(ticket_number) / 2)
    first_part_sum, second_part_sum, i = 0, 0, 0
    while i < le:
        first_part_sum += int(ticket_number[i])
        second_part_sum += int(ticket_number[i + le])
        i += 1
    return first_part_sum == second_part_sum


print(diff())