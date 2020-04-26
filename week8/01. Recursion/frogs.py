import copy


def init_lake(frogs_count_in_direction):
    lake = '>' * frogs_count_in_direction + '_' + '<' * frogs_count_in_direction
    return list(lake)


def final_lake(frogs_count_in_direction):
    lake = '<' * frogs_count_in_direction + '_' + '>' * frogs_count_in_direction
    return list(lake)


def move_frog(frog_position, lake):  # position of frog in the lake, lake = [>>>_<<<]
    position = {'>': 1, '_': 0, '<': -1}
    if lake[frog_position] != '_':
        for i in [1, 2]:
            new_position = i * position[lake[frog_position]] + frog_position

            if valid_position(new_position, lake) and lake[new_position] == '_':
                lake[new_position] = lake[frog_position]
                lake[frog_position] = '_'
                return lake

    return False


def all_moves_for_turn(lake):
    rock_position = lake.index('_')
    possible_lakes = []

    for i in [-2, -1, 1, 2]:
        frog_in_lake = rock_position + i

        if valid_position(frog_in_lake, lake):
            new_lake = move_frog(frog_in_lake, copy.deepcopy(lake))

            if new_lake is not False:
                possible_lakes.append(new_lake)

    return possible_lakes


def valid_position(position, lake):
    return position >= 0 and position < len(lake)


def game(lily_pads):
    assert lily_pads % 2 != 0, 'Lily-pads should be odd number'
    start_lake = init_lake(lily_pads // 2)
    final = final_lake(lily_pads // 2)

    print('path:', dfs(start_lake, final))


def dfs(lake, final_lake, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    path.append(lake)

    if lake == final_lake:
        return path

    visited.append(lake)

    for possible_lake in all_moves_for_turn(copy.deepcopy(lake)):
        if possible_lake not in visited:
            path = dfs(possible_lake, final_lake, visited, path)
            if final_lake in path:
                return path

    path = path[:-1]
    return path


if __name__ == '__main__':
    game(5)
