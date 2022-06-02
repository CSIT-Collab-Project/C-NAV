import copy
import re

from PIL import Image, ImageDraw
import asyncio
import json
import math
import path
import sys
import Backend.Nodes.StairNode
import Backend.Nodes.CornerNode
from Backend.Node_Config.Dev.nodes import *
from Logger.logger import logger

sys.path.append(path.Path(__file__).abspath().parent.parent)

WIDTH = 2000
HEIGHT = 1659

full_path = []


async def is_arts(node):
    """
    Checks if node is in arts building
    :param node: Node to check
    :return: Boolean for node being in arts building
    """
    if isinstance(node, DoorNode):
        if int((node.door_num / 100) % 10) == 6:
            return True
    elif "Arts" in node.name:
        return True
    return False


async def draw_path(node_list):
    logger.info(f"draw_path({node_list})")
    """
    Takes path and draws on proper maps; crops maps to fit phone screen
    :param node_list: List of visited nodes in order from start to end
    :return: Pixel length of drawn path
    """
    # Defines map img files
    floor = [
        Image.open('Backend/Maps/floor1.png'),
        Image.open('Backend/Maps/floor2.png'),
        Image.open('Backend/Maps/floor3.png'),
        Image.open('Backend/Maps/floor4.png'),
        Image.open('Backend/Maps/floor5.png'),
        Image.open('Backend/Maps/floor5.png'),
        Image.open('Backend/Maps/floor5.png'),
        Image.open('Backend/Maps/Arts2nd.png')
    ]

    # Defines icon files
    im2 = Image.open('Backend/Icons/You are here.png')
    stair_up = Image.open('Backend/Icons/stair-up-hi.png')
    stair_down = Image.open('Backend/Icons/stair-down-hi.png')
    dest = Image.open('Backend/Icons/destination.png')

    # Resizes icons to proper size
    im2 = im2.resize((50, 50))
    stair_up = stair_up.resize((30, 30))
    stair_down = stair_down.resize((30, 30))
    dest = dest.resize((50, 50))

    # Creates ImageDraw objects to draw on
    draw_floor = [ImageDraw.Draw(floor[0]), ImageDraw.Draw(floor[1]), ImageDraw.Draw(floor[2]),
                  ImageDraw.Draw(floor[3]), ImageDraw.Draw(floor[4]), ImageDraw.Draw(floor[0]),
                  ImageDraw.Draw(floor[0]), ImageDraw.Draw(floor[7])]

    # Starting values for variables
    total_length = 0
    top = math.inf
    left = math.inf
    bottom = -math.inf
    right = - math.inf
    fill_color = (155, 9, 238, 255)

    print(node_list)

    if len(node_list) == 1:
        # Extracts floor number from node
        current_floor = int((node_list[0].door_num / 1000) - 1)

        thresh = 100
        fn = lambda x: 255 if x < thresh else 0
        floor[current_floor].paste(dest, (node_list[0].coordinates[0] - 25, node_list[0].coordinates[1] - 50),
                                   dest.convert("L").point(fn, mode='1'))
        left = max(node_list[0].coordinates[0] - 75, 0)
        top = max(node_list[0].coordinates[1] - 75, 0)
        right = min(node_list[0].coordinates[0] + 75, 2000)
        bottom = min(node_list[0].coordinates[1] + 75, 1659)

    # Iterates over each node in path
    for i in range(len(node_list) - 1):
        # Checks for building of from and to node
        from_arts = await is_arts(node_list[i])
        to_arts = await is_arts(node_list[i + 1])

        try:
            # Get coordinates of from and to nodes
            from_node = node_list[i].coordinates
            to_node = node_list[i + 1].coordinates

            # Extracts floor number from node
            if isinstance(node_list[i], DoorNode):
                current_floor = int((node_list[i].door_num / 1000) - 1)
            elif isinstance(node_list[i], StairwellNode):
                if isinstance(node_list[i + 1], DoorNode):
                    current_floor = int((node_list[i + 1].door_num / 1000) - 1)
                else:
                    current_floor = int(node_list[i + 1].name[0]) - 1
            else:
                current_floor = int(node_list[i].name[0]) - 1

            # Skip drawing from main -> arts and vice-versa
            if from_arts != to_arts:
                continue
            elif from_arts:
                current_floor += 5

            # Don't draw to yourself
            if from_node == to_node:
                continue

            # Get most extreme node coordinates in each direction
            if from_node[0] < left:
                left = max(from_node[0] - 75, 0)
            if from_node[1] < top:
                top = max(from_node[1] - 75, 0)
            if from_node[0] > right:
                right = min(from_node[0] + 75, 2000)
            if from_node[1] > bottom:
                bottom = min(from_node[1] + 75, 1659)

            # Keep track of path length in pixels to help choose the shortest path
            total_length += abs(abs(to_node[0]) - abs(from_node[0])) + abs(abs(to_node[1]) - abs(from_node[1]))

            # Changes floor when travelling on stairs
            if isinstance(node_list[i], StairNode) and isinstance(node_list[i + 1], StairNode):
                if int(node_list[i].name[0]) < int(node_list[i + 1].name[0]):
                    floor[current_floor].paste(stair_up, (from_node[0] - 15, from_node[1] - 15), stair_up)
                else:
                    floor[current_floor].paste(stair_down, (from_node[0] - 15, from_node[1] - 15), stair_down)

            # Handle front bend !!!REMOVE ONCE UPDATED MAP IS ADDED!!!
            elif node_list[i] in [fl1, fl2] and node_list[i + 1] in [fr1, fr2]:
                front_coords = (841, 905)

                draw_floor[current_floor].line(((from_node[0], from_node[1]), (front_coords[0], front_coords[1])),
                                               fill=fill_color, width=10)
                draw_floor[current_floor].line(((front_coords[0], front_coords[1]), (to_node[0], to_node[1])),
                                               fill=fill_color, width=10)

            # Enter door from center of hallway rather than a direct path
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

            # Draw normally between nodes
            else:
                draw_floor[current_floor].line(((from_node[0], from_node[1]), (to_node[0], to_node[1])),
                                               fill=fill_color, width=10)

            # Make current location marker's background transparent and add to first node
            if i == 0:
                thresh = 100
                fn = lambda x: 255 if x > thresh else 0
                floor[current_floor].paste(im2, (from_node[0] - 25, from_node[1] - 50),
                                           im2.convert("L").point(fn, mode='1'))

            # Make destination pin's background transparent and add to last node
            if i == len(node_list) - 2:
                thresh = 100
                fn = lambda x: 255 if x < thresh else 0
                floor[current_floor].paste(dest, (to_node[0] - 25, to_node[1] - 50),
                                           dest.convert("L").point(fn, mode='1'))

        # Don't die if path does weird things
        except AttributeError:
            pass

    # Crop maps to proper dimensions for phone screen
    for i in range(len(floor)):
        # Set target dimensions
        target_width = 1080
        target_height = 1920

        # Find center of nodes
        crop_center = (((left + right) / 2), ((top + bottom) / 2))

        # If edge goes over map edge, shift to compensate
        left_over = max(target_width / 2 - crop_center[0], 0)
        right_over = max((target_width / 2 + crop_center[0]) - WIDTH, 0)
        top_over = max(target_height / 2 - crop_center[1], 0)
        bottom_over = max((target_height / 2 + crop_center[1]) - HEIGHT, 0)

        left = max(crop_center[0] - target_width / 2 - right_over, 0)
        right = min(crop_center[0] + target_width / 2 + left_over, WIDTH)
        top = max(crop_center[1] - target_height / 2 - top_over, 0)
        bottom = min(crop_center[1] + target_height / 2 + bottom_over, HEIGHT)

        crop_rect = (left, top, right, bottom)
        floor[i] = floor[i].crop(crop_rect)

        # Save drawn / cropped map
        floor[i].save(f'map_path{i}.png', quality=95)

    # Return final length of path
    print(f"Total Length: {total_length}")
    return total_length


