from __future__ import annotations


class Node:
    def __init__(self, connections: list, coords: tuple = (0, 0)):
        self.connections = connections
        self.coordinates = coords
        self.name = "Default Name"

    async def is_connected_to(self, target_node: Node) -> bool:
        return True if target_node in self.connections else False

    async def add_connections(self, new_nodes: list):
        self.connections.extend(new_nodes)

    def set_name(self, new_name: str):
        self.name = new_name