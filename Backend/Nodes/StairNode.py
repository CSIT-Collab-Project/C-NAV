from Backend.Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, upstairs: Node, downstairs: Node):
        super(StairNode, self).__init__(connections)
        self.upstairs = upstairs
        self.downstairs = downstairs
