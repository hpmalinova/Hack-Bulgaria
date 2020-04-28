# Implement schema_validator(schema: List, data: Dict)
# which should assert that the given data keys
# are as the given schema.

# - 'data' is valid only if the given keys
#   from the schema are found in the data
# - If the schema has more or less keys, data is invalid.
# - If there is a missmatch in the schema and the data keys,
#   data is invalid.
# - schema_validator should work for N levels of nesting.
# from collections.abc import Iterable


def schema_validator(schema, data):
    if not isinstance(data, dict):
        raise TypeError('Data should be of type dictionary')
    if not isinstance(schema, list):
        raise TypeError('Schema should be of type list')

    return flatten_list(schema) == flatten_dict(data)


def flatten_list(my_list):
    result = []

    for element in my_list:
        if isinstance(element, list):
            result += flatten_list(element)
        else:
            result.append(element)

    return result


def flatten_dict(my_dict):
    result = []

    for key, value in my_dict.items():
        result.append(key)
        if isinstance(value, dict):
            result += flatten_dict(value)

    return result
