from enum import Enum

from pydantic import BaseModel


class Level(Enum):
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


class PreciousResource(Enum):
    ARC_SAND_ORE = "アーク砂鉱"
    AURORITE = "オーロラ石"
    BOILED_EGG_ORE = "ボイルドエッグ鉱石"
    BONJELIUM = "バンドジェリウム"
    CIMMERIAN_CINNABAR = "暗黒辰砂"
    DAWNSTONE = "ドーンナイト"
    ENDURON_LEAD = "エンデュロ鉛"
    EVERFREEZE_ORE = "千年氷鉱"
    FOUCAULTIUM = "フーコイト鉱石"
    INFERNIUM = "ヘルファイアゲート"
    LIONBONE_BORT = "獅子骨石"
    MARINE_RUTILE = "アクアルチル"
    OUROBOROS_CRYSTAL = "ウロボロス結晶"
    PARHELION_PLATINUM = "幻日白金"
    WHITE_COMETITE = "白彗星鉱石"


class SpotInformation(BaseModel):
    production: Level
    profit: Level
    support: Level
    secret_spots: int
    precious_resources: list[PreciousResource]


FRONTIER_NETWORK_SPOT: list[SpotInformation | None] = [None] * 517

FRONTIER_NETWORK_SPOT[101] = SpotInformation(
    production=Level.C,
    profit=Level.A,
    support=Level.S,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[102] = SpotInformation(
    production=Level.C,
    profit=Level.F,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[103] = SpotInformation(
    production=Level.C,
    profit=Level.E,
    support=Level.A,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[104] = SpotInformation(
    production=Level.C,
    profit=Level.A,
    support=Level.B,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[105] = SpotInformation(
    production=Level.A,
    profit=Level.F,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[106] = SpotInformation(
    production=Level.B,
    profit=Level.E,
    support=Level.B,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[107] = SpotInformation(
    production=Level.A,
    profit=Level.F,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[108] = SpotInformation(
    production=Level.C,
    profit=Level.F,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[109] = SpotInformation(
    production=Level.C,
    profit=Level.D,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[110] = SpotInformation(
    production=Level.C,
    profit=Level.E,
    support=Level.B,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[111] = SpotInformation(
    production=Level.C,
    profit=Level.F,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[112] = SpotInformation(
    production=Level.A,
    profit=Level.F,
    support=Level.A,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[113] = SpotInformation(
    production=Level.C,
    profit=Level.C,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[114] = SpotInformation(
    production=Level.C,
    profit=Level.E,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[115] = SpotInformation(
    production=Level.C,
    profit=Level.D,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[116] = SpotInformation(
    production=Level.A,
    profit=Level.D,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[117] = SpotInformation(
    production=Level.A,
    profit=Level.D,
    support=Level.A,
    secret_spots=1,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[118] = SpotInformation(
    production=Level.C,
    profit=Level.E,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[119] = SpotInformation(
    production=Level.C,
    profit=Level.E,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[120] = SpotInformation(
    production=Level.B,
    profit=Level.B,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[121] = SpotInformation(
    production=Level.A,
    profit=Level.E,
    support=Level.B,
    secret_spots=0,
    precious_resources=[],
)

FRONTIER_NETWORK_SPOT[201] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[202] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[203] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[204] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[205] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[206] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[207] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[208] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[209] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[210] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[211] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[212] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[213] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[214] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[215] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[216] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[217] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[218] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[219] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[220] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[221] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[222] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[223] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[224] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[225] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)

FRONTIER_NETWORK_SPOT[301] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[302] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[303] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[304] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[305] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[306] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[307] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[308] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[309] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[310] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[311] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[312] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[313] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[314] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[315] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[316] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[317] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[318] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[319] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[320] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[321] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[322] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)

FRONTIER_NETWORK_SPOT[401] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[402] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[403] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[404] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[405] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[406] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[407] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[408] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[409] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[410] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[411] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[412] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[413] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[414] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[415] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[416] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[417] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[418] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[419] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[420] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)

FRONTIER_NETWORK_SPOT[501] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[502] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[503] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[504] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[505] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[506] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[507] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[508] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[509] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[510] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[511] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[512] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[513] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[514] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[515] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)
FRONTIER_NETWORK_SPOT[516] = SpotInformation(
    production=Level.S,
    profit=Level.S,
    support=Level.S,
    secret_spots=0,
    precious_resources=[],
)


class FrontierNetwork:
    NETWORK: dict[int, list[int]] = {
        101: [105],
        102: [105, 106, 222],
        103: [104],
        104: [103, 106],
        105: [101, 102, 109],
        106: [102, 104, 107],
        107: [106, 110],
        108: [109],
        109: [105, 108],
        110: [107, 111, 112],
        111: [110, 113],
        112: [110, 114, 115],
        113: [111, 409],
        114: [112, 116],
        115: [112],
        116: [114, 117],
        117: [116, 118, 120],
        118: [117, 121],
        119: [120],
        120: [117, 119],
        121: [118, 301],
        201: [206],
        202: [203, 207, 208],
        203: [202, 204],
        204: [203, 205, 211, 212],
        205: [204, 209],
        206: [201, 207, 213],
        207: [206, 202],
        208: [202],
        209: [205],
        210: [211],
        211: [210, 204],
        212: [204, 216],
        213: [206],
        214: [215],
        215: [214, 218],
        216: [212, 218, 225],
        217: [222],
        218: [215, 216, 224],
        219: [220],
        220: [219, 221, 225],
        221: [220, 222],
        222: [217, 221, 102],
        223: [224],
        224: [223, 218],
        225: [216, 220],
        301: [121, 302, 303],
        302: [301],
        303: [301, 306],
        304: [305, 306, 309],
        305: [304, 308],
        306: [303, 304, 307],
        307: [306, 313],
        308: [305],
        309: [304, 311],
        310: [311],
        311: [309, 310],
        312: [313, 315],
        313: [307, 312, 314],
        314: [313],
        315: [312, 316, 318, 321],
        316: [315],
        317: [318, 319],
        318: [315, 317],
        319: [317],
        320: [321],
        321: [315, 320, 322],
        322: [321],
        401: [402, 404],
        402: [401, 408],
        403: [405],
        404: [401, 407],
        405: [403, 408, 409],
        406: [408],
        407: [404, 412],
        408: [402, 405, 406, 413],
        409: [113, 405, 411],
        410: [412],
        411: [409, 414],
        412: [407, 410, 415],
        413: [408, 416],
        414: [411],
        415: [412, 502],
        416: [413, 418, 419],
        417: [419],
        418: [416],
        419: [416, 417, 420],
        420: [419],
        501: [502],
        502: [415, 501, 503],
        503: [502, 504],
        504: [503, 508],
        505: [506, 509],
        506: [505],
        507: [508],
        508: [504, 507, 509, 511],
        509: [505, 508, 510, 513],
        510: [509],
        511: [508, 512, 514],
        512: [511],
        513: [509, 516],
        514: [511, 515],
        515: [514],
        516: [513],
    }
