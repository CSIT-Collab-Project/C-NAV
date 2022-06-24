import path
import sys

sys.path.append(path.Path(__file__).abspath().parent.parent.parent)
from Backend.Nodes.CornerNode import CornerNode
from Backend.Nodes.DoorNode import DoorNode
from Backend.Nodes.StairNode import StairNode
from Backend.Nodes.StairwellNode import StairwellNode

fc1 = CornerNode([], "1 Front Center 1st")
fr1 = CornerNode([], "1 Front Right 1st", (1288, 1001))
fl1 = CornerNode([], "1 Front Left 1st", (422, 1001))
bc1 = CornerNode([], "1 Back Center 1st")
br1 = CornerNode([], "1 Back Right 1st", (1288, 512))
bl1 = CornerNode([], "1 Back Left 1st", (422, 512))

fc2 = CornerNode([], "2 Front Center 2nd")
fr2 = CornerNode([], "2 Front Right 2nd", (1281, 1001))
fl2 = CornerNode([], "2 Front Left 2nd", (429, 1001))
bc2 = CornerNode([], "2 Back Center 2nd")
br2 = CornerNode([], "2 Back Right 2nd", (1281, 514))
bl2 = CornerNode([], "2 Back Left 2nd", (429, 514))

n2e = CornerNode([], "2 North Extension 2nd Floor", (352, 664))
c2e = CornerNode([], "2 Center Extension 2nd Floor", (323, 768))
s2e = CornerNode([], "2 South Extension 2nd Floor", (280, 860))

l3 = CornerNode([], "3 Left 3rd", (433, 997))
r3 = CornerNode([], "3 Right 3rd", (1287, 997))

n3e = CornerNode([], "3 North Extension 3rd Floor", (257, 866))
s3e = CornerNode([], "3 South Extension 3rd Floor", (257, 1142))

l4 = CornerNode([], "4 Left 4th", (430, 1001))
r4 = CornerNode([], "4 Right 4th", (1285, 1001))

atl0 = CornerNode([], "Arts Building Top Left Basement")
atr0 = CornerNode([], "Arts Building Top Right Basement")
aml0 = CornerNode([], "Arts Building Middle Left Basement")
amr0 = CornerNode([], "Arts Building Middle Right Basement")
abl0 = CornerNode([], "Arts Building Bottom Left Basement")
abr0 = CornerNode([], "Arts Building Bottom Right Basement")

af1 = CornerNode([], "1 Arts Building Front 1st")
atl1 = CornerNode([], "1 Arts Building Top Left 1st")
abl1 = CornerNode([], "1 Arts Building Bottom Left 1st")
abr1 = CornerNode([], "1 Arts Building Bottom Right 1st")
atr1 = CornerNode([], "1 Arts Building Top Right 1st")

atl2 = CornerNode([], "2 Arts Building Top Left 2nd", (676, 609))
abl2 = CornerNode([], "2 Arts Building Back Left 2nd", (673, 1280))
abr2 = CornerNode([], "2 Arts Building Back Right 2nd", (1488, 1284))
atr2 = CornerNode([], "2 Arts Building Top Right 2nd", (1488, 804))
amb2 = CornerNode([], "2 Arts Building Middle Bottom 2nd", (1150, 804))
amt2 = CornerNode([], "2 Arts Building Middle Top 2nd", (1150, 609))

atl3 = CornerNode([], "3 Arts Building Top Left 3rd")
atll3 = CornerNode([], "3 Arts Building Top Left Left 3rd")
abl3 = CornerNode([], "3 Arts Building Back Left 3rd")
abr3 = CornerNode([], "3 Arts Building Back Right 3rd")
atr3 = CornerNode([], "3 Arts Building Top Right 3rd")
amb3 = CornerNode([], "3 Arts Building Middle Bottom 3rd")
amt3 = CornerNode([], "3 Arts Building Middle Top 3rd")

the_void = CornerNode([], "The endless void of nothingness and despair. "
                          "Nothing can enter, nothing can exit. Pure emptiness")

stair1_f1 = StairNode([], "n", "1 Stair 1 1st Floor", (916, 968))
stair1_f2 = StairNode([], "n", "2 Stair 1 2nd Floor", (917, 968))
stair1_f3 = StairNode([], "n", "3 Stair 1 3rd Floor", (918, 968))
stair1_f4 = StairNode([], "n", "4 Stair 1 4th Floor", (918, 968))

stair2_f1 = StairNode([], "w", "1 Stair 2 1st Floor", (394, 1171))
stair2_f2 = StairNode([], "w", "2 Stair 2 2nd Floor", (395, 1143))
stair2_f3 = StairNode([], "w", "3 Stair 2 3rd Floor", (396, 1143))
stair2_f4 = StairNode([], "w", "4 Stair 2 4th Floor", (396, 1143))
stair2_f5 = StairNode([], "w", "5 Stair 2 5th Floor", (461, 1175))

stair3_f1 = StairNode([], "w", "1 Stair 3 1st Floor", (389, 821))
stair3_f2 = StairNode([], "w", "2 Stair 3 2nd Floor", (394, 861))
stair3_f3 = StairNode([], "w", "3 Stair 3 3rd Floor", (394, 858))
stair3_f4 = StairNode([], "w", "4 Stair 3 4th Floor", (394, 858))

stair5_f1 = StairNode([], "n", "1 Stair 5 1st Floor", (407, 477))
stair5_f2 = StairNode([], "n", "2 Stair 5 2nd Floor", (407, 480))

stair6_f1 = StairNode([], "n", "1 Stair 6 1st Floor", (1305, 479))
stair6_f2 = StairNode([], "n", "2 Stair 6 2nd Floor", (1305, 479))

stair8_f1 = StairNode([], "e", "1 Stair 8 1st Floor", (1324, 820))
stair8_f2 = StairNode([], "e", "2 Stair 8 2nd Floor", (1324, 820))
stair8_f3 = StairNode([], "e", "3 Stair 8 3rd Floor", (1324, 820))
stair8_f4 = StairNode([], "e", "4 Stair 8 4th Floor", (1324, 820))

