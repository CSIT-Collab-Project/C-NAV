from Backend.Nodes.Node import Node


async def create_door(connections: list, num: int, closest: Node):
    door = DoorNode(connections, num, closest)
    await connect_to_network(door)
    return door


async def connect_to_network(node, directions):
    for i in range(len(node.connections)):
        await node.connections[i].add_connections([node])
        if isinstance(node, DoorNode):
            node.connections[i].node_map[node] = directions[i]


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest

    async def set_info(self, connections, num, closest, directions):
        self.connections = connections
        self.door_num = num
        self.closest_node = closest
        await connect_to_network(self, directions)



