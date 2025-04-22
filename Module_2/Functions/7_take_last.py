def run(text):
    # BEGIN (write your solution here)
    # take_last = lambda text, count_sumb: text[::-1][:count_sumb]
    def take_last(text, count_sumb):
        if not text or len(text) < count_sumb:
            return None
        return text[:count_sumb][::-1]

    return take_last(text, 4)


print(run('dfgggfg'))