stair9_f1 = StairNode([], "e", "1 Stair 9 1st Floor", (1324, 1186))
stair9_f2 = StairNode([], "e", "2 Stair 9 2nd Floor", (1324, 1186))
stair9_f3 = StairNode([], "e", "3 Stair 9 3rd Floor", (1324, 1186))
stair9_f4 = StairNode([], "e", "4 Stair 9 4th Floor", (1324, 1186))
stair9_f5 = StairNode([], "e", "5 Stair 9 5th Floor", (1263, 1175))

stair11_f0 = StairNode([], "e", "Stair 11 Basement")
stair11_f1 = StairNode([], "e", "1 Stair 11 1st Floor")
stair11_f2 = StairNode([], "e", "2 Stair 11 2nd Floor", (861, 147))
stair11_f3 = StairNode([], "e", "3 Stair 11 3rd Floor")

stair14_f0 = StairNode([], "w", "Stair 14 Basement")
stair14_f1 = StairNode([], "w", "1 Stair 14 1st Floor")
stair14_f2 = StairNode([], "w", "2 Stair 14 2nd Floor", (588, 1399))
stair14_f3 = StairNode([], "w", "3 Stair 14 3rd Floor")

stair17_f0 = StairNode([], "e", "Stair 17 Basement")
stair17_f1 = StairNode([], "e", "1 Stair 17 1st Floor")
stair17_f2 = StairNode([], "e", "2 Stair 17 2nd Floor", (1451, 1325))
stair17_f3 = StairNode([], "e", "3 Stair 17 3rd Floor")

# 1st Floor
room_1108 = DoorNode([], 0, the_void, 'e', (457, 949))
room_1105 = DoorNode([], 0, the_void, 's', (597, 1034))
room_1102 = DoorNode([], 0, the_void, 's', (709, 1034))
room_1401 = DoorNode([], 0, the_void, 'n', (974, 968))
room_1402 = DoorNode([], 0, the_void, 's', (1086, 1034))
room_1409 = DoorNode([], 0, the_void, 'n', (1103, 968))
room_1202 = DoorNode([], 0, the_void, 'w', (390, 787))
room_1225 = DoorNode([], 0, the_void, 'n', (724, 481))
room_1228 = DoorNode([], 0, the_void, 'n', (820, 481))
room_1223 = DoorNode([], 0, the_void, 's', (569, 547))  # Resume here
room_1311 = DoorNode([], 0, the_void, 's', (940, 547))
room_1312 = DoorNode([], 0, the_void, 'n', (1165, 481))
room_1107 = DoorNode([], 0, the_void, 'e', (457, 1052))
room_1109 = DoorNode([], 0, the_void, 's', (427, 1189))
room_1106 = DoorNode([], 0, the_void, 'n', (728, 967))
room_1410 = DoorNode([], 0, the_void, 'n', (1133, 968))
room_1420 = DoorNode([], 0, the_void, 'e', (1337, 1260))
room_1309 = DoorNode([], 0, the_void, 'n', (1373, 481))
room_1224 = DoorNode([], 0, the_void, 's', (604, 547))
room_1303 = DoorNode([], 0, the_void, 's', (1405, 529))
room_1307 = DoorNode([], 0, the_void, 'n', (1423, 506))
room_1305 = DoorNode([], 0, the_void, 's', (1423, 506))
room_1221 = DoorNode([], 0, the_void, 'n', (245, 481))
room_1203 = DoorNode([], 0, the_void, 's', (270, 529))
room_1226 = DoorNode([], 0, the_void, 'w')
room_1227 = DoorNode([], 0, the_void, 'w')
room_1204 = DoorNode([], 0, the_void, 'w', (223, 506))

mbr1 = DoorNode([], 0, the_void, "w", (1255, 725))
fbr1 = DoorNode([], 0, the_void, "e", (457, 726))

career = DoorNode([], 0, the_void, "s", (1274, 1307))

main = DoorNode([], 0, the_void, "s", (870, 1034))

# Testing
room_1234 = DoorNode([], 0, the_void, "e")

# 2nd Floor
room_2203 = DoorNode([], 0, the_void, "n", (110, 481))
room_2204 = DoorNode([], 0, the_void, "s", (110, 547))
room_2205 = DoorNode([], 0, the_void, "n", (206, 481))
room_2206 = DoorNode([], 0, the_void, "s", (190, 547))
room_2207 = DoorNode([], 0, the_void, "n", (206, 481))
room_2208 = DoorNode([], 0, the_void, "s", (239, 547))
room_2209 = DoorNode([], 0, the_void, "n", (366, 481))
room_2210 = DoorNode([], 0, the_void, "s", (369, 547))
room_2211 = DoorNode([], 0, the_void, "n", (616, 481))
room_2213 = DoorNode([], 0, the_void, "n", (658, 481))
room_2214 = DoorNode([], 0, the_void, "s", (670, 547))
room_2215 = DoorNode([], 0, the_void, "n", (829, 547))
room_2311 = DoorNode([], 0, the_void, "n", (1526, 481))
room_2312 = DoorNode([], 0, the_void, "s", (1556, 547))
room_2313 = DoorNode([], 0, the_void, "n", (1453, 481))
room_2314 = DoorNode([], 0, the_void, "s", (1490, 547))
room_2315 = DoorNode([], 0, the_void, "n", (1388, 481))
room_2316 = DoorNode([], 0, the_void, "n", (1399, 481))
room_2317 = DoorNode([], 0, the_void, "n", (1163, 481))
room_2318 = DoorNode([], 0, the_void, "s", (1185, 547))
room_2319 = DoorNode([], 0, the_void, "n", (945, 481))
room_2310 = DoorNode([], 0, the_void, "s", (1598, 547))
room_2320 = DoorNode([], 0, the_void, "s", (1071, 547))
room_2321 = DoorNode([], 0, the_void, "n", (902, 481))
room_2322 = DoorNode([], 0, the_void, "s", (968, 547))
room_2309 = DoorNode([], 0, the_void, "n", (1598, 481))
room_2112 = DoorNode([], 0, the_void, "n", (549, 967))
room_2110 = DoorNode([], 0, the_void, "s", (598, 1034))
room_2106 = DoorNode([], 0, the_void, "n", (673, 967))
room_2101 = DoorNode([], 0, the_void, "n", (866, 967))
room_2109 = DoorNode([], 0, the_void, "s", (675, 1034))
room_2104 = DoorNode([], 0, the_void, "s", (778, 1034))
room_2403 = DoorNode([], 0, the_void, "s", (908, 1034))
room_2405 = DoorNode([], 0, the_void, "s", (1044, 1034))
room_2401 = DoorNode([], 0, the_void, "n", (1095, 967))
room_2212 = DoorNode([], 0, the_void, "e", (463, 596))
room_2202 = DoorNode([], 0, the_void, "w", (396, 639))
room_2201 = DoorNode([], 0, the_void, "w", (396, 787))
room_2119 = DoorNode([], 0, the_void, "s", (445, 1189))

