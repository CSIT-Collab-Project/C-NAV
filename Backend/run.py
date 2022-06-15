from PIL import Image, ImageDraw
import asyncio
import json
import math
import path
import sys

sys.path.append(path.Path(__file__).abspath().parent.parent)
import Backend.Nodes.StairNode
import Backend.Nodes.CornerNode
from Backend.Node_Config.Dev.nodes import *

WIDTH = 2000
HEIGHT = 1659


async def is_arts(node):
    if isinstance(node, DoorNode):
        if int((node.door_num / 100) % 10) == 6:
            return True
    elif "Arts" in node.name:
        return True
    return False


async def draw_path(node_list):
    # im = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    floor = [
        Image.open('Backend/Maps/test1.png'),
        Image.open('Backend/Maps/test2.png'),
        Image.open('Backend/Maps/test3.png'),
        Image.open('Backend/Maps/test4.png'),
        Image.open('Backend/Maps/test5.png'),
        Image.open('Backend/Maps/test5.png'),
        Image.open('Backend/Maps/test5.png'),
        Image.open('Backend/Maps/Arts2nd.png')
    ]
    im2 = Image.open('Backend/Icons/You are here.png')
    stair_up = Image.open('Backend/Icons/stair-up-hi.png')
    stair_down = Image.open('Backend/Icons/stair-down-hi.png')
    dest = Image.open('Backend/Icons/destination.png')
    im2 = im2.resize((50, 50))
    stair_up = stair_up.resize((30, 30))
    stair_down = stair_down.resize((30, 30))
    dest = dest.resize((50, 50))
    draw_floor = [ImageDraw.Draw(floor[0]), ImageDraw.Draw(floor[1]), ImageDraw.Draw(floor[2]),
                  ImageDraw.Draw(floor[3]), ImageDraw.Draw(floor[4]), ImageDraw.Draw(floor[0]),
                  ImageDraw.Draw(floor[0]), ImageDraw.Draw(floor[7])]
    total_length = 0
    from_node = (0, 0)
    to_node = (0, 0)

    top = math.inf
    left = math.inf
    bottom = -math.inf
    right = - math.inf

    fill_color = (155, 9, 238, 255)
    print(fill_color)

    for i in range(len(node_list) - 1):
        print(node_list[i + 1].name)
        from_arts = await is_arts(node_list[i])
        to_arts = await is_arts(node_list[i + 1])
        print(to_arts)
        try:
            from_node = node_list[i].coordinates
            if isinstance(node_list[i], DoorNode):
                current_floor = int((node_list[i].door_num / 1000) - 1)
            elif isinstance(node_list[i], StairwellNode):
                if isinstance(node_list[i + 1], DoorNode):
                    current_floor = int((node_list[i + 1].door_num / 1000) - 1)
                else:
                    current_floor = int(node_list[i + 1].name[0]) - 1
            else:
                current_floor = int(node_list[i].name[0]) - 1

            if from_arts != to_arts:
                continue
            elif from_arts:
                current_floor += 5

            to_node = node_list[i + 1].coordinates

            if from_node == to_node:
                continue

            if from_node[0] < left:
                left = max(from_node[0] - 75, 0)
            if from_node[1] < top:
                top = max(from_node[1] - 75, 0)
            if from_node[0] > right:
                right = min(from_node[0] + 75, 2000)
            if from_node[1] > bottom:
                bottom = min(from_node[1] + 75, 1659)

            print(f"Drawing from {from_node} to {to_node}")

            total_length += abs(abs(to_node[0]) - abs(from_node[0])) + abs(abs(to_node[1]) - abs(from_node[1]))

            if isinstance(node_list[i], StairNode) and isinstance(node_list[i + 1], StairNode):
                if int(node_list[i].name[0]) < int(node_list[i + 1].name[0]):
                    floor[current_floor].paste(stair_up, (from_node[0] - 15, from_node[1] - 15), stair_up)
                else:
                    floor[current_floor].paste(stair_down, (from_node[0] - 15, from_node[1] - 15), stair_down)
            elif node_list[i] in [fl1, fl2] and node_list[i + 1] in [fr1, fr2]:
                front_coords = (841, 905)

                draw_floor[current_floor].line(((from_node[0], from_node[1]), (front_coords[0], front_coords[1])),
                                               fill=fill_color, width=10)
                draw_floor[current_floor].line(((front_coords[0], front_coords[1]), (to_node[0], to_node[1])),
                                               fill=fill_color, width=10)

            elif isinstance(node_list[i + 1], DoorNode) or isinstance(node_list[i], DoorNode):
                hor_directions = {"n": 0, "s": 0, "e": -1, "w": 1}
                vert_directions = {"n": 1, "s": -1, "e": 0, "w": 0}

                if isinstance(node_list[i + 1], DoorNode):
                    stop_coords = (to_node[0] + (25 * hor_directions[node_list[i + 1].door_side]),
                                   to_node[1] + (25 * vert_directions[node_list[i + 1].door_side]))
                else:
                    stop_coords = (from_node[0] + (25 * hor_directions[node_list[i].door_side]),
                                   from_node[1] + (25 * vert_directions[node_list[i].door_side]))

                draw_floor[current_floor].line(((from_node[0], from_node[1]), (stop_coords[0], stop_coords[1])),
                                               fill=fill_color, width=10)
                draw_floor[current_floor].line(((stop_coords[0], stop_coords[1]), (to_node[0], to_node[1])),
                                               fill=fill_color, width=10)

            else:
                draw_floor[current_floor].line(((from_node[0], from_node[1]), (to_node[0], to_node[1])),
                                               fill=fill_color, width=10)

            if i == 0:
                thresh = 100
                fn = lambda x: 255 if x > thresh else 0
                floor[current_floor].paste(im2, (from_node[0] - 25, from_node[1] - 50),
                                           im2.convert("L").point(fn, mode='1'))

            if i == len(node_list) - 2:
                print(to_node[0])
                print(to_node[1])
                if to_node[0] < left:
                    left = max(to_node[0] - 75, 0)
                if to_node[1] < top:
                    top = max(to_node[1] - 75, 0)
                if to_node[0] > right:
                    right = min(to_node[0] + 75, 2000)
                if to_node[1] > bottom:
                    bottom = min(to_node[1] + 75, 1659)

                thresh = 100
                fn = lambda x: 255 if x < thresh else 0
                floor[current_floor].paste(dest, (to_node[0] - 25, to_node[1] - 50),
                                           dest.convert("L").point(fn, mode='1'))

        except AttributeError:
            pass

    for i in range(len(floor)):
        # 1080 x 1920
        TARGET_WIDTH = 1080
        TARGET_HEIGHT = 1920

        crop_center = (((left + right) / 2), ((top + bottom) / 2))

        left_over = max(TARGET_WIDTH / 2 - crop_center[0], 0)
        right_over = max((TARGET_WIDTH / 2 + crop_center[0]) - WIDTH, 0)
        top_over = max(TARGET_HEIGHT / 2 - crop_center[1], 0)
        bottom_over = max((TARGET_HEIGHT / 2 + crop_center[1]) - HEIGHT, 0)

        left = max(crop_center[0] - TARGET_WIDTH / 2 - right_over, 0)
        right = min(crop_center[0] + TARGET_WIDTH / 2 + left_over, WIDTH)
        top = max(crop_center[1] - TARGET_HEIGHT / 2 - top_over, 0)
        bottom = min(crop_center[1] + TARGET_HEIGHT / 2 + bottom_over, HEIGHT)

        crop_rect = (left, top, right, bottom)
        floor[i] = floor[i].crop(crop_rect)

        floor[i].save(f'map_path{i}.png', quality=95)

    print(f"Total Length: {total_length}")
    return total_length


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
                    turn_order.append("through doors to left")
            elif from_node in [stair2_f2, stair2_f3]:
                if to_node in [s2e, s3e]:
                    turn_order.append("exit stairs through doors to left")
                    facing = "w"
                    continue
                else:
                    turn_order.append("through doors to right")
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

    for i in range(len(turn_order) - 2):
        counter = 1
        try:
            if turn_order[i] == 'go up 1 floor' and turn_order[i + 1] == turn_order[i]:
                while turn_order[i + 1] == 'go up 1 floor':
                    turn_order.pop(i + 1)
                    counter += 1

                turn_order[i] = f'go up {counter} floors'

            elif turn_order[i] == 'go down 1 floor' and turn_order[i + 1] == turn_order[i]:
                while turn_order[i + 1] == 'go down 1 floor':
                    turn_order.pop(i + 1)
                    counter += 1

                turn_order[i] = f'go down {counter} floors'
        except IndexError:
            continue

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
    visited = [start_loc]

    for node in await go_to(start_loc, end_loc):
        if not isinstance(node, DoorNode):
            visited_nodes.append(node.name)
            visited.append(node)

    visited.append(end_loc)
    await draw_path(visited)

    return await toJSON(directions)


async def toJSON(directions: list):
    return json.dumps(directions, indent=4)


if __name__ == '__main__':
    print(asyncio.run(main('2202', '2601')))
