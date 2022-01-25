from Backend.Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, door_side: str, upstairs: Node = None, downstairs: Node = None,
                 n: Node = None,
                 s: Node = None,
                 e: Node = None,
                 w: Node = None):
        super(StairNode, self).__init__(connections)
        self.upstairs = upstairs
        self.downstairs = downstairs
        self.north_node = n
        self.east_node = e
        self.south_node = s
        self.west_node = w
        self.door_side = door_side
        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}
        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}

    async def add_directions(self, n: Node, e: Node, s: Node, w: Node, u: Node, d: Node):
        self.north_node = n

        self.east_node = e

        self.south_node = s

        self.west_node = w

        self.upstairs = u
        self.downstairs = d

        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w, 'u': u, 'd': d}
        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w', u: 'u', d: 'd'}
        await self.add_connections([n, s, e, w, u, d])