room_2414 = DoorNode([], 0, the_void, "s", (1430, 887))
room_2415 = DoorNode([], 0, the_void, "e", (1483, 862))
room_2412 = DoorNode([], 0, the_void, "n", (1430, 1116))
room_2411 = DoorNode([], 0, the_void, "e", (1483, 1140))

room_2135 = DoorNode([], 0, the_void, "w", (237, 865))
room_2132 = DoorNode([], 0, the_void, "w", (237, 1138))
room_2133 = DoorNode([], 0, the_void, "s", (132, 1017))
room_2134 = DoorNode([], 0, the_void, "n", (132, 986))

mbr2 = DoorNode([], 0, the_void, "w", (1250, 728))
fbr2 = DoorNode([], 0, the_void, "e", (461, 725))

library = DoorNode([], 0, the_void, "s", (1319, 1290))

room_3124 = DoorNode([], 0, the_void, "e", (463, 890))
room_3111 = DoorNode([], 0, the_void, "s", (445, 1189))
room_3103 = DoorNode([], 0, the_void, "n", (673, 967))
room_3104 = DoorNode([], 0, the_void, "s", (600, 1034))
room_3101 = DoorNode([], 0, the_void, "n", (866, 967))
room_3102 = DoorNode([], 0, the_void, "s", (747, 1034))
room_3401 = DoorNode([], 0, the_void, "s", (911, 1034))
room_3404 = DoorNode([], 0, the_void, "n", (1094, 967))
room_3402 = DoorNode([], 0, the_void, "s", (1032, 1034))

room_3411 = DoorNode([], 0, the_void, "s", (1430, 886))
room_3412 = DoorNode([], 0, the_void, "e", (1438, 863))
room_3409 = DoorNode([], 0, the_void, "n", (1430, 1116))
room_3408 = DoorNode([], 0, the_void, "e", (1438, 1140))

room_3121 = DoorNode([], 0, the_void, "w", (237, 898))
room_3120 = DoorNode([], 0, the_void, "w", (237, 961))
room_3119 = DoorNode([], 0, the_void, "w", (237, 991))
room_3118 = DoorNode([], 0, the_void, "w", (237, 1061))
room_3117 = DoorNode([], 0, the_void, "n", (295, 1105))
room_3122 = DoorNode([], 0, the_void, "s", (295, 898))

mbr3 = DoorNode([], 0, the_void, "w", (1249, 785))
fbr3 = DoorNode([], 0, the_void, "e", (463, 784))

room_4111 = DoorNode([], 0, the_void, "s", (445, 1153))
room_4117 = DoorNode([], 0, the_void, "w", (396, 1089))
room_4118 = DoorNode([], 0, the_void, "w", (396, 1002))
room_4119 = DoorNode([], 0, the_void, "w", (396, 972))
room_4120 = DoorNode([], 0, the_void, "w", (396, 884))
room_4121 = DoorNode([], 0, the_void, "w", (396, 787))
room_4122 = DoorNode([], 0, the_void, "n", (396, 787))# Placeholder
room_4105 = DoorNode([], 0, the_void, "e", (463, 890))
room_4104 = DoorNode([], 0, the_void, "s", (713, 1034))
room_4103 = DoorNode([], 0, the_void, "n", (719, 967))
room_4102 = DoorNode([], 0, the_void, "s", (837, 1034))
room_4101 = DoorNode([], 0, the_void, "n", (901, 952))
room_4401 = DoorNode([], 0, the_void, "s", (972, 1034))
room_4402 = DoorNode([], 0, the_void, "s", (1108, 1034))
room_4403 = DoorNode([], 0, the_void, "n", (1107, 967))
room_4405 = DoorNode([], 0, the_void, "s", (1137, 1034))
room_4410 = DoorNode([], 0, the_void, "e", (1316, 787))
room_4406 = DoorNode([], 0, the_void, "s", (1313, 1201))

mbr4 = DoorNode([], 0, the_void, "w", (1238, 776))
fbr4 = DoorNode([], 0, the_void, "e", (472, 776))

room_5101 = DoorNode([], 0, the_void, "s", (728, 1045))
room_5102 = DoorNode([], 0, the_void, "n", (712, 967))
room_5103 = DoorNode([], 0, the_void, "s", (788, 1045))
room_5104 = DoorNode([], 0, the_void, "n", (742, 967))
room_5105 = DoorNode([], 0, the_void, "n", (827, 967))
room_5405 = DoorNode([], 0, the_void, "s", (881, 1033))
room_5404 = DoorNode([], 0, the_void, "n", (982, 967))
room_5403 = DoorNode([], 0, the_void, "s", (937, 1045))
room_5402 = DoorNode([], 0, the_void, "n", (1011, 967))
room_5401 = DoorNode([], 0, the_void, "s", (996, 1045))

