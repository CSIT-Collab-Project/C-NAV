from __future__ import annotations
from Backend.Nodes.Node import Node


async def create_door(connections: list, num: int, closest: Node) -> DoorNode:
    door = DoorNode(connections, num, closest)
    await connect_to_network(door)
    return door


async def connect_to_network(node):
    [await connection.add_connections([node]) for connection in node.connections]


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest

    async def set_info(self, connections, num, closest):
        self.connections = connections
        self.door_num = num
        self.closest_node = closest
        await connect_to_network(self)


