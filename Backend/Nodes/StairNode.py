from Backend.Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, upstairs: Node, downstairs: Node,
                 n: Node = None,
                 s: Node = None,
                 e: Node = None,
                 w: Node = None):
        super(StairNode, self).__init__(connections)
        self.upstairs = upstairs
        self.downstairs = downstairs
        self.node_map = {n: 'n', s: 's', e: 'e', w: 'w'}
