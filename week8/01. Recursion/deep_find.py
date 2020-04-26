# Implement deep_find(data, key)
# which finds the given key in the data and returns it's value.
from collections.abc import Iterable


# BFS
def deep_find_bfs(data, key_to_search):
    queue = list(data.items())

    while queue:
        key, value = queue.pop(0)

        if key == key_to_search:
            return value

        if isinstance(value, dict):
            for value_item in list(value.items()):
                queue.append(value_item)

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for value_item in value:
                for item in list(value_item.items()):
                    queue.append(item)


# DFS
def deep_find_dfs(data, key_to_search):
    for key, value in data.items():
        if key == key_to_search:
            return value

        if isinstance(value, dict):
            found_value = deep_find_dfs(value, key_to_search)
            if found_value:
                return found_value

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for dictionary in value:
                found_value = deep_find_dfs(dictionary, key_to_search)
                if found_value:
                    return found_value
