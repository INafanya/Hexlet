def get_super_series_winner(scores):
    score_canada = 0
    score_ussr = 0
    for score in scores:
        if score[0] > score[1]:
            score_canada += 1
        elif score[0] < score[1]:
            score_ussr += 1
    if score_ussr > score_canada:
        return 'ussr'
    elif score_canada > score_ussr:
        return 'canada'
    else:
        return None


scores = [
            [3, 7],
            [4, 1],
            [4, 4],
            [3, 5],
            [4, 5],
            [3, 2],
            [4, 3],
            [6, 5],
        ]

print(get_super_series_winner(scores)) # 'canada'