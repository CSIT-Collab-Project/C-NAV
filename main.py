from __future__ import annotations


class LocationNode:
    def __init__(self, connections: list):
        self.connections = connections

    def get_connections(self) -> list:
        return self.connections

    def is_connected_to(self, other_node: LocationNode) -> bool:
        if other_node in self.connections:
            return True
        return False

    def add_connections(self, new_nodes: list):
        self.connections.extend(new_nodes)

    def get_door_num(self):
        return None


class CornerNode(LocationNode):
    def __init__(self, connections,
                 n: LocationNode = None,
                 s: LocationNode = None,
                 e: LocationNode = None,
                 w: LocationNode = None):
        super(CornerNode, self).__init__(connections)
        self.north_node = n
        self.south_node = s
        self.east_node = e
        self.west_node = w
        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}

    def get_turns(self) -> list:
        available_turns = ['n', 's', 'e', 'w']
        for turn in available_turns:
            if not self.turn_map[turn]:
                available_turns.remove(turn)
        return available_turns

    def get_node_to(self, direction: str) -> LocationNode:
        return self.turn_map[direction]

    def add_directions(self, n: LocationNode, s: LocationNode, e: LocationNode, w: LocationNode):
        self.north_node = n
        self.east_node = e
        self.south_node = s
        self.west_node = w
        self.add_connections([n, s, e, w])


class StairNode(LocationNode):
    def __init__(self, connections: list, u: LocationNode, d: LocationNode):
        super(StairNode, self).__init__(connections)
        self.upstairs = u
        self.downstairs = d

    def get_up(self) -> LocationNode:
        return self.upstairs

    def get_down(self) -> LocationNode:
        return self.downstairs


class DoorNode(LocationNode):
    def __init__(self, connections: list, num: int, closest: LocationNode):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest

    def get_door_num(self) -> int:
        return self.door_num

    def get_closest_node(self) -> LocationNode:
        return self.closest_node


def get_turn_direction(facing, from_node, to_node):
    direct_order = ['n', 'e', 's', 'w']


def go_to(start, end, direction_list=[]):
    if start.get_door_num() == end.get_door_num():
        return 'Found'

    for node in start.get_door_num().get_door_num():
        go_to(node, end)


if __name__ == '__main__':
    print("TODO")
