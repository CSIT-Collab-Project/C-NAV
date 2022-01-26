from Backend.Nodes.Node import Node


class CornerNode(Node):
    def __init__(self, connections, name,
                 n: Node = None,
                 s: Node = None,
                 e: Node = None,
                 w: Node = None
                 ):

        super(CornerNode, self).__init__(connections)

        self.set_name(name)

        self.north_node = n

        self.south_node = s

        self.east_node = e

        self.west_node = w

        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}

        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}

        self.door_map = {}

    async def get_turns(self) -> list:
        return [turn for turn in ['n', 's', 'e', 'w'] if not self.turn_map[turn]]

    async def get_node_to(self, direction: str) -> Node:
        return self.turn_map[direction]

    async def add_directions(self, n: Node, e: Node, s: Node, w: Node):
        self.north_node = n

        self.east_node = e

        self.south_node = s

        self.west_node = w
        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}
        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}
        await self.add_connections([n, s, e, w])
