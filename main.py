class LocationNode:
    def __init__(self, connections):
        self.connections = connections

    def get_connections(self):
        return self.connections

    def is_connected_to(self, other_node):
        if other_node in self.connections:
            return True
        return False


class CornerNode(LocationNode):
    def __init__(self, connections, n, s, e, w):
        super(CornerNode, self).__init__(connections)
        self.north_node = n
        self.south_node = s
        self.east_node = e
        self.west_node = w
        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}

    def get_turns(self):
        available_turns = ['n', 's', 'e', 'w']
        for turn in available_turns:
            if not self.turn_map[turn]:
                available_turns.remove(turn)

    def get_node_to(self, direction):
        return self.turn_map[direction]


class StairNode(LocationNode):
    def __init__(self, connections, u, d):
        super(StairNode, self).__init__(connections)
        self.upstairs = u
        self.downstairs = d

    def get_up(self):
        return self.upstairs

    def get_down(self):
        return self.downstairs


class DoorNode(LocationNode):
    def __init__(self, connections, num, closest):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest

    def get_door_num(self):
        return self.door_num

    def get_closest_node(self):
        return self.closest_node


if __name__ == '__main__':
    print("TODO")
