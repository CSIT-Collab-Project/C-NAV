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
    print(start.connections)

    if isinstance(start, DoorNode):
        print(start.door_num)
        print(end.door_num)
        if start.door_num == end.door_num:
            return direction_list

    else:
        print("Else")
        if start is not None:
            print("If start is not")
            for node in start.connections:
                if node != start:
                    print("If node != start")
                    try:
                        print("RECURSE")
                        direction_list.append(asyncio.ensure_future(get_turn_direction(facing, start, node)))
                        asyncio.ensure_future(go_to(node, end, start.node_map[node]))
                    except KeyError:
                        print('KeyError')
                        pass

    return 'Error'


async def main():
    await build_school()
    directions = await go_to(br1, room_1401, 'n')
    print([direction for direction in directions])


if __name__ == '__main__':
    asyncio.run(main())