mbr5 = DoorNode([], 0, the_void, "w")
fbr5 = DoorNode([], 0, the_void, "e")

# Arts Building

room_0601 = DoorNode([], 0, the_void, "n")
room_0603 = DoorNode([], 0, the_void, "w")
room_0606 = DoorNode([], 0, the_void, "n")
room_0607 = DoorNode([], 0, the_void, "n")
room_0614 = DoorNode([], 0, the_void, "s")
room_0617 = DoorNode([], 0, the_void, "n")
room_0618 = DoorNode([], 0, the_void, "s")
room_0619 = DoorNode([], 0, the_void, "n")
room_0621 = DoorNode([], 0, the_void, "e")
room_0624 = DoorNode([], 0, the_void, "e")
room_0628 = DoorNode([], 0, the_void, "n")

room_1604 = DoorNode([], 0, the_void, "w")
room_1605 = DoorNode([], 0, the_void, "w")
room_1606 = DoorNode([], 0, the_void, "w")
room_1607 = DoorNode([], 0, the_void, "s")
room_1608 = DoorNode([], 0, the_void, "s")
room_1609 = DoorNode([], 0, the_void, "e")
room_1610 = DoorNode([], 0, the_void, "w")
room_1611 = DoorNode([], 0, the_void, "e")
room_1612 = DoorNode([], 0, the_void, "e")
room_1613 = DoorNode([], 0, the_void, "e")
room_1601 = DoorNode([], 0, the_void, "s")
room_1603 = DoorNode([], 0, the_void, "n")

room_2601 = DoorNode([], 0, the_void, "e", (883, 213))
room_2602 = DoorNode([], 0, the_void, "w", (620, 778))
room_2603 = DoorNode([], 0, the_void, "e", (705, 822))
room_2606 = DoorNode([], 0, the_void, "w", (620, 843))
room_2607 = DoorNode([], 0, the_void, "e", (705, 854))
room_2608 = DoorNode([], 0, the_void, "n", (600, 1252))
room_2609 = DoorNode([], 0, the_void, "e", (705, 1233))
room_2611 = DoorNode([], 0, the_void, "s", (631, 1425))
room_2612 = DoorNode([], 0, the_void, "s", (673, 1453))
room_2613 = DoorNode([], 0, the_void, "s", (865, 1310))
room_2614 = DoorNode([], 0, the_void, "s", (1406, 1310))
room_2615 = DoorNode([], 0, the_void, "n", (1310, 1253))
room_2616 = DoorNode([], 0, the_void, "s", (1435, 1429))
room_2617 = DoorNode([], 0, the_void, "e", (1522, 1307))
room_2618 = DoorNode([], 0, the_void, "e", (1522, 1048))
room_2619 = DoorNode([], 0, the_void, "w", (1458, 1039))
room_2620 = DoorNode([], 0, the_void, "e", (1522, 851))
room_2621 = DoorNode([], 0, the_void, "s", (1134, 837))
room_2622 = DoorNode([], 0, the_void, "e", (1522, 818))
room_2623 = DoorNode([], 0, the_void, "e", (1181, 561))
room_2624 = DoorNode([], 0, the_void, "n", (1074, 547))

room_3601 = DoorNode([], 0, the_void, "w")
room_3602 = DoorNode([], 0, the_void, "w")
room_3604 = DoorNode([], 0, the_void, "w")
room_3605 = DoorNode([], 0, the_void, "e")
room_3606 = DoorNode([], 0, the_void, "n")
room_3607 = DoorNode([], 0, the_void, "e")
room_3608 = DoorNode([], 0, the_void, "s")
room_3610 = DoorNode([], 0, the_void, "s")
room_3611 = DoorNode([], 0, the_void, "n")
room_3617 = DoorNode([], 0, the_void, "e")
room_3622 = DoorNode([], 0, the_void, "e")
room_3623 = DoorNode([], 0, the_void, "e")
room_3621 = DoorNode([], 0, the_void, "s")
room_3624 = DoorNode([], 0, the_void, "s")
room_3625 = DoorNode([], 0, the_void, "s")

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
    room_2414,
    room_2415,
    room_2412,
    room_2411,
    room_2132,
    room_2133,
    room_2134,
    room_2135,
    room_3124,
    room_3111,
    room_3103,
    room_3104,
    room_3101,
    room_3102,
    room_3401,
    room_3404,
    room_3402,
    room_3411,
    room_3412,
    room_3409,
    room_3408,
    room_3121,
    room_3120,
    room_3119,
    room_3118,
    room_3117,
    room_3122,
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
    room_5401,
    room_3601,
    room_3602,
    room_3604,
    room_3605,
    room_3606,
    room_3607,
    room_3608,
    room_3610,
    room_3611,
    room_3617,
    room_3622,
    room_3623,
    room_3621,
    room_3624,
    room_3625,
    room_2601,
    room_2602,
    room_2603,
    room_2606,
    room_2607,
    room_2608,
    room_2609,
    room_2611,
    room_2612,
    room_2613,
    room_2614,
    room_2615,
    room_2616,
    room_2617,
    room_2618,
    room_2619,
    room_2620,
    room_2621,
    room_2622,
    room_2623,
    room_2624,
    room_1604,
    room_1605,
    room_1606,
    room_1607,
    room_1608,
    room_1609,
    room_1610,
    room_1611,
    room_1612,
    room_1613,
    room_1601,
    room_1603,
    room_0601,
    room_0603,
    room_0606,
    room_0607,
    room_0614,
    room_0617,
    room_0618,
    room_0619,
    room_0621,
    room_0624,
    room_0628,
    mbr1,
    fbr1,
    career,
    library,
    main
]


