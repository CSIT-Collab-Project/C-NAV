def get_turn_direction(facing, from_node, to_node):
    direct_order = {'n': 1, 'e': 1, 's': 2, 'w': 2}
    to_direction = from_node.turn_map[to_node]
    if direct_order[facing] - direct_order[to_direction] == 0:
        return 'left'
    else:
        return 'right'


def go_to(start, end, direction_list=[]):
    if start.get_door_num() == end.get_door_num():
        return 'Found'

    for node in start.get_door_num().get_door_num():
        go_to(node, end)


if __name__ == '__main__':
    print("TODO")