async def convert_to_direction(facing, path):
    """
    Convert path to list of human-readable instructions
    :param facing: Direction user is facing at start
    :param path: List of visited nodes in order from start to end
    :return: List of human-readable instructions to follow path
    """
    direct_order = ['n', 'e', 's', 'w', 'n', 'w']
    turn_order = []
    skip = False
    just_staired = False

    for i in range(len(path) - 1):
        # Skip this direction if instructed to
        if skip:
            skip = False
            continue

        # Get currently occupied node and next node in list
        from_node = path[i]
        to_node = path[i + 1]

        # Give instructions for exiting stairs
        if just_staired and not isinstance(to_node, StairNode):
            just_staired = False
            # Handle stairs with multiple exits
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
        # Handle passing through stairwells
        elif from_node in [stair3_f2, stair3_f3, stair2_f2, stair2_f3] and isinstance(to_node, CornerNode):
            turn_order.append("exit through doors across stairwell")
            continue

        # Reverse direction when leaving stairs
        if isinstance(from_node, StairNode) and not isinstance(to_node, StairwellNode):
            if to_node not in [n2e, n3e, s2e, s3e]:
                facing = await turn(from_node.door_side, 'reverse')

        # Handle generic stair instructions
        if isinstance(from_node, Backend.Nodes.StairNode.StairNode):
            # Going up/down
            if isinstance(to_node, Backend.Nodes.StairNode.StairNode):
                if from_node.upstairs == to_node:
                    turn_order.append('go up 1 floor')
                elif from_node.downstairs == to_node:
                    turn_order.append('go down 1 floor')
                facing = await turn(to_node.door_side, 'reverse')
                just_staired = True
            # Entering stairs
            elif isinstance(to_node, StairwellNode):
                turn_order.append('enter doors in stairwell')
            # Exiting stairs
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

        # Stairwell -> Door is always east
        elif isinstance(from_node, StairwellNode):
            if isinstance(to_node, DoorNode):
                facing = "e"
            continue

        # Non-stair originating instructions
        else:
            # Exiting rooms to stairwells
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
            # Standard turning
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
            # Entering stairs
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

    # Get desired direction to be facing
    to_direction = path[-1].door_side

    # Provide info on location of door when time to enter
    if direct_order[direct_order.index(facing) - 1] == to_direction:
        turn_order.append('room door is on the left')
    elif direct_order[direct_order.index(facing) + 1] == to_direction:
        turn_order.append('room door is on the right')
    else:
        turn_order.append('room door is straight ahead')

    # Look through instructions and compress floor climbs into 1 instruction
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
    """
    Take currently facing direction and desired direction to generate turn direction
    :param start_direction: Initial Direction
    :param turn_direction: Desired Direction
    :return: Turn needed to go from initial -> desired direction
    """
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
    """
    Generate path from start node to end node
    :param start: Node to start at
    :param end: Final Node
    :return: List of nodes corresponding to the shortest path from start->end
    """
    logger.info(f"go_to({start}, {end})")
    visited = []
    queue = [[start]]

    # Breadth-first search for shortest path
    while queue:
        if not (isinstance(queue[-1], DoorNode) and isinstance(queue[0], DoorNode)):
            current_path = queue.pop(0)
            current_pos = current_path[-1]
            logger.info(f"Current search node: {current_pos.name}")
            visited.append(current_pos)

            if isinstance(current_pos, DoorNode) and current_pos.door_num == end.door_num:
                print(current_path)
                return current_path

            for connection in current_pos.connections:
                if connection not in visited:
                    new_path = list(current_path)
                    new_path.append(connection)
                    visited.append(connection)
                    queue.append(new_path)