async def build_doors():
    await room_1108.set_info([fl1, bl1, room_1202, stair3_f1], 1108, fl1, ["n", "s", "s", "s"])

    await room_1102.set_info([fl1, fr1, room_1105, room_1106, stair1_f1, room_1401, room_1402, room_1409, room_1410],
                             1102, fc1, ["e", "w", "e", "w", "w", "w", "w", "w", "w"])
    await room_1105.set_info([fl1, fr1, room_1102, room_1106, stair1_f1, room_1401, room_1402, room_1409, room_1410],
                             1105, fl1, ["e", "w", "w", "w", "w", "w", "w", "w", "w"])
    await room_1106.set_info([fr1, fl1, room_1105, room_1102, stair1_f1, room_1401, room_1402, room_1409, room_1410],
                             1106, fc1, ["w", "e", "e", "e", "w", "w", "w", "w", "w"])
    await room_1401.set_info([fl1, fr1, room_1409, room_1402, stair1_f1, room_1102, room_1105, room_1106, room_1410],
                             1401, fc1, ["e", "w", "w", "w", "e", "e", "e", "e", "w"])
    await room_1402.set_info([fl1, fr1, room_1401, room_1409, stair1_f1, room_1102, room_1105, room_1106, room_1410],
                             1402, fc1, ["e", "w", "e", "w", "e", "e", "e", "e", "w"])
    await room_1409.set_info([fl1, fr1, room_1401, room_1402, stair1_f1, room_1102, room_1105, room_1106, room_1410],
                             1409, fr1, ["e", "w", "e", "e", "e", "e", "e", "e", "w"])
    await room_1410.set_info([fl1, fr1, room_1401, room_1402, stair1_f1, room_1102, room_1105, room_1106, room_1409],
                             1410, fr1, ["e", "w", "e", "e", "e", "e", "e", "e", "e"])

    await room_1202.set_info([fl1, bl1, room_1108, stair3_f1, stair5_f1], 1202, fl1, ["n", "s", "n", "n", "s"])

    await room_1224.set_info([bl1, br1, room_1223, room_1225, room_1228, room_1311, room_1312], 1225, bc1,
                             ["e", "w", "e", "w", "w", "w", "w"])
    await room_1225.set_info([bl1, br1, room_1223, room_1224, room_1228, room_1311, room_1312], 1225, bc1,
                             ["e", "w", "e", "e", "w", "w", "w"])
    await room_1228.set_info([bl1, br1, room_1223, room_1224, room_1225, room_1311, room_1312], 1228, bc1,
                             ["e", "n", "e", "e", "e", "w", "w"])
    await room_1223.set_info([bl1, br1, room_1224, room_1225, room_1228, room_1311, room_1312], 1223, bl1,
                             ["e", "w", "w", "w", "w", "w", "w"])
    await room_1311.set_info([br1, bl1, room_1312, room_1223, room_1224, room_1225, room_1228], 1311, bc1,
                             ["w", "e", "w", "e", "e", "e", "e"])
    await room_1312.set_info([bl1, br1, room_1311, room_1223, room_1224, room_1225, room_1228], 1312, br1,
                             ["e", "w", "e", "e", "e", "e", "e"])

    await mbr1.set_info([br1, fr1, stair8_f1], 1, fr1, ["s", "n", "n"])
    await fbr1.set_info([fl1, bl1, stair3_f1, room_1202], 2, fl1, ["n", "s", "n", "n"])

    await career.set_info([fr1], 1501, the_void, ["s"])

    await main.set_info([fl1, fr1, room_1105, room_1106, room_1102, room_1401, room_1402, room_1409, room_1410], 9,
                        the_void, ["e", "w", "e", "e", "e", "w", "w", "w", "w"])

    await room_1107.set_info([fl1, room_1109], 1107, fl1, ["s", "n"])
    await room_1109.set_info([fl1, room_1107, stair2_f1], 1109, fl1, ["s", "s", "e"])
    await room_1420.set_info([fr1, stair9_f1], 1420, fr1, ["s", "s"])
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

    await room_2212.set_info([room_2202, room_2201, bl2, fl2, stair3_f2, stair5_f2], 2212, bl2, ['n', 'n', 's', 'n',
                                                                                                 'n', 's'])
    await room_2202.set_info([room_2212, room_2201, bl2, fl2, stair3_f2, stair5_f2], 2202, bl2, ['s', 'n', 's', 'n',
                                                                                                 'n', 's'])
    await room_2201.set_info([room_2212, room_2202, bl2, fl2, stair3_f2, stair5_f2], 2201, bl2, ['s', 's', 's', 'n',
                                                                                                 'n', 's'])

    await mbr2.set_info([br2, fr2, stair8_f2], 1, fr2, ["s", "n", "n"])
    await fbr2.set_info([fl1, bl1, stair3_f2, room_2201, room_2202], 2, fr2, ["n", "s", "n", "n", "s"])

    await library.set_info([fr2, atl2], 2501, the_void, ["s", "n"])

    await room_2119.set_info([fl2, stair2_f2], 2119, fl2, ['s', 'e'])

    sw8_f2 = StairwellNode(stair8_f2, [])
    await stair8_f2.add_connections([sw8_f2])
    sw9_f2 = StairwellNode(stair9_f2, [])
    await stair9_f2.add_connections([sw9_f2])

    await room_2414.set_info([sw8_f2, room_2415], 2414, sw8_f2, ["n", "w"])
    await room_2415.set_info([sw8_f2, room_2414], 2415, sw8_f2, ["n", "e"])
    await room_2412.set_info([sw9_f2, room_2412], 2412, sw9_f2, ["n", "w"])
    await room_2411.set_info([sw9_f2, room_2411], 2411, sw9_f2, ["n", "e"])

    await n2e.add_directions(the_void, stair3_f2, c2e, the_void)
    await c2e.add_directions(n2e, the_void, s2e, the_void)
    await s2e.add_directions(c2e, stair2_f2, the_void, the_void)

    await room_2132.set_info([s2e, c2e], 2132, s2e, ["w", "s"])
    await room_2133.set_info([room_2134, c2e], 2133, c2e, ["s", "w"])
    await room_2134.set_info([room_2133, c2e], 2134, c2e, ["n", "w"])
    await room_2135.set_info([n2e, c2e], 2135, n2e, ["w", "n"])

    await room_3124.set_info([l3, stair3_f3], 3124, l3, ['n', 's'])
    await room_3111.set_info([l3, stair3_f2], 3111, l3, ['s', 'e'])
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

    sw8_f3 = StairwellNode(stair8_f3, [])
    await stair8_f3.add_connections([sw8_f3])
    sw9_f3 = StairwellNode(stair9_f3, [])
    await stair9_f3.add_connections([sw9_f3])

    await room_3411.set_info([sw8_f3, room_3412], 3411, sw8_f3, ["n", "w"])
    await room_3412.set_info([sw8_f3, room_3411], 3412, sw8_f3, ["n", "e"])
    await room_3409.set_info([sw9_f3, room_3408], 3409, sw9_f3, ["n", "w"])
    await room_3408.set_info([sw9_f3, room_3409], 3408, sw9_f3, ["n", "e"])

    await room_3121.set_info([room_3120, room_3119, room_3118, room_3122, n3e, s3e], 3121, n3e,
                             ["n", "n", "n", "w", "w", "n"])
    await room_3120.set_info([room_3121, room_3119, room_3118, n3e, s3e], 3120, n3e,
                             ["s", "n", "n", "s", "n"])
    await room_3119.set_info([room_3121, room_3120, room_3118, n3e, s3e], 3119, n3e,
                             ["s", "s", "n", "s", "n"])
    await room_3118.set_info([room_3121, room_3120, room_3119, n3e, s3e], 3118, n3e,
                             ["s", "s", "s", "s", "n"])
    await room_3122.set_info([room_3121, n3e], 3122, n3e, ["e", "s"])
    await room_3117.set_info([s3e], 3117, s3e, ["n"])

    await mbr3.set_info([r3, stair8_f3], 1, the_void, ["n", "n"])
    await fbr3.set_info([l3, stair3_f3], 2, the_void, ["n", "n"])

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
    await room_4406.set_info([r3, stair9_f4], 4406, r4, ['s', 's'])

    await mbr4.set_info([r4, stair8_f4, room_4410], 1, the_void, ["n", "n", "w"])
    await fbr4.set_info([l4, stair3_f4, room_4121], 2, the_void, ["n", "n", "e"])

    await room_5102.set_info([room_5101, room_5104, room_5103, room_5104, room_5105, room_5405, room_5404, room_5403,
                              room_5402, room_5401, stair2_f5, stair9_f5], 5102, the_void, ['w', 'w', 'w', 'w', 'w',
                                                                                            'w', 'w', 'w', 'w', 'w',
                                                                                            'e', 'w'])
    await room_5101.set_info([room_5102, room_5104, room_5103, room_5104, room_5105, room_5405, room_5404, room_5403,
                              room_5402, room_5401, stair2_f5, stair9_f5], 5101, the_void, ['e', 's', 'w', 'w', 'w',
                                                                                            'w', 'w', 'w', 'w', 'w',
                                                                                            'e', 'w'])

    await room_0601.set_info([atl1, atr1], 601, the_void, ["e", "w"])
    await room_0603.set_info([stair11_f0, atl0], 603, the_void, ["s", "n"])
    await room_0606.set_info([room_0607, atl0, aml0], 606, the_void, ["e", "w", "e"])
    await room_0607.set_info([room_0606, atl0, aml0, abl0], 607, the_void, ["w", "w", "n", "n"])
    await room_0614.set_info([aml0, abl0, abr0], 614, the_void, ["s", "s", "w"])
    await room_0617.set_info([room_0618, room_0619, abl0, abr0], 617, the_void, ["n", "w", "e", "w"])
    await room_0618.set_info([room_0617, room_0619, abl0, abr0], 618, the_void, ["e", "e", "e", "w"])
    await room_0619.set_info([room_0617, room_0618, abl0, abr0], 619, the_void, ["e", "e", "e", "w"])
    await room_0621.set_info([room_0624, abr0, amr0], 621, the_void, ["s", "n", "s"])
    await room_0624.set_info([room_0621, abr0, amr0], 621, the_void, ["n", "n", "s"])
    await room_0628.set_info([amr0, atr0], 628, the_void, ["w", "e"])

    await room_1604.set_info([room_1605, room_1606, atl1, atr1], 1604, the_void, ["n", "n", "s", "n"])
    await room_1605.set_info([room_1604, room_1606, atl1, atr1], 1605, the_void, ["s", "n", "s", "n"])
    await room_1606.set_info([room_1604, room_1605, atl1, atr1], 1606, the_void, ["s", "s", "s", "n"])
    await room_1607.set_info([room_1608, abl1, abr1], 1607, the_void, ["w", "e", "w"])
    await room_1608.set_info([room_1607, abl1, abr1], 1608, the_void, ["e", "e", "w"])
    await room_1609.set_info([room_1610, room_1611, room_1612, room_1613, abr1, atr1], 1609, the_void,
                             ["s", "s", "s", "s", "n", "s"])
    await room_1610.set_info([room_1609, room_1611, room_1612, room_1613, abr1, atr1], 1610, the_void,
                             ["n", "w", "s", "s", "n", "s"])
    await room_1611.set_info([room_1609, room_1610, room_1612, room_1613, abr1, atr1], 1611, the_void,
                             ["n", "e", "s", "s", "n", "s"])
    await room_1612.set_info([room_1609, room_1610, room_1611, room_1613, abr1, atr1], 1612, the_void,
                             ["n", "n", "n", "s", "n", "s"])
    await room_1613.set_info([room_1609, room_1610, room_1611, room_1613, abr1, atr1], 1613, the_void,
                             ["n", "n", "n", "n", "n", "s"])
    await room_1603.set_info([room_1601, af1, atr1], 1603, the_void, ["n", "e", "w"])
    await room_1601.set_info([room_1603, af1, atr1, atl1], 1601, the_void, ["s", "s", "w", "e"])

    await room_2601.set_info([fr2, stair9_f2, atl2], 2601, the_void, ["s", "s", "n"])
    await room_2602.set_info([room_2603, room_2606, room_2607, room_2609, atl2, abl2], 2602, the_void,
                             ["w", "w", "n", "n", "s", "n"])
    await room_2603.set_info([room_2602, room_2606, room_2607, room_2609, atl2, abl2], 2603, the_void,
                             ["e", "e", "n", "n", "s", "n"])
    await room_2606.set_info([room_2602, room_2603, room_2607, room_2609, atl2, abl2], 2606, the_void,
                             ["w", "w", "n", "n", "s", "n"])
    await room_2607.set_info([room_2602, room_2603, room_2606, room_2609, atl2, abl2], 2607, the_void,
                             ["s", "s", "s", "n", "s", "n"])
    await room_2609.set_info([room_2602, room_2603, room_2606, room_2607, atl2, abl2], 2609, the_void,
                             ["s", "s", "s", "s", "s", "n"])
    await room_2608.set_info([abl2], 2608, the_void, ["w"])
    await room_2613.set_info([room_2614, room_2615, abl2, abr2], 2613, the_void, ["w", "w", "e", "w"])
    await room_2614.set_info([room_2613, room_2615, abl2, abr2], 2614, the_void, ["e", "e", "e", "w"])
    await room_2615.set_info([room_2613, room_2614, abl2, abr2], 2615, the_void, ["e", "e", "w", "w"])
    await room_2617.set_info([room_2618, room_2619, room_2620, room_2622, abr2, atr2], 2617, the_void,
                             ["s", "s", "s", "s", "e", "s"])
    await room_2618.set_info([room_2617, room_2619, room_2620, room_2622, abr2, atr2], 2618, the_void,
                             ["n", "e", "s", "s", "n", "s"])
    await room_2619.set_info([room_2617, room_2618, room_2620, room_2622, abr2, atr2], 2619, the_void,
                             ["n", "w", "s", "s", "n", "s"])
    await room_2620.set_info([room_2617, room_2618, room_2619, room_2622, abr2, atr2], 2620, the_void,
                             ["n", "n", "n", "s", "n", "s"])
    await room_2622.set_info([room_2617, room_2618, room_2619, room_2620, abr2, atr2], 2622, the_void,
                             ["n", "n", "n", "n", "n", "e"])
    await room_2621.set_info([amb2, amt2, atr2, room_2623], 2621, the_void, ["s", "s", "w", "s"])
    await room_2623.set_info([amt2, amb2, atl2, room_2621], 2623, the_void, ["e", "n", "e", "n"])
    await room_2624.set_info([amb2, atl2], 2624, the_void, ["w", "e"])

    await room_3601.set_info([atl3, amt3], 3601, the_void, ["w", "w"])
    await room_3602.set_info([room_3604, room_3605, room_3607, atll3, abl3], 3602, the_void,
                             ["n", "n", "n", "s", "n"])
    await room_3604.set_info([room_3602, room_3605, room_3607, atll3, abl3], 3604, the_void,
                             ["s", "w", "n", "s", "n"])
    await room_3605.set_info([room_3602, room_3604, room_3607, atll3, abl3], 3605, the_void,
                             ["s", "e", "n", "s", "n"])
    await room_3607.set_info([room_3602, room_3604, room_3605, atll3, abl3], 3607, the_void,
                             ["s", "s", "s", "s", "n"])
    await room_3606.set_info([room_3608, abl3, stair14_f3], 3606, the_void, ["n", "w", "n"])
    await room_3608.set_info([room_3606, abl3, stair14_f3], 3608, the_void, ["s", "w", "n"])
    await room_3610.set_info([room_3611, abl3, abr3], 3610, the_void, ["w", "e", "w"])
    await room_3611.set_info([room_3610, abl3, abr3], 3611, the_void, ["e", "e", "w"])
    await room_3617.set_info([room_3622, room_3623, abr3, atr3], 3617, the_void, ["s", "s", "n", "s"])
    await room_3622.set_info([room_3617, room_3623, abr3, atr3], 3622, the_void, ["n", "s", "n", "s"])
    await room_3623.set_info([room_3617, room_3622, atr3], 3622, the_void, ["n", "n", "n"])
    await room_3621.set_info([room_3624, amb3, atr3], 3621, the_void, ["e", "e", "w"])
    await room_3624.set_info([room_3621, amb3, atr3], 3624, the_void, ["w", "e", "w"])
    await room_3625.set_info([atl3, amt3], 3625, the_void, ["e", "w"])


