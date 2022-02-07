from Backend.Nodes.Node import Node


class StairwellNode(Node):
    def __init__(self, stairwell, rooms):
        self.stairwell = stairwell
        self.rooms = rooms
        self.rooms.append(stairwell)
        super(StairwellNode, self).__init__(self.rooms)
