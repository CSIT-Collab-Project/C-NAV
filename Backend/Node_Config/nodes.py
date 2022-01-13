from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.DoorNode import DoorNode

fc1 = CornerNode([])
fr1 = CornerNode([])
fl1 = CornerNode([])
bc1 = CornerNode([])
br1 = CornerNode([])
bl1 = CornerNode([])
the_void = None

room_1108 = DoorNode([fl1, bl1], 1108, fl1)
room_1105 = DoorNode([fl1, fc1], 1105, fl1)
room_1102 = DoorNode([fl1, fc1], 1102, fc1)
room_1401 = DoorNode([fc1, fr1], 1401, fc1)
room_1402 = DoorNode([fc1, fr1], 1402, fc1)
room_1409 = DoorNode([fc1, fr1], 1409, fr1)
room_1202 = DoorNode([fl1, bl1], 1202, fl1)
room_1225 = DoorNode([bl1, bc1], 1225, bc1)
room_1228 = DoorNode([bl1, bc1], 1228, bc1)
room_1223 = DoorNode([bl1, bc1], 1223, bl1)
room_1311 = DoorNode([bc1, br1], 1311, bc1)
room_1312 = DoorNode([bc1, br1], 1312, br1)


async def build_school():
    await fc1.add_directions(bc1, fr1, the_void, fl1)
    await fr1.add_directions(br1, the_void, the_void, fc1)
    await fl1.add_directions(bl1, fc1, the_void, the_void)
    await bc1.add_directions(the_void, br1, fc1, bl1)
    await br1.add_directions(the_void, the_void, fr1, bc1)
    await bl1.add_directions(the_void, bc1, fl1, the_void)