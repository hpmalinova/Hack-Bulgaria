# Implement deep_find_all(data, key)
# which finds the given key in the data
# and returns array of the found values.
from collections.abc import Iterable


# BFS
def deep_find_all_bfs(data, key_to_search):
    queue = list(data.items())
    result = []

    while queue:
        key, value = queue.pop(0)

        if key == key_to_search:
            result.append(value)

        if isinstance(value, dict):
            for value_item in list(value.items()):
                queue.append(value_item)

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for value_item in value:
                for item in list(value_item.items()):
                    queue.append(item)

    return result


# DFS
def deep_find_all_dfs(data, key_to_search, result=None):
    if result is None:
        result = []

    for key, value in data.items():
        if key == key_to_search:
            result.append(value)

        if isinstance(value, dict):
            deep_find_all_dfs(value, key_to_search, result)

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for dictionary in value:
                deep_find_all_dfs(dictionary, key_to_search, result)

    return result
