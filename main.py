from __future__ import annotations


class LocationNode:
    def __init__(self, connections: list):
        self.connections = connections

    def get_connections(self) -> list:
        return self.connections

    def is_connected_to(self, target_node: LocationNode) -> bool:
        if target_node in self.connections:
            return True
        return False


class CornerNode(LocationNode):
    def __init__(self, connections,
                 north: LocationNode,
                 south: LocationNode,
                 east: LocationNode,
                 west: LocationNode):
        super(CornerNode, self).__init__(connections)
        self.north_node = north
        self.south_node = south
        self.east_node = east
        self.west_node = west
        self.turn_map = {'n': north, 's': south, 'e': east, 'w': west}

    def get_turns(self) -> list:
        return [turn for turn in ['n', 's', 'e', 'w'] if self.turn_map[turn]]

    def get_node_to(self, direction: str) -> LocationNode:
        return self.turn_map[direction]


class StairNode(LocationNode):
    def __init__(self, connections: list, upstairs: LocationNode, downstairs: LocationNode):
        super(StairNode, self).__init__(connections)
        self.upstairs = upstairs
        self.downstairs = downstairs

    def get_up(self) -> LocationNode:
        return self.upstairs

    def get_down(self) -> LocationNode:
        return self.downstairs


class DoorNode(LocationNode):
    def __init__(self, connections: list, door_number: int, closest: LocationNode):
        super(DoorNode, self).__init__(connections)
        self.door_number = door_number
        self.closest_node = closest

    def get_door_number(self) -> int:
        return self.door_number

    def get_closest_node(self) -> LocationNode:
        return self.closest_node


if __name__ == '__main__':
    print("TODO")
