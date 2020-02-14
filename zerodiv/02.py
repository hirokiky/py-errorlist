def avg(iterable):
    return sum(iterable) / len(iterable)


avg([0, 1, 2, 3])  # OK
avg([])  # NG
