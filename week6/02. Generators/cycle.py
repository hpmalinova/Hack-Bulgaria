
def cycle(iterable):
    while True:
        for x in iterable:
            yield x


# endless = cycle([1, 5, 6, 7])

# for i in endless:
    # print(i)
