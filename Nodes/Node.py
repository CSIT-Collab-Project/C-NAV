from __future__ import annotations


class Node:
    def __init__(self, connections: list):
        self.connections = connections

    # we don't need a get_connections method. Node.connections will have the same effect without performance impact

    async def is_connected_to(self, other_node: Node) -> bool:
        if other_node in self.connections:
            return True

    # we don't need return false here

    async def add_connections(self, new_nodes: list):
        self.connections.extend(new_nodes)

    async def get_door_num(self) -> int:
        pass

    # not sure what this is
