from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.DoorNode import DoorNode
from Backend.Nodes.StairNode import StairNode

fc1 = CornerNode([], "Front Center 1st")
fr1 = CornerNode([], "Front Right 1st")
fl1 = CornerNode([], "Front Left 1st")
bc1 = CornerNode([], "Back Center 1st")
br1 = CornerNode([], "Back Right 1st")
bl1 = CornerNode([], "Back Left 1st")

fc2 = CornerNode([], "Front Center 2nd")
fr2 = CornerNode([], "Front Right 2nd")
fl2 = CornerNode([], "Front Left 2nd")
bc2 = CornerNode([], "Back Center 2nd")
br2 = CornerNode([], "Back Right 2nd")
bl2 = CornerNode([], "Back Left 2nd")

l3 = CornerNode([], "Left 3rd")
r3 = CornerNode([], "Right 3rd")

l4 = CornerNode([], "Left 4th")
r4 = CornerNode([], "Right 4th")

the_void = CornerNode([], "The endless void of nothingness and despair. "
                          "Nothing can enter, nothing can exit. Pure emptiness")

stair1_f1 = StairNode([], "n", "Stair 1 1st Floor")
stair1_f2 = StairNode([], "n", "Stair 1 2nd Floor")
stair1_f3 = StairNode([], "n", "Stair 1 3rd Floor")
stair1_f4 = StairNode([], "n", "Stair 1 4th Floor")

stair2_f1 = StairNode([], "w", "Stair 2 1st Floor")
stair2_f2 = StairNode([], "w", "Stair 2 2nd Floor")
stair2_f3 = StairNode([], "w", "Stair 2 3rd Floor")
stair2_f4 = StairNode([], "w", "Stair 2 4th Floor")
stair2_f5 = StairNode([], "w", "Stair 2 5th Floor")

stair3_f1 = StairNode([], "w", "Stair 3 1st Floor")
stair3_f2 = StairNode([], "w", "Stair 3 2nd Floor")
stair3_f3 = StairNode([], "w", "Stair 3 3rd Floor")
stair3_f4 = StairNode([], "w", "Stair 3 4th Floor")

stair5_f1 = StairNode([], "n", "Stair 5 1st Floor")
stair5_f2 = StairNode([], "n", "Stair 5 2nd Floor")

stair6_f1 = StairNode([], "n", "Stair 6 1st Floor")
stair6_f2 = StairNode([], "n", "Stair 6 2nd Floor")

stair8_f1 = StairNode([], "e", "Stair 8 1st Floor")
stair8_f2 = StairNode([], "e", "Stair 8 2nd Floor")
stair8_f3 = StairNode([], "e", "Stair 8 3rd Floor")
stair8_f4 = StairNode([], "e", "Stair 8 4th Floor")

