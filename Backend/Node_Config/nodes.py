from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.DoorNode import DoorNode
from Backend.Nodes.StairNode import StairNode

fc1 = CornerNode([], "Front Center 1st")
fr1 = CornerNode([], "Front Right 1st")
fl1 = CornerNode([], "Front Left 1st")
bc1 = CornerNode([], "Back Center 1st")
br1 = CornerNode([], "Back Right 1st")
bl1 = CornerNode([], "Back Left 1st")
the_void = CornerNode([], "The endless void of nothingness and despair. "
                          "Nothing can enter, nothing can exit. Pure emptiness")

stair1_f1 = StairNode([], "n", "Stair 1 1st Floor")
stair1_f2 = StairNode([], "n", "Stair 1 2nd Floor")

stair2_f1 = StairNode([], "w", "Stair 2 1st Floor")
stair2_f2 = StairNode([], "w", "Stair 2 2nd Floor")

stair3_f1 = StairNode([], "w", "Stair 3 1st Floor")
stair3_f2 = StairNode([], "w", "Stair 3 2nd Floor")

stair5_f1 = StairNode([], "n", "Stair 5 1st Floor")
stair5_f2 = StairNode([], "n", "Stair 5 2nd Floor")

stair6_f1 = StairNode([], "n", "Stair 6 1st Floor")
stair6_f2 = StairNode([], "n", "Stair 6 2nd Floor")

stair8_f1 = StairNode([], "e", "Stair 8 1st Floor")
stair8_f2 = StairNode([], "e", "Stair 8 2nd Floor")

# 1st Floor
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
room_1107 = DoorNode([], 0, the_void, 'e')
room_1109 = DoorNode([], 0, the_void, 's')
room_1106 = DoorNode([], 0, the_void, 'n')
room_1104 = DoorNode([], 0, the_void, 'w')
room_1410 = DoorNode([], 0, the_void, 'n')
room_1420 = DoorNode([], 0, the_void, 'e')
room_1309 = DoorNode([], 0, the_void, 'n')
room_1224 = DoorNode([], 0, the_void, 's')
room_1303 = DoorNode([], 0, the_void, 's')
room_1307 = DoorNode([], 0, the_void, 'n')
room_1305 = DoorNode([], 0, the_void, 's')
room_1221 = DoorNode([], 0, the_void, 'n')
room_1203 = DoorNode([], 0, the_void, 's')
room_1226 = DoorNode([], 0, the_void, 'w')
room_1227 = DoorNode([], 0, the_void, 'w')
room_1204 = DoorNode([], 0, the_void, 'w')

# Testing
room_1234 = DoorNode([], 0, the_void, "e")

# 2nd Floor


room_list = [
    room_1108,
    room_1105,
    room_1102,
    room_1401,
    room_1402,
    room_1409,
    room_1202,
    room_1225,
    room_1228,
    room_1223,
    room_1311,
    room_1312,
    room_1107,
    room_1109,
    room_1106,
    room_1104,
    room_1410,
    room_1420,
    room_1309,
    room_1303,
    room_1307,
    room_1305,
    room_1221,
    room_1203,
    room_1226,
    room_1227,
    room_1204,
    room_1234
]


