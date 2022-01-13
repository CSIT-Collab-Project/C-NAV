from Backend.Nodes.Node import Node


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node):

        super(DoorNode, self).__init__(connections)

        self.door_num = num

        self.closest_node = closest

    async def connect_to_network(self):
        [await connection.add_connections([self]) for connection in self.connections]