stair9_f1 = StairNode([], "e", "Stair 9 1st Floor")
stair9_f2 = StairNode([], "e", "Stair 9 2nd Floor")
stair9_f3 = StairNode([], "e", "Stair 9 3rd Floor")
stair9_f4 = StairNode([], "e", "Stair 9 4th Floor")
stair9_f5 = StairNode([], "e", "Stair 9 5th Floor")

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
room_2203 = DoorNode([], 0, the_void, "n")
room_2204 = DoorNode([], 0, the_void, "s")
room_2205 = DoorNode([], 0, the_void, "n")
room_2206 = DoorNode([], 0, the_void, "s")
room_2207 = DoorNode([], 0, the_void, "n")
room_2208 = DoorNode([], 0, the_void, "s")
room_2209 = DoorNode([], 0, the_void, "n")
room_2210 = DoorNode([], 0, the_void, "s")
room_2211 = DoorNode([], 0, the_void, "n")
room_2213 = DoorNode([], 0, the_void, "n")
room_2214 = DoorNode([], 0, the_void, "s")
room_2215 = DoorNode([], 0, the_void, "n")
room_2311 = DoorNode([], 0, the_void, "n")
room_2312 = DoorNode([], 0, the_void, "s")
room_2313 = DoorNode([], 0, the_void, "n")
room_2314 = DoorNode([], 0, the_void, "s")
room_2315 = DoorNode([], 0, the_void, "n")
room_2316 = DoorNode([], 0, the_void, "n")
room_2317 = DoorNode([], 0, the_void, "n")
room_2318 = DoorNode([], 0, the_void, "s")
room_2319 = DoorNode([], 0, the_void, "n")
room_2310 = DoorNode([], 0, the_void, "s")
room_2320 = DoorNode([], 0, the_void, "s")
room_2321 = DoorNode([], 0, the_void, "n")
room_2322 = DoorNode([], 0, the_void, "s")
room_2309 = DoorNode([], 0, the_void, "n")
room_2112 = DoorNode([], 0, the_void, "n")
room_2110 = DoorNode([], 0, the_void, "s")
room_2106 = DoorNode([], 0, the_void, "n")
room_2101 = DoorNode([], 0, the_void, "n")
room_2109 = DoorNode([], 0, the_void, "s")
room_2104 = DoorNode([], 0, the_void, "s")
room_2403 = DoorNode([], 0, the_void, "s")
room_2405 = DoorNode([], 0, the_void, "s")
room_2401 = DoorNode([], 0, the_void, "n")
room_2212 = DoorNode([], 0, the_void, "e")
room_2202 = DoorNode([], 0, the_void, "w")
room_2201 = DoorNode([], 0, the_void, "w")
room_2119 = DoorNode([], 0, the_void, "s")
room_3124 = DoorNode([], 0, the_void, "e")
room_3111 = DoorNode([], 0, the_void, "s")
room_3103 = DoorNode([], 0, the_void, "n")
room_3104 = DoorNode([], 0, the_void, "s")
room_3101 = DoorNode([], 0, the_void, "n")
room_3102 = DoorNode([], 0, the_void, "s")
room_3401 = DoorNode([], 0, the_void, "s")
room_3404 = DoorNode([], 0, the_void, "n")
room_3402 = DoorNode([], 0, the_void, "s")

room_4111 = DoorNode([], 0, the_void, "s")
room_4117 = DoorNode([], 0, the_void, "w")
room_4118 = DoorNode([], 0, the_void, "w")
room_4119 = DoorNode([], 0, the_void, "w")
room_4120 = DoorNode([], 0, the_void, "w")
room_4121 = DoorNode([], 0, the_void, "w")
room_4122 = DoorNode([], 0, the_void, "n")
room_4105 = DoorNode([], 0, the_void, "e")
room_4104 = DoorNode([], 0, the_void, "s")
room_4103 = DoorNode([], 0, the_void, "n")
room_4102 = DoorNode([], 0, the_void, "s")
room_4101 = DoorNode([], 0, the_void, "n")
room_4401 = DoorNode([], 0, the_void, "s")
room_4402 = DoorNode([], 0, the_void, "s")
room_4403 = DoorNode([], 0, the_void, "n")
room_4405 = DoorNode([], 0, the_void, "s")
room_4410 = DoorNode([], 0, the_void, "e")
room_4406 = DoorNode([], 0, the_void, "s")

room_5101 = DoorNode([], 0, the_void, "s")
room_5102 = DoorNode([], 0, the_void, "n")
room_5103 = DoorNode([], 0, the_void, "s")
room_5104 = DoorNode([], 0, the_void, "n")
room_5105 = DoorNode([], 0, the_void, "n")
room_5405 = DoorNode([], 0, the_void, "s")
room_5404 = DoorNode([], 0, the_void, "n")
room_5403 = DoorNode([], 0, the_void, "s")
room_5402 = DoorNode([], 0, the_void, "n")
room_5401 = DoorNode([], 0, the_void, "s")

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
    room_1204,
    room_2203,
    room_2204,
    room_2205,
    room_2206,
    room_2207,
    room_2208,
    room_2209,
    room_2210,
    room_2211,
    room_2213,
    room_2214,
    room_2215,
    room_2311,
    room_2312,
    room_2313,
    room_2314,
    room_2315,
    room_2316,
    room_2317,
    room_2318,
    room_2319,
    room_2310,
    room_2320,
    room_2321,
    room_2322,
    room_2309,
    room_2112,
    room_2110,
    room_2106,
    room_2101,
    room_2109,
    room_2104,
    room_2403,
    room_2405,
    room_2401,
    room_2212,
    room_2202,
    room_2201,
    room_2119,
    room_3124,
    room_3111,
    room_3103,
    room_3104,
    room_3101,
    room_3102,
    room_3401,
    room_3404,
    room_3402,
    room_4111,
    room_4117,
    room_4118,
    room_4119,
    room_4120,
    room_4121,
    room_4122,
    room_4105,
    room_4104,
    room_4103,
    room_4102,
    room_4101,
    room_4401,
    room_4402,
    room_4403,
    room_4405,
    room_4410,
    room_4406,
    room_5101,
    room_5102,
    room_5103,
    room_5104,
    room_5105,
    room_5405,
    room_5404,
    room_5403,
    room_5402,
    room_5401
]


