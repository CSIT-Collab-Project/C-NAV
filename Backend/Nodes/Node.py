from __future__ import annotations

import path
import sys

sys.path.append(path.Path(__file__).abspath().parent.parent.parent)
from Backend.Logger.logger import logger


class Node:
    def __init__(self, connections: list, coords: tuple = (0, 0)):
        # logger.info(f'Node({connections}, {coords})')
        self.connections = connections
        self.coordinates = coords
        self.name = "0Default Name"

    async def is_connected_to(self, target_node: Node) -> bool:
        # logger.info(f'is_connected_to({target_node})')
        return True if target_node in self.connections else False

    async def add_connections(self, new_nodes: list):
        # logger.info(f'add_connections({new_nodes})')
        self.connections.extend(new_nodes)

    def set_name(self, new_name: str):
        # logger.info(f'set_name({new_name})')
        self.name = new_name
