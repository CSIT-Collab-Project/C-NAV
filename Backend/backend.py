import asyncio

from Node_Config.nodes import *


async def convert_to_direction(facing, path):
    direct_order = ['n', 'e', 's', 'w', 'n', 'w']
    turn_order = []
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i+1]

        try:
            to_direction = from_node.node_map[to_node]

            if direct_order[direct_order.index(facing) - 1] == to_direction:
                facing = await turn(facing, 'left')
                turn_order.append('left')
            elif direct_order[direct_order.index(facing) + 1] == to_direction:
                facing = await turn(facing, 'right')
                turn_order.append('right')
            else:
                turn_order.append('continue until next intersection')

        except KeyError:
            print('No Work')

    to_direction = path[-1].door_side
    if direct_order[direct_order.index(facing) - 1] == to_direction:
        turn_order.append('room door is on the left')
    elif direct_order[direct_order.index(facing) + 1] == to_direction:
        turn_order.append('room door is on the right')
    else:
        turn_order.append('room door is straight ahead')

    return turn_order


async def turn(start_direction, turn_direction):
    directions = ('n', 'e', 's', 'w', 'n', 'w')
    if turn_direction == 'right':
        return directions[directions.index(start_direction) + 1]
    elif turn_direction == 'left':
        return directions[directions.index(start_direction) - 1]
    else:
        return 'continue straight'


async def go_to(start, end):
    visited = []
    queue = [[start]]

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


async def main(start_loc, end_loc):
    opp_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    await build_school()
    directions = await go_to(start_loc, end_loc)
    path = [direction for direction in directions]
    print([turn for turn in await convert_to_direction(opp_directions[start_loc.door_side], path)])
    return [turn for turn in await convert_to_direction(opp_directions[start_loc.door_side], path)]

if __name__ == '__main__':
    asyncio.run(main(room_1401, room_1107))
