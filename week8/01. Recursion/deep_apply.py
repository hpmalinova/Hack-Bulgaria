# Implement deep_apply(func, data)
# which applies the given func to all keys
# from the given data.
from collections.abc import Iterable


def some_func(x):
    return x + '!'


# DFS
def deep_apply_dfs(func, data):
    for key, value in data.items():
        if isinstance(value, dict):
            deep_apply_dfs(func, value)

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for dictionary in value:
                deep_apply_dfs(func, dictionary)

        else:
            data[key] = some_func(value)

    return data
