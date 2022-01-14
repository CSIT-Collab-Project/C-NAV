from Backend.Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, u: Node, d: Node):
        super(StairNode, self).__init__(connections)
        self.upstairs = u
        self.downstairs = d
