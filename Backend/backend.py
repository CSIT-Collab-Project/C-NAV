import asyncio

from Node_Config.nodes import *


async def get_turn_direction(facing, from_node, to_node):
    direct_order = {'n': 1, 'e': 1, 's': 2, 'w': 2}

    try:
        to_direction = from_node.node_map[to_node]

        if direct_order[facing] - direct_order[to_direction] == 0:
            return 'right'
        else:
            return 'left'
    except KeyError:
        pass


async def go_to(start, end, facing, direction_list=[]):
    visited = []
    queue = []
    queue.append([start])

    while queue:
        current_path = queue.pop(0)
        current_pos = current_path[-1]
        visited.append(current_pos)

        if isinstance(current_pos, DoorNode) and current_pos.door_num == end.door_num:
            return current_path

        for connection in current_pos.connections:
            if connection not in visited:
                new_path = list(current_path)
                new_path.append(connection)
                queue.append(new_path)


async def main():
    await build_school()
    directions = await go_to(br1, room_1401, 'n')
    print([direction for direction in directions])


if __name__ == '__main__':
    asyncio.run(main())