import asyncio

from Node_Config.nodes import *


async def get_turn_direction(facing, from_node, to_node):
    direct_order = {'n': 1, 'e': 1, 's': 2, 'w': 2}
    to_direction = from_node.turn_map[to_node]

    if direct_order[facing] - direct_order[to_direction] == 0:
        return 'right'
    else:
        return 'left'


async def go_to(start, end, facing, direction_list=[]):
    if isinstance(start, DoorNode):
        if start.door_num == end.door_num:
            return direction_list

    else:
        for node in start.connections:
            direction_list.append(await get_turn_direction(facing, start, node))
            await go_to(node, end, start.turn_map[node])


async def main():
    await build_school()
    directions = await go_to(br1, room_1401, 'n')
    print(directions)


if __name__ == '__main__':
    asyncio.run(main())