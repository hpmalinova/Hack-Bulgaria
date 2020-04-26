# Implement deep_update(data, key, val)
# which updates every occurance of the given key
# in the data with val.
from collections.abc import Iterable


# DFS
def deep_update_dfs(data, key_to_search, new_value):
    for key, value in data.items():
        if key == key_to_search:
            data[key] = new_value

        if isinstance(value, dict):
            deep_update_dfs(value, key_to_search, new_value)

        elif isinstance(value, Iterable) and not isinstance(value, str):
            for dictionary in value:
                deep_update_dfs(dictionary, key_to_search, new_value)

    return data
