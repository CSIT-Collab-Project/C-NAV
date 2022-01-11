from Nodes.Node import Node


class StairNode(Node):
    def __init__(self, connections: list, u: Node, d: Node):
        super(StairNode, self).__init__(connections)
        self.upstairs = u
        self.downstairs = d

        # we don't need get_up or get_down methods here. We can just use StairNode.upstairs and StairNode.downstairs
