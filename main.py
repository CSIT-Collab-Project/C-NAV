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


class CornerNode(LocationNode):
    def __init__(self, connections,
                 n: LocationNode,
                 s: LocationNode,
                 e: LocationNode,
                 w: LocationNode):
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


if __name__ == '__main__':
    print("TODO")
