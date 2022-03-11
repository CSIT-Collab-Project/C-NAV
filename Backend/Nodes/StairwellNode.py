from Backend.Nodes.Node import Node
from Backend.Logger.logger import logger

class StairwellNode(Node):
    def __init__(self, stairwell, rooms, coords=(0, 0)):
        logger.info(f'StairwellNode({stairwell}, {rooms}, {coords})')
        self.stairwell = stairwell
        self.rooms = rooms
        self.rooms.append(stairwell)
        coords = self.stairwell.coordinates
        super(StairwellNode, self).__init__(self.rooms, coords)
