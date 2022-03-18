from __future__ import annotations
import path
import sys

sys.path.append(path.Path(__file__).abspath().parent.parent.parent)
from Backend.Nodes.Node import Node
from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.StairwellNode import StairwellNode
from Backend.Logger.logger import logger


async def create_door(connections: list, num: int, closest: Node, directions):
    logger.info(f'create door({connections}, {num}, {closest}, {directions})')
    door = DoorNode(connections, num, closest)
    await connect_to_network(door, directions)
    return door


async def connect_to_network(node, directions):
    logger.info(f'connect_to_network({node}, {directions})')
    opp_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    for i in range(len(node.connections)):
        await node.connections[i].add_connections([node])
        # logger.info(f"Connecting {node.connections[i].name} to {node.name}")
        if isinstance(node, DoorNode) and not isinstance(node.connections[i], StairwellNode):
            node.connections[i].node_map[node] = directions[i]
            node.node_map[node.connections[i]] = opp_directions[directions[i]]


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node, door_side: str, coords=(0, 0)):
        super(DoorNode, self).__init__(connections, coords)
        logger.info(f'DoorNode({connections}, {num}, {closest}, {door_side}, {coords})')
        self.door_num = num
        self.closest_node = closest
        self.node_map = {}
        self.door_side = door_side

    async def set_info(self, connections, num, closest, directions):
        logger.info(f'set_info({connections}, {num}, {closest}, {directions})')
        self.connections = connections
        self.door_num = num
        self.closest_node = closest
        await connect_to_network(self, directions)

    async def in_same_hall(self, checkNode):
        logger.info(f'in_same_hall({checkNode})')
        self_corner_list = set()
        check_corner_list = set()
        for connection in self.connections:
            if isinstance(connection, CornerNode):
                self_corner_list.add(connection)

        for connection in checkNode.connections:
            if isinstance(connection, CornerNode):
                check_corner_list.add(connection)

        if self_corner_list == check_corner_list:
            return True
        return False
