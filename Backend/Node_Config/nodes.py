from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.DoorNode import DoorNode
from Backend.Nodes.Node import Node

fc1 = CornerNode([])
fr1 = CornerNode([])
fl1 = CornerNode([])
bc1 = CornerNode([])
br1 = CornerNode([])
bl1 = CornerNode([])
the_void = CornerNode([])

room_1108 = DoorNode([], 0, the_void, 'e')
room_1105 = DoorNode([], 0, the_void, 's')
room_1102 = DoorNode([], 0, the_void, 's')
room_1401 = DoorNode([], 0, the_void, 'n')
room_1402 = DoorNode([], 0, the_void, 's')
room_1409 = DoorNode([], 0, the_void, 'n')
room_1202 = DoorNode([], 0, the_void, 'w')
room_1225 = DoorNode([], 0, the_void, 'n')
room_1228 = DoorNode([], 0, the_void, 'n')
room_1223 = DoorNode([], 0, the_void, 's')
room_1311 = DoorNode([], 0, the_void, 's')
room_1312 = DoorNode([], 0, the_void, 'n')


async def build_doors():
    await room_1108.set_info([fl1, bl1], 1108, fl1, ["n", "s"])
    await room_1105.set_info([fl1, fc1], 1105, fl1, ["e", "w"])
    await room_1102.set_info([fl1, fc1], 1102, fc1, ["e", "w"])
    await room_1401.set_info([fc1, fr1], 1401, fc1, ["e", "w"])
    await room_1402.set_info([fc1, fr1], 1402, fc1, ["e", "w"])
    await room_1409.set_info([fc1, fr1], 1409, fr1, ["e", "w"])
    await room_1202.set_info([fl1, bl1], 1202, fl1, ["n", "s"])
    await room_1225.set_info([bl1, bc1], 1225, bc1, ["e", "w"])
    await room_1228.set_info([bl1, bc1], 1228, bc1, ["e", "n"])
    await room_1223.set_info([bl1, bc1], 1223, bl1, ["e", "w"])
    await room_1311.set_info([bc1, br1], 1311, bc1, ["e", "w"])
    await room_1312.set_info([bc1, br1], 1312, br1, ["e", "w"])


async def build_school():
    await fc1.add_directions(bc1, fr1, the_void, fl1)
    await fr1.add_directions(br1, the_void, the_void, fc1)
    await fl1.add_directions(bl1, fc1, the_void, the_void)
    await bc1.add_directions(the_void, br1, fc1, bl1)
    await br1.add_directions(the_void, the_void, fr1, bc1)
    await bl1.add_directions(the_void, bc1, fl1, the_void)
    await build_doors()