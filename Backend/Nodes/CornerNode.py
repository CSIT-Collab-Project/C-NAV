import path
import sys

sys.path.append(path.Path(__file__).abspath().parent.parent.parent)
from Backend.Nodes.Node import Node
from Backend.Logger.logger import logger

class CornerNode(Node):
    def __init__(self, connections, name,
                 coords=(0, 0),
                 n: Node = None,
                 s: Node = None,
                 e: Node = None,
                 w: Node = None,
                 ):

        super(CornerNode, self).__init__(connections, coords)

        logger.info(f'CornerNode({connections}, {name}, {coords}, {n}, {s}, {e}, {w})')

        self.set_name(name)

        self.north_node = n

        self.south_node = s

        self.east_node = e

        self.west_node = w

        self.turn_map = {'n': n, 's': s, 'e': e, 'w': w}

        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}

        self.door_map = {}

    async def get_turns(self) -> list:
        logger.info('get_turns()')
        return [turn for turn in ['n', 's', 'e', 'w'] if not self.turn_map[turn]]

    async def get_node_to(self, direction: str) -> Node:
        logger.info(f'get_node_to({direction})')
        return self.turn_map[direction]

    async def add_directions(self, n, e, s, w):
        logger.info(f'add_directions({n}, {e}, {s}, {w})')
        nodes = []

        if isinstance(n, list):
            for node in n:
                self.node_map[node] = 'n'
                nodes.append(node)
        else:
            self.node_map[n] = 'n'
            nodes.append(n)

        if isinstance(e, list):
            for node in e:
                self.node_map[node] = 'e'
                nodes.append(node)
        else:
            self.node_map[e] = 'e'
            nodes.append(e)

        if isinstance(s, list):
            for node in s:
                self.node_map[node] = 's'
                nodes.append(node)
        else:
            self.node_map[s] = 's'
            nodes.append(s)

        if isinstance(w, list):
            for node in w:
                self.node_map[node] = 'w'
                nodes.append(node)
        else:
            self.node_map[w] = 'w'
            nodes.append(w)

        await self.add_connections(nodes)
