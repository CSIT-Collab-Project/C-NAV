def get_turn_direction(facing, from_node, to_node):
    direct_order = ['n', 'e', 's', 'w']


def go_to(start, end, direction_list=[]):
    if start.get_door_num() == end.get_door_num():
        return 'Found'

    for node in start.get_door_num().get_door_num():
        go_to(node, end)


if __name__ == '__main__':
    print("TODO")
