import asyncio
import json

import Backend.Nodes.StairNode
import Backend.Nodes.CornerNode
from Node_Config.nodes import *


async def convert_to_direction(facing, path):
    direct_order = ['n', 'e', 's', 'w', 'n', 'w']
    turn_order = []
    skip = False
    just_staired = False

    for i in range(len(path) - 1):
        if skip:
            skip = False
            continue

        from_node = path[i]
        to_node = path[i + 1]

        if just_staired and not isinstance(to_node, StairNode):
            just_staired = False
            if from_node in [stair3_f2, stair3_f3]:
                if to_node in [n2e, n3e]:
                    turn_order.append("exit stairs through doors to right")
                    facing = "w"
                    continue
                else:
                    turn_order.append("through doors to left:")
            elif from_node in [stair2_f2, stair2_f3]:
                if to_node in [s2e, s3e]:
                    turn_order.append("exit stairs through doors to left")
                    facing = "w"
                    continue
                else:
                    turn_order.append("through doors on right:")
        elif from_node in [stair3_f2, stair3_f3, stair2_f2, stair2_f3] and isinstance(to_node, CornerNode):
            turn_order.append("exit through doors across stairwell")
            continue

        if isinstance(from_node, StairNode) and not isinstance(to_node, StairwellNode):
            if to_node not in [n2e, n3e, s2e, s3e]:
                facing = await turn(from_node.door_side, 'reverse')

        if isinstance(from_node, Backend.Nodes.StairNode.StairNode):
            if isinstance(to_node, Backend.Nodes.StairNode.StairNode):
                if from_node.upstairs == to_node:
                    turn_order.append('go up 1 floor')
                elif from_node.downstairs == to_node:
                    turn_order.append('go down 1 floor')
                facing = await turn(to_node.door_side, 'reverse')
                just_staired = True
            elif isinstance(to_node, StairwellNode):
                turn_order.append('enter doors in stairwell')
            else:
                to_direction = from_node.node_map[to_node]
                if direct_order[direct_order.index(facing) - 1] == to_direction:
                    facing = await turn(facing, 'left')
                    turn_order.append('exit stairs left')
                elif direct_order[direct_order.index(facing) + 1] == to_direction:
                    facing = await turn(facing, 'right')
                    turn_order.append('exit stairs right')
                elif direct_order[direct_order.index(facing)] == to_direction:
                    turn_order.append('exit stairs straight')
                    if isinstance(to_node, Backend.Nodes.CornerNode.CornerNode):
                        skip = True

        elif isinstance(from_node, StairwellNode):
            if isinstance(to_node, DoorNode):
                facing = "e"
            continue

        else:
            if isinstance(from_node, DoorNode) and i == 0:
                if isinstance(to_node, StairwellNode):
                    turn_order.append('exit to stairwell')
                else:
                    to_direction = from_node.node_map[to_node]
                    if direct_order[direct_order.index(facing) - 1] == to_direction:
                        facing = await turn(facing, 'left')
                        turn_order.append('exit left')
                    elif direct_order[direct_order.index(facing) + 1] == to_direction:
                        facing = await turn(facing, 'right')
                        turn_order.append('exit right')
                    elif direct_order[direct_order.index(facing)] == to_direction:
                        turn_order.append('exit straight')

            elif not isinstance(from_node, Backend.Nodes.StairNode.StairNode):
                to_direction = from_node.node_map[to_node]
                if direct_order[direct_order.index(facing) - 1] == to_direction:
                    facing = await turn(facing, 'left')
                    turn_order.append('left')
                elif direct_order[direct_order.index(facing) + 1] == to_direction:
                    facing = await turn(facing, 'right')
                    turn_order.append('right')
                elif direct_order[direct_order.index(facing)] == to_direction:
                    turn_order.append('continue straight')

            if isinstance(to_node, Backend.Nodes.StairNode.StairNode):
                to_direction = to_node.door_side
                if direct_order[direct_order.index(facing) - 1] == to_direction:
                    facing = await turn(facing, 'left')
                    turn_order.append('enter stairs on left')
                elif direct_order[direct_order.index(facing) + 1] == to_direction:
                    facing = await turn(facing, 'right')
                    turn_order.append('enter stairs on right')
                elif direct_order[direct_order.index(facing)] == to_direction:
                    turn_order.append('enter stairs straight ahead')

    to_direction = path[-1].door_side
    if direct_order[direct_order.index(facing) - 1] == to_direction:
        turn_order.append('room door is on the left')
    elif direct_order[direct_order.index(facing) + 1] == to_direction:
        turn_order.append('room door is on the right')
    else:
        turn_order.append('room door is straight ahead')

    return turn_order


async def turn(start_direction, turn_direction):
    directions = ('n', 'e', 's', 'w', 'n', 'e', 's', 'w')
    if turn_direction == 'right':
        return directions[directions.index(start_direction) + 1]
    elif turn_direction == 'left':
        return directions[directions.index(start_direction) - 1]
    elif turn_direction == 'reverse':
        return directions[directions.index(start_direction) - 2]
    else:
        return 'continue straight'


async def go_to(start, end):
    visited = []
    queue = [[start]]

    while queue:
        if not (isinstance(queue[-1], DoorNode) and isinstance(queue[0], DoorNode)):
            current_path = queue.pop(0)
            current_pos = current_path[-1]
            visited.append(current_pos)

            if isinstance(current_pos, DoorNode) and current_pos.door_num == end.door_num:
                print(current_path)
                return current_path

            for connection in current_pos.connections:
                if connection not in visited:
                    new_path = list(current_path)
                    new_path.append(connection)
                    queue.append(new_path)


async def main(start_str, end_str):
    start_loc = None
    end_loc = None

    opp_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    await build_school()

    for room in room_list:
        if room.door_num == int(start_str):
            start_loc = room
        elif room.door_num == int(end_str):
            end_loc = room

    if not start_loc or not end_loc:
        print('Error')
        return await toJSON(['Error'])

    directions = [direction for direction in await convert_to_direction(opp_directions[start_loc.door_side],
                                                                        [direction for direction in
                                                                         await go_to(start_loc, end_loc)])]

    visited_nodes = []

    for node in await go_to(start_loc, end_loc):
        if not isinstance(node, DoorNode):
            visited_nodes.append(node.name)

    print(visited_nodes)

    return await toJSON(directions)


async def toJSON(directions: list):
    return json.dumps(directions, indent=2)


if __name__ == '__main__':
    print(asyncio.run(main('1311', '5102')))
