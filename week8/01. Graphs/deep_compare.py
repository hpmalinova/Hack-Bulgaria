# Implement deep_compare(obj1, obj2)
# where obj1 and obj2 can be dict or iterable
# and compares the given objects.


# DFS
def deep_compare_dfs(obj1, obj2):
    def compare_dicts(dict1, dict2):
        if dict1.keys() != dict2.keys():
            return False
        for key in list(dict1.keys()):
            if not deep_compare_dfs(dict1[key], dict2[key]):
                return False
        return True

    if isinstance(obj1, dict) and isinstance(obj2, dict):
        return compare_dicts(obj1, obj2)

    if len(obj1) != len(obj2):
        return False

    for elem1, elem2 in zip(obj1, obj2):
        if type(elem1) != type(elem2):
            return False

        if elem1 != elem2:
            return False

    return True