async def build_doors():
    await room_1108.set_info([fl1, bl1, room_1202], 1108, fl1, ["n", "s", "s"])
    await room_1105.set_info([fl1, fc1, room_1102, room_1106], 1105, fl1, ["e", "w", "w", "w"])
    await room_1102.set_info([fl1, fc1, room_1105, room_1106], 1102, fc1, ["e", "w", "e", "w"])
    await room_1401.set_info([fc1, fr1, room_1409, room_1402], 1401, fc1, ["e", "w", "w", "w"])
    await room_1402.set_info([fc1, fr1, room_1401, room_1409], 1402, fc1, ["e", "w", "e", "w"])
    await room_1409.set_info([fc1, fr1, room_1401, room_1402], 1409, fr1, ["e", "w", "e", "e"])
    await room_1202.set_info([fl1, bl1, room_1108], 1202, fl1, ["n", "s", "n"])
    await room_1225.set_info([bl1, bc1, room_1223, room_1224, room_1228], 1225, bc1, ["e", "w", "e", "e", "w"])
    await room_1228.set_info([bl1, bc1, room_1223, room_1224, room_1225], 1228, bc1, ["e", "n", "e", "e", "e"])
    await room_1223.set_info([bl1, bc1, room_1224, room_1225, room_1228], 1223, bl1, ["e", "w", "w", "w", "w"])
    await room_1311.set_info([bc1, br1, room_1312], 1311, bc1, ["e", "w", "w"])
    await room_1312.set_info([bc1, br1, room_1311], 1312, br1, ["e", "w", "e"])
    await room_1107.set_info([fl1, room_1109], 1107, fl1, ["s", "n"])
    await room_1109.set_info([fl1, room_1107], 1109, fl1, ["s", "s"])
    await room_1106.set_info([fc1, fl1, room_1105, room_1102], 1106, fc1, ["w", "e", "e", "e"])
    await room_1104.set_info([fc1, bc1, room_1227, room_1226], 1104, fc1, ["n", "s", "s", "s"])
    await room_1410.set_info([fc1, fr1], 1410, fr1, ["e", "w"])
    await room_1420.set_info([fr1], 1420, fr1, ["s"])
    await room_1309.set_info([br1, room_1303, room_1307, room_1305], 1309, br1, ["e", "e", "w", "w"])
    await room_1303.set_info([br1, room_1305, room_1307, room_1309], 1303, br1, ["e", "w", "w", "w"])
    await room_1307.set_info([br1, room_1303, room_1305, room_1309], 1307, br1, ["e", "e", "w", "e"])
    await room_1305.set_info([br1, room_1303, room_1307, room_1309], 1305, br1, ["e", "e", "e", "e"])
    await room_1221.set_info([bl1, room_1203, room_1204], 1221, bl1, ["w", "n", "e"])
    await room_1203.set_info([bl1, room_1221, room_1204], 1203, bl1, ["w", "s", "e"])
    await room_1226.set_info([fc1, bc1, room_1227, room_1104], 1226, bc1, ["n", "s", "n", "n"])
    await room_1227.set_info([fc1, bc1, room_1226, room_1104], 1227, bc1, ["n", "s", "s", "n"])
    await room_1204.set_info([bl1, room_1221, room_1203], 1204, bl1, ["w", "w", "w"])
    await room_1234.set_info([stair2_f2], 1234, stair2_f2, "e")


async def build_school():
    await fc1.add_directions(bc1, fr1, the_void, fl1)
    await fr1.add_directions(br1, the_void, the_void, fc1)
    await fl1.add_directions(bl1, fc1, stair2_f1, the_void)
    await bc1.add_directions(the_void, br1, fc1, bl1)
    await br1.add_directions(the_void, the_void, fr1, bc1)
    await bl1.add_directions(the_void, bc1, fl1, the_void)

    await stair1_f1.add_directions(the_void, fr1, fc1, fl1, stair1_f2, the_void)
    await stair1_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair1_f1)

    await stair2_f1.add_directions(fl1, the_void, the_void, the_void, stair2_f2, the_void)
    await stair2_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair2_f1)

    await stair3_f1.add_directions(bl1, the_void, fr1, the_void, stair3_f2, the_void)
    await stair3_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair3_f1)

    await stair5_f1.add_directions(the_void, the_void, bl1, the_void, stair5_f2, the_void)
    await stair5_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair5_f1)

    await stair6_f1.add_directions(the_void, the_void, br1, the_void, stair6_f2, the_void)
    await stair6_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair6_f1)

    await stair8_f1.add_directions(br1, the_void, fr1, the_void, stair8_f2, the_void)
    await stair8_f2.add_directions(the_void, the_void, the_void, the_void, the_void, stair8_f2)

    await build_doors()