def compress(iterable, mask):
    for x, y in zip(iterable, mask):
        if y:
            yield x