async def draw_step(step):
    part_path = copy.deepcopy(full_path)
    for i in range(step):
        part_path.pop(0)
    await draw_path(part_path)


async def main(start_str, end_str):
    """
    Run entire pathfinding system
    :param start_str: String representing starting room
    :param end_str: String representing ending room
    :return: List of human-readable instructions from start to end
    """

    start_str = re.sub("[^0-9]", "", start_str)
    end_str = re.sub("[^0-9]", "", end_str)

    if len(start_str) < 1 or len(end_str) < 1:
        return await toJSON(['Error'])

    logger.info(f"main({start_str}, {end_str})")
    start_loc = None
    end_loc = None
    global full_path

    opp_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    await build_school()

    # Check if the rooms are valid and convert to int
    for room in room_list:
        if room.door_num == int(start_str):
            start_loc = room
        elif room.door_num == int(end_str):
            end_loc = room

    # Return error if improper room
    if not start_loc or not end_loc:
        print('Error')
        return await toJSON(['Error'])

    # Create list of human-readable directions given start and end point
    full_path = await go_to(start_loc, end_loc)
    directions = [direction for direction in await convert_to_direction(opp_directions[start_loc.door_side],
                                                                        [direction for direction in
                                                                         full_path])]

    visited_nodes = []
    visited = [start_loc]

    # Make list of all node objects visited
    for node in await go_to(start_loc, end_loc):
        if not isinstance(node, DoorNode):
            visited_nodes.append(node.name)
            visited.append(node)

    visited.append(end_loc)

    # Draw map using all visited nodes
    await draw_path(visited)

    return await toJSON(directions)


async def toJSON(directions: list):
    return json.dumps(directions, indent=2)


if __name__ == '__main__':
    print(asyncio.run(main('1311', '1225')))
