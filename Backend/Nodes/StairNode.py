from Backend.Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, door_side: str, name: str, upstairs: Node = None, downstairs: Node = None,
                 n: Node = None,
                 s: Node = None,
                 e: Node = None,
                 w: Node = None):
        super(StairNode, self).__init__(connections)
        self.set_name(name)
        self.upstairs = upstairs
        self.downstairs = downstairs
        self.north_node = n
        self.east_node = e
        self.south_node = s
        self.west_node = w
        self.door_side = door_side
        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}

    async def add_directions(self, n, e, s, w, u, d):
        self.north_node = n

        self.east_node = e

        self.south_node = s

        self.west_node = w

        self.upstairs = u
        self.downstairs = d

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

        self.node_map[u] = 'u'
        nodes.append(u)
        self.node_map[d] = 'd'
        nodes.append(d)

        await self.add_connections(nodes)

