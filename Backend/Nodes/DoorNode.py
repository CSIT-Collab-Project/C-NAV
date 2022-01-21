from __future__ import annotations
from Backend.Nodes.Node import Node
from Backend.Nodes.CornerNode import CornerNode


async def create_door(connections: list, num: int, closest: Node, directions):
    door = DoorNode(connections, num, closest)
    await connect_to_network(door, directions)
    return door


async def connect_to_network(node, directions):
    opp_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    for i in range(len(node.connections)):
        await node.connections[i].add_connections([node])
        if isinstance(node, DoorNode):
            node.connections[i].node_map[node] = directions[i]
            node.node_map[node.connections[i]] = opp_directions[directions[i]]


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node, door_side: str):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest
        self.node_map = {}
        self.door_side = door_side

    async def set_info(self, connections, num, closest, directions):
        self.connections = connections
        self.door_num = num
        self.closest_node = closest
        await connect_to_network(self, directions)

    async def in_same_hall(self, checkNode):
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