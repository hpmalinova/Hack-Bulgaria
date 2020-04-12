def chain(iterable_one, iterable_two):
    for x in iterable_one:
        yield x

    for x in iterable_two:
        yield x
