from __future__ import annotations


class Node:
    def __init__(self, connections: list):
        self.connections = connections

    async def is_connected_to(self, target_node: Node) -> bool:
        if target_node in self.connections:
            return True

    async def add_connections(self, new_nodes: list):
        self.connections.extend(new_nodes)