async def build_doors():
    await room_1108.set_info([fl1, bl1, room_1202, stair3_f1], 1108, fl1, ["n", "s", "s", "s"])
    await room_1105.set_info([fl1, fr1, room_1102, room_1106, stair1_f1], 1105, fl1, ["e", "w", "w", "w", "w"])
    await room_1102.set_info([fl1, fr1, room_1105, room_1106, stair1_f1], 1102, fc1, ["e", "w", "e", "w", "w"])
    await room_1401.set_info([fl1, fr1, room_1409, room_1402, stair1_f1], 1401, fc1, ["e", "w", "w", "w", "e"])
    await room_1402.set_info([fl1, fr1, room_1401, room_1409, stair1_f1], 1402, fc1, ["e", "w", "e", "w", "e"])
    await room_1409.set_info([fl1, fr1, room_1401, room_1402, stair1_f1], 1409, fr1, ["e", "w", "e", "e", "e"])
    await room_1202.set_info([fl1, bl1, room_1108, stair3_f1], 1202, fl1, ["n", "s", "n", "n"])
    await room_1225.set_info([bl1, br1, room_1223, room_1224, room_1228], 1225, bc1, ["e", "w", "e", "e", "w"])
    await room_1228.set_info([bl1, br1, room_1223, room_1224, room_1225], 1228, bc1, ["e", "n", "e", "e", "e"])
    await room_1223.set_info([bl1, br1, room_1224, room_1225, room_1228], 1223, bl1, ["e", "w", "w", "w", "w"])
    await room_1311.set_info([bl1, br1, room_1312], 1311, bc1, ["e", "w", "w"])
    await room_1312.set_info([bl1, br1, room_1311], 1312, br1, ["e", "w", "e"])
    await room_1107.set_info([fl1, room_1109], 1107, fl1, ["s", "n"])
    await room_1109.set_info([fl1, room_1107], 1109, fl1, ["s", "s"])
    await room_1106.set_info([fr1, fl1, room_1105, room_1102], 1106, fc1, ["w", "e", "e", "e"])
    await room_1104.set_info([fr1, bl1, room_1227, room_1226], 1104, fc1, ["n", "s", "s", "s"])
    await room_1410.set_info([fl1, fr1], 1410, fr1, ["e", "w"])
    await room_1420.set_info([fr1], 1420, fr1, ["s"])
    await room_1309.set_info([br1, room_1303, room_1307, room_1305], 1309, br1, ["e", "e", "w", "w"])
    await room_1303.set_info([br1, room_1305, room_1307, room_1309], 1303, br1, ["e", "w", "w", "w"])
    await room_1307.set_info([br1, room_1303, room_1305, room_1309], 1307, br1, ["e", "e", "w", "e"])
    await room_1305.set_info([br1, room_1303, room_1307, room_1309], 1305, br1, ["e", "e", "e", "e"])
    await room_1221.set_info([bl1, room_1203, room_1204], 1221, bl1, ["w", "n", "e"])
    await room_1203.set_info([bl1, room_1221, room_1204], 1203, bl1, ["w", "s", "e"])
    await room_1204.set_info([bl1, room_1221, room_1203], 1204, bl1, ["w", "w", "w"])

    await room_2203.set_info([room_2204, room_2205, room_2206, room_2207, room_2208, room_2209, room_2210, bl2], 2203,
                             bl2, ["n", "w", "w", "w", "w", "w", "w", "w"])
    await room_2204.set_info([room_2203, room_2205, room_2206, room_2207, room_2208, room_2209, room_2210, bl2], 2204,
                             bl2, ["s", "w", "w", "w", "w", "w", "w", "w"])
    await room_2205.set_info([room_2204, room_2203, room_2206, room_2207, room_2208, room_2209, room_2210, bl2], 2205,
                             bl2, ["e", "e", "e", "w", "w", "w", "w", "w"])
    await room_2206.set_info([room_2203, room_2204, room_2205, room_2207, room_2208, room_2209, room_2210, bl2], 2206,
                             bl2, ["e", "e", "w", "w", "w", "w", "w", "w"])
    await room_2207.set_info([room_2203, room_2204, room_2205, room_2206, room_2208, room_2209, room_2210, bl2], 2207,
                             bl2, ["e", "e", "e", "e", "w", "w", "w", "w"])
    await room_2208.set_info([room_2203, room_2204, room_2205, room_2206, room_2207, room_2209, room_2210, bl2], 2208,
                             bl2, ["e", "e", "e", "e", "e", "w", "w", "w"])
    await room_2209.set_info([room_2203, room_2204, room_2205, room_2206, room_2207, room_2208, room_2210, bl2], 2209,
                             bl2, ["e", "e", "e", "e", "e", "e", "n", "w"])
    await room_2210.set_info([room_2203, room_2204, room_2205, room_2206, room_2207, room_2208, room_2209, bl2], 2210,
                             bl2, ["e", "e", "e", "e", "e", "e", "s", "w"])
    await room_2211.set_info([room_2213, room_2214, room_2215, room_2321, room_2322, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2211, bl2, ["w", "n", "w", "w", "w", "w", "w", "w", "w", "e", "w"])
    await room_2213.set_info([room_2211, room_2214, room_2215, room_2321, room_2322, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2213, bl2, ["e", "e", "w", "w", "w", "w", "w", "w", "w", "e", "w"])
    await room_2214.set_info([room_2211, room_2213, room_2215, room_2321, room_2322, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2214, bl2, ["s", "w", "w", "w", "w", "w", "w", "w", "w", "e", "w"])
    await room_2215.set_info([room_2211, room_2213, room_2214, room_2321, room_2322, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2215, bl2, ["e", "e", "e", "w", "w", "w", "w", "w", "w", "e", "w"])
    await room_2322.set_info([room_2211, room_2213, room_2214, room_2315, room_2321, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2322, bl2, ["e", "e", "e", "e", "w", "w", "w", "w", "w", "e", "w"])
    await room_2321.set_info([room_2211, room_2213, room_2214, room_2315, room_2322, room_2320, room_2319, room_2318,
                              room_2317, bl2, br2], 2321, bl2, ["e", "e", "e", "e", "e", "w", "w", "w", "w", "e", "w"])
    await room_2320.set_info([room_2211, room_2213, room_2214, room_2315, room_2322, room_2321, room_2319, room_2318,
                              room_2317, bl2, br2], 2320, bl2, ["e", "e", "e", "e", "e", "e", "s", "w", "w", "e", "w"])
    await room_2319.set_info([room_2211, room_2213, room_2214, room_2315, room_2322, room_2321, room_2320, room_2318,
                              room_2317, bl2, br2], 2319, bl2, ["e", "e", "e", "e", "e", "e", "n", "w", "w", "e", "w"])
    await room_2318.set_info([room_2211, room_2213, room_2214, room_2315, room_2322, room_2321, room_2320, room_2319,
                              room_2317, bl2, br2], 2318, bl2, ["e", "e", "e", "e", "e", "e", "e", "e", "s", "e", "w"])
    await room_2317.set_info([room_2211, room_2213, room_2214, room_2315, room_2322, room_2321, room_2320, room_2319,
                              room_2317, bl2, br2], 2317, bl2, ["e", "e", "e", "e", "e", "e", "e", "e", "n", "e", "w"])

    await room_2309.set_info([room_2316, room_2315, room_2314, room_2313, room_2312, room_2311, room_2310, br2], 2309,
                             br2, ["e", "e", "e", "e", "e", "e", "n", "e"])
    await room_2310.set_info([room_2316, room_2315, room_2314, room_2313, room_2312, room_2311, room_2309, br2], 2330,
                             br2, ["e", "e", "e", "e", "e", "e", "s", "e"])
    await room_2311.set_info([room_2316, room_2315, room_2314, room_2313, room_2312, room_2310, room_2309, br2], 2311,
                             br2, ["e", "e", "e", "e", "n", "w", "w", "e"])
    await room_2312.set_info([room_2316, room_2315, room_2314, room_2313, room_2311, room_2310, room_2309, br2], 2312,
                             br2, ["e", "e", "e", "e", "s", "w", "w", "e"])
    await room_2313.set_info([room_2316, room_2315, room_2314, room_2312, room_2311, room_2310, room_2309, br2], 2313,
                             br2, ["e", "e", "w", "w", "w", "w", "w", "e"])
    await room_2314.set_info([room_2316, room_2315, room_2313, room_2312, room_2311, room_2310, room_2309, br2], 2314,
                             br2, ["e", "e", "e", "w", "w", "w", "w", "e"])
    await room_2315.set_info([room_2316, room_2314, room_2313, room_2312, room_2311, room_2310, room_2309, br2], 2315,
                             br2, ["e", "w", "w", "w", "w", "w", "w", "e"])
    await room_2316.set_info([room_2315, room_2314, room_2313, room_2312, room_2311, room_2310, room_2309, br2], 2316,
                             br2, ["w", "w", "w", "w", "w", "w", "w", "e"])

    await room_2112.set_info([room_2110, room_2109, room_2106, room_2104, room_2101, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2112, fl2, ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_2110.set_info([room_2112, room_2109, room_2106, room_2104, room_2101, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2110, fl2, ['e', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_2109.set_info([room_2112, room_2110, room_2106, room_2104, room_2101, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2109, fl2, ['e', 'e', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_2106.set_info([room_2112, room_2110, room_2109, room_2104, room_2101, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2106, fl2, ['e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_2104.set_info([room_2112, room_2110, room_2109, room_2106, room_2101, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2104, fl2, ['e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_2101.set_info([room_2112, room_2110, room_2109, room_2106, room_2104, stair1_f2, room_2403, room_2405,
                              fl2, fr2], 2101, fl2, ['e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'e', 'w'])
    await room_2403.set_info([room_2112, room_2110, room_2109, room_2106, room_2104, room_2101, stair1_f2, room_2405,
                              fl2, fr2], 2403, fl2, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w'])
    await room_2405.set_info([room_2112, room_2110, room_2109, room_2106, room_2104, room_2101, stair1_f2, room_2403,
                              fl2, fr2], 2405, fl2, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w'])

    await room_2212.set_info([room_2202, room_2201, bl2, fl2], 2212, bl2, ['n', 'n', 's', 'n'])
    await room_2202.set_info([room_2212, room_2201, bl2, fl2], 2202, bl2, ['s', 'n', 's', 'n'])
    await room_2201.set_info([room_2212, room_2202, bl2, fl2], 2201, bl2, ['s', 's', 's', 'n'])

    await room_2119.set_info([fl2], 2119, fl2, ['s'])
    await room_3124.set_info([l3], 3124, l3, ['n'])
    await room_3111.set_info([l3], 3111, l3, ['s'])
    await room_3103.set_info([room_3104, room_3101, room_3102, room_3401, stair1_f3, room_3404, room_3402, l3, r3],
                             3103, l3, ['n', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_3104.set_info([room_3103, room_3101, room_3102, room_3401, stair1_f3, room_3404, room_3402, l3, r3],
                             3104, l3, ['s', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_3101.set_info([room_3103, room_3104, room_3102, room_3401, stair1_f3, room_3404, room_3402, l3, r3],
                             3101, l3, ['e', 'e', 'e', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_3102.set_info([room_3103, room_3104, room_3101, room_3401, stair1_f3, room_3404, room_3402, l3, r3],
                             3102, l3, ['e', 'e', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_3401.set_info([room_3103, room_3104, room_3101, room_3102, stair1_f3, room_3404, room_3402, l3, r3],
                             3401, l3, ['e', 'e', 'e', 'e', 's', 'w', 'w', 'e', 'w'])
    await room_3404.set_info([room_3103, room_3104, room_3101, room_3102, room_3401, stair1_f3, room_3402, l3, r3],
                             3404, l3, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w'])
    await room_3402.set_info([room_3103, room_3104, room_3101, room_3102, room_3401, stair1_f3, room_3404, l3, r3],
                             3402, l3, ['e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w'])

    await room_4111.set_info([room_4117, room_4118, room_4119, room_4120, room_4121, room_4122, stair2_f4, stair3_f4,
                              l4], 4111, l4, ['s', 's', 's', 's', 's', 's', 'e', 's', 's'])
    await room_4117.set_info([room_4111, room_4118, room_4119, room_4120, room_4121, room_4122, stair2_f4, stair3_f4,
                              l4], 4117, l4, ['n', 's', 's', 's', 's', 's', 'n', 's', 's'])
    await room_4118.set_info([room_4111, room_4117, room_4119, room_4120, room_4121, room_4122, stair2_f4, stair3_f4,
                              l4], 4118, l4, ['n', 'n', 's', 's', 's', 's', 'n', 's', 'n'])
    await room_4119.set_info([room_4111, room_4117, room_4118, room_4120, room_4121, room_4122, stair2_f4, stair3_f4,
                              l4], 4119, l4, ['n', 'n', 'n', 's', 's', 's', 'n', 's', 'n'])
    await room_4120.set_info([room_4111, room_4117, room_4118, room_4119, room_4121, room_4122, stair2_f4, stair3_f4,
                              l4], 4120, l4, ['n', 'n', 'n', 'n', 's', 's', 'n', 's', 'n'])
    await room_4121.set_info([room_4111, room_4117, room_4118, room_4119, room_4120, room_4122, stair2_f4, stair3_f4,
                              l4], 4121, l4, ['n', 'n', 'n', 'n', 'n', 's', 's', 's', 'n'])
    await room_4122.set_info([room_4111, room_4117, room_4118, room_4119, room_4120, room_4121, stair2_f4, stair3_f4,
                              l4], 4122, l4, ['n', 'n', 'n', 'n', 'n', 'n', 's', 's', 'n'])

    await room_4105.set_info([room_4104, room_4103, room_4102, room_4101, room_4401, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4105, l4, ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_4104.set_info([room_4105, room_4103, room_4102, room_4101, room_4401, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4104, l4, ['e', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_4103.set_info([room_4105, room_4104, room_4102, room_4101, room_4401, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4103, l4, ['e', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_4102.set_info([room_4105, room_4104, room_4103, room_4101, room_4401, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4102, l4, ['e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_4101.set_info([room_4105, room_4104, room_4103, room_4102, room_4401, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4101, l4, ['e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 'e', 'w'])
    await room_4401.set_info([room_4105, room_4104, room_4103, room_4102, room_4101, stair1_f4, room_4402, room_4403,
                              room_4405, l4, r4], 4401, l4, ['e', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'e', 'w'])
    await room_4402.set_info([room_4105, room_4104, room_4103, room_4102, room_4101, stair1_f4, room_4401, room_4403,
                              room_4405, l4, r4], 4402, l4, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'e', 'w'])
    await room_4403.set_info([room_4105, room_4104, room_4103, room_4102, room_4101, stair1_f4, room_4401, room_4402,
                              room_4405, l4, r4], 4403, l4, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'w'])
    await room_4405.set_info([room_4105, room_4104, room_4103, room_4102, room_4101, stair1_f4, room_4401, room_4402,
                              room_4405, l4, r4], 4405, l4, ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'e', 'w'])

    await room_4410.set_info([stair8_f4, r4], 4410, r4, ['n', 'n'])
    await room_4406.set_info([r3], 4406, r4, ['s'])

    await room_5102.set_info([room_5101, room_5104, room_5103, room_5104, room_5105, room_5405, room_5404, room_5403,
                              room_5402, room_5401, stair2_f5, stair9_f5], 5102, the_void, ['w', 'w', 'w', 'w', 'w',
                                                                                            'w', 'w', 'w', 'w', 'w',
                                                                                            'e', 'w'])
    await room_5101.set_info([room_5102, room_5104, room_5103, room_5104, room_5105, room_5405, room_5404, room_5403,
                              room_5402, room_5401, stair2_f5, stair9_f5], 5101, the_void, ['e', 's', 'w', 'w', 'w',
                                                                                            'w', 'w', 'w', 'w', 'w',
                                                                                            'e', 'w'])


async def build_school():
    await fr1.add_directions([br1, stair8_f1], the_void, stair9_f1, [fl1, stair1_f1])
    await fl1.add_directions([bl1, stair3_f1], [fr1, stair1_f1], stair2_f1, the_void)
    await br1.add_directions(stair6_f1, the_void, [fr1, stair8_f1], bl1)
    await bl1.add_directions(stair5_f1, br1, [fl1, stair3_f1], the_void)

    await fr2.add_directions([br2, stair8_f2], the_void, stair9_f2, fl2)
    await fl2.add_directions([bl2, stair3_f2], fr2, stair2_f2, the_void)
    await br2.add_directions(stair6_f2, the_void, [fr2, stair9_f2], bl2)
    await bl2.add_directions(stair5_f2, br2, [fl2, stair3_f2], the_void)

    await l3.add_directions(stair3_f3, r3, stair2_f3, the_void)
    await r3.add_directions(stair8_f3, the_void, stair9_f3, l3)

    await l4.add_directions(stair3_f4, r4, stair2_f4, the_void)
    await r4.add_directions(stair8_f4, the_void, stair9_f4, l4)

    await stair1_f1.add_directions(the_void, fr1, fc1, fl1, stair1_f2, the_void)
    await stair1_f2.add_directions(the_void, fr2, the_void, fl2, stair1_f3, stair1_f1)
    await stair1_f3.add_directions(the_void, r3, the_void, l3, stair1_f4, stair1_f2)
    await stair1_f4.add_directions(the_void, r4, the_void, l4, the_void, stair1_f3)

    await stair2_f1.add_directions(fl1, the_void, the_void, the_void, stair2_f2, the_void)
    await stair2_f2.add_directions(fl2, the_void, the_void, the_void, stair2_f3, stair2_f1)
    await stair2_f3.add_directions(l3, the_void, the_void, the_void, stair2_f4, stair2_f2)
    await stair2_f4.add_directions(l4, the_void, the_void, the_void, stair2_f5, stair2_f3)
    await stair2_f5.add_directions(the_void, the_void, the_void, the_void, the_void, stair2_f4)

    await stair3_f1.add_directions(bl1, the_void, fl1, the_void, stair3_f2, the_void)
    await stair3_f2.add_directions(bl2, the_void, fl2, the_void, stair3_f3, stair3_f1)
    await stair3_f3.add_directions(the_void, the_void, l3, the_void, stair3_f4, stair3_f2)
    await stair3_f4.add_directions(the_void, the_void, l4, the_void, the_void, stair3_f4)

    await stair5_f1.add_directions(the_void, the_void, bl1, the_void, stair5_f2, the_void)
    await stair5_f2.add_directions(the_void, the_void, bl2, the_void, the_void, stair5_f1)

    await stair6_f1.add_directions(the_void, the_void, br1, the_void, stair6_f2, the_void)
    await stair6_f2.add_directions(the_void, the_void, br2, the_void, the_void, stair6_f1)

    await stair8_f1.add_directions(br1, the_void, fr1, the_void, stair8_f2, the_void)
    await stair8_f2.add_directions(br2, the_void, fr2, the_void, stair8_f3, stair8_f2)
    await stair8_f3.add_directions(the_void, the_void, r3, the_void, stair8_f4, stair8_f2)
    await stair8_f4.add_directions(the_void, the_void, r4, the_void, the_void, stair8_f3)

    await stair9_f1.add_directions(br1, the_void, fr1, the_void, stair9_f2, the_void)
    await stair9_f2.add_directions(br2, the_void, fr2, the_void, stair9_f3, stair9_f1)
    await stair9_f3.add_directions(r3, the_void, the_void, the_void, stair9_f4, stair9_f2)
    await stair9_f4.add_directions(r4, the_void, the_void, the_void, stair9_f5, stair9_f3)
    await stair9_f5.add_directions(the_void, the_void, the_void, the_void, the_void, stair9_f4)

    await build_doors()