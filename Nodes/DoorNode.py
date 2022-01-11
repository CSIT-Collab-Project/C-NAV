from Nodes.Node import Node


class DoorNode(Node):
    def __init__(self, connections: list, num: int, closest: Node):
        super(DoorNode, self).__init__(connections)
        self.door_num = num
        self.closest_node = closest

    # we don't need get_door_num or get_closest_node. We can just use DoorNode.door_num and DoorNode.closest_node