async def build_school():
    await fr1.add_directions([stair8_f1, br1], the_void, stair9_f1, [stair1_f1, fl1])
    await fl1.add_directions([stair3_f1, bl1], [stair1_f1, fr1], stair2_f1, the_void)
    await br1.add_directions(stair6_f1, the_void, [stair8_f1, fr1], bl1)
    await bl1.add_directions(stair5_f1, br1, [stair3_f1, fl1], the_void)

    await fr2.add_directions([stair8_f2, br2], the_void, [stair9_f2, atl2], fl2)
    await fl2.add_directions([stair3_f2, bl2], fr2, stair2_f2, the_void)
    await br2.add_directions(stair6_f2, the_void, [stair9_f2, fr2], bl2)
    await bl2.add_directions(stair5_f2, br2, [stair3_f2, fl2], the_void)

    await n2e.add_directions(the_void, stair3_f2, s2e, the_void)
    await s2e.add_directions(n2e, stair2_f2, the_void, the_void)

    await l3.add_directions(stair3_f3, r3, stair2_f3, the_void)
    await r3.add_directions(stair8_f3, the_void, stair9_f3, l3)

    await n3e.add_directions(the_void, stair3_f3, s3e, the_void)
    await s3e.add_directions(n3e, stair2_f3, the_void, the_void)

    await l4.add_directions(stair3_f4, r4, stair2_f4, the_void)
    await r4.add_directions(stair8_f4, the_void, stair9_f4, l4)

    await atl0.add_directions(stair11_f0, atr0, the_void, aml0)
    await aml0.add_directions(the_void, atl0, abl0, the_void)
    await abl0.add_directions(aml0, abr0, stair14_f0, the_void)
    await abr0.add_directions(amr0, the_void, stair17_f0, abl0)
    await amr0.add_directions(the_void, the_void, abr0, atr0)
    await atr0.add_directions(the_void, amr0, the_void, atl0)

    await af1.add_directions(stair11_f1, atr1, atl1, the_void)
    await atl1.add_directions(the_void, af1, abl1, the_void)
    await abl1.add_directions(atl1, abr1, stair14_f1, the_void)
    await abr1.add_directions(atr1, the_void, stair17_f1, abl1)
    await atr1.add_directions(the_void, the_void, abr1, af1)

    await atl2.add_directions([stair11_f2, fr2], amt2, abl2, the_void)
    await abl2.add_directions(atl2, abr2, stair14_f2, the_void)
    await abr2.add_directions(atr2, the_void, stair17_f2, abl2)
    await atr2.add_directions(the_void, the_void, abr2, amb2)
    await amb2.add_directions(amt2, atr2, the_void, the_void)
    await amt2.add_directions(the_void, the_void, amb2, atl2)

    await atl3.add_directions([stair11_f3, r3], amt3, the_void, atll3)
    await atll3.add_directions(the_void, atl3, abl3, the_void)
    await abl3.add_directions(atll3, abr3, stair14_f3, the_void)
    await abr3.add_directions(atr3, the_void, stair17_f3, abl3)
    await atr3.add_directions(the_void, the_void, abr3, amb3)
    await amb3.add_directions(amt3, atr3, the_void, the_void)
    await amt3.add_directions(the_void, the_void, amb3, atl3)

    await stair1_f1.add_directions(the_void, fr1, fc1, fl1, stair1_f2, the_void)
    await stair1_f2.add_directions(the_void, fr2, the_void, fl2, stair1_f3, stair1_f1)
    await stair1_f3.add_directions(the_void, r3, the_void, l3, stair1_f4, stair1_f2)
    await stair1_f4.add_directions(the_void, r4, the_void, l4, the_void, stair1_f3)

    await stair2_f1.add_directions(fl1, the_void, the_void, the_void, stair2_f2, the_void)
    await stair2_f2.add_directions(fl2, the_void, the_void, s2e, stair2_f3, stair2_f1)
    await stair2_f3.add_directions(l3, the_void, the_void, s3e, stair2_f4, stair2_f2)
    await stair2_f4.add_directions(l4, the_void, the_void, the_void, stair2_f5, stair2_f3)
    await stair2_f5.add_directions(the_void, the_void, the_void, the_void, the_void, stair2_f4)

    await stair3_f1.add_directions(bl1, the_void, fl1, the_void, stair3_f2, the_void)
    await stair3_f2.add_directions(bl2, the_void, fl2, n2e, stair3_f3, stair3_f1)
    await stair3_f3.add_directions(the_void, the_void, l3, n3e, stair3_f4, stair3_f2)
    await stair3_f4.add_directions(the_void, the_void, l4, the_void, the_void, stair3_f4)

    await stair5_f1.add_directions(the_void, the_void, bl1, the_void, stair5_f2, the_void)
    await stair5_f2.add_directions(the_void, the_void, bl2, the_void, the_void, stair5_f1)

    await stair6_f1.add_directions(the_void, the_void, br1, the_void, stair6_f2, the_void)
    await stair6_f2.add_directions(the_void, the_void, br2, the_void, the_void, stair6_f1)

    await stair8_f1.add_directions(br1, the_void, fr1, the_void, stair8_f2, the_void)
    await stair8_f2.add_directions(br2, the_void, fr2, the_void, stair8_f3, stair8_f2)
    await stair8_f3.add_directions(the_void, the_void, r3, the_void, stair8_f4, stair8_f2)
    await stair8_f4.add_directions(the_void, the_void, r4, the_void, the_void, stair8_f3)

    await stair9_f1.add_directions(fr1, the_void, the_void, the_void, stair9_f2, the_void)
    await stair9_f2.add_directions(fr2, the_void, abl2, the_void, stair9_f3, stair9_f1)
    await stair9_f3.add_directions(r3, the_void, the_void, the_void, stair9_f4, stair9_f2)
    await stair9_f4.add_directions(r4, the_void, the_void, the_void, stair9_f5, stair9_f3)
    await stair9_f5.add_directions(the_void, the_void, the_void, the_void, the_void, stair9_f4)

    await stair11_f3.add_directions(the_void, the_void, atl3, the_void, the_void, stair11_f2)
    await stair11_f2.add_directions(fr2, the_void, atl2, the_void, stair11_f3, stair11_f1)
    await stair11_f1.add_directions(the_void, the_void, af1, the_void, stair11_f2, stair11_f0)
    await stair11_f0.add_directions(the_void, the_void, atl0, the_void, stair11_f1, the_void)

    await stair14_f3.add_directions(abl3, the_void, the_void, the_void, the_void, stair14_f2)
    await stair14_f2.add_directions(abl2, the_void, the_void, the_void, stair14_f3, stair14_f1)
    await stair14_f1.add_directions(abl1, the_void, the_void, the_void, stair14_f2, stair14_f0)
    await stair14_f0.add_directions(abl0, the_void, the_void, the_void, stair14_f1, the_void)

    await stair17_f3.add_directions(abr3, the_void, the_void, the_void, the_void, stair17_f2)
    await stair17_f2.add_directions(abr2, the_void, the_void, the_void, stair17_f3, stair17_f1)
    await stair17_f1.add_directions(abr1, the_void, the_void, the_void, stair17_f2, stair17_f0)
    await stair17_f0.add_directions(abr0, the_void, the_void, the_void, stair17_f1, the_void)

    await build_doors()