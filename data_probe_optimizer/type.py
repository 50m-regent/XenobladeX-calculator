from enum import Enum
from pathlib import Path

import pandas
from pydantic import BaseModel


class DataProbePaths:
    # SITES = Path(__file__).parent / "sites.tsv"
    SITES = Path(__file__).parent / "sites_small.tsv"


class Level(Enum):
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


class PreciousResource(Enum):
    ARC_SAND_ORE = "Arc Sand Ore"
    AURORITE = "Aurorite"
    BOILED_EGG_ORE = "Boiled-Egg Ore"
    BONJELIUM = "Bonjelium"
    CIMMERIAN_CINNABAR = "Cimmerian Cinnabar"
    DAWNSTONE = "Dawnstone"
    ENDURON_LEAD = "Enduron Lead"
    EVERFREEZE_ORE = "Everfreeze Ore"
    FOUCAULTIUM = "Foucaltium"
    INFERNIUM = "Infernium"
    LIONBONE_BORT = "Lionbone Bort"
    MARINE_RUTILE = "Marine Rutile"
    OUROBOROS_CRYSTAL = "Ouroboros Crystal"
    PARHELION_PLATINUM = "Parhelion Platinum"
    WHITE_COMETITE = "White Cometite"

    @property
    def jp(self) -> str:
        match self:
            case PreciousResource.ARC_SAND_ORE:
                return "アーク砂鉱"
            case PreciousResource.AURORITE:
                return "オーロラ石"
            case PreciousResource.BOILED_EGG_ORE:
                return "ボイルドエッグ鉱石"
            case PreciousResource.BONJELIUM:
                return "バンドジェリウム"
            case PreciousResource.CIMMERIAN_CINNABAR:
                return "暗黒辰砂"
            case PreciousResource.DAWNSTONE:
                return "ドーンナイト"
            case PreciousResource.ENDURON_LEAD:
                return "エンデュロ鉛"
            case PreciousResource.EVERFREEZE_ORE:
                return "千年氷鉱"
            case PreciousResource.FOUCAULTIUM:
                return "フーコイト鉱石"
            case PreciousResource.INFERNIUM:
                return "ヘルファイアゲート"
            case PreciousResource.LIONBONE_BORT:
                return "獅子骨石"
            case PreciousResource.MARINE_RUTILE:
                return "アクアルチル"
            case PreciousResource.OUROBOROS_CRYSTAL:
                return "ウロボロス結晶"
            case PreciousResource.PARHELION_PLATINUM:
                return "幻日白金"
            case PreciousResource.WHITE_COMETITE:
                return "白彗星鉱石"


class Site(BaseModel):
    production: Level
    profit: Level
    secret_spots: int
    precious_resources: set[PreciousResource]
    connection: set[int]

    @property
    def profit_value(self) -> int:
        match self.profit:
            case Level.S:
                return 0
            case Level.A:
                return 750
            case Level.B:
                return 650
            case Level.C:
                return 550
            case Level.D:
                return 450
            case Level.E:
                return 300
            case Level.F:
                return 200


class ProbeType(Enum):
    BASIC = 0
    MINING = 1
    RESEARCH = 2
    BOOST = 3
    STORAGE = 4
    DUPLICATE = 5


class Probe(BaseModel):
    name: str

    production: float = 0.5
    profit: float = 0.5
    storage: int = 0

    boost: float = 1

    type: ProbeType


class Probes:
    BASIC = Probe(name="basic", type=ProbeType.BASIC)

    RESEARCH_1 = Probe(
        name="research_1", production=0.3, profit=2, type=ProbeType.RESEARCH
    )
    RESEARCH_2 = Probe(
        name="research_2", production=0.3, profit=2.5, type=ProbeType.RESEARCH
    )
    RESEARCH_3 = Probe(
        name="research_3", production=0.3, profit=3, type=ProbeType.RESEARCH
    )
    RESEARCH_4 = Probe(
        name="research_4", production=0.3, profit=3.5, type=ProbeType.RESEARCH
    )
    RESEARCH_5 = Probe(
        name="research_5", production=0.3, profit=4, type=ProbeType.RESEARCH
    )
    RESEARCH_6 = Probe(
        name="research_6", production=0.3, profit=4.5, type=ProbeType.RESEARCH
    )

    BOOST_1 = Probe(
        name="boost_1", production=0.1, profit=0.1, boost=1.5, type=ProbeType.BOOST
    )
    BOOST_2 = Probe(
        name="boost_2", production=0.1, profit=0.1, boost=2, type=ProbeType.BOOST
    )

    DUPLICATE = Probe(
        name="duplicate", production=0, profit=0, type=ProbeType.DUPLICATE
    )

    STORAGE = Probe(
        name="storage", production=0.1, profit=0.1, storage=3000, type=ProbeType.STORAGE
    )

    @staticmethod
    def from_name(name: str) -> Probe:
        match name:
            case "research_1":
                return Probes.RESEARCH_1
            case "research_2":
                return Probes.RESEARCH_2
            case "research_3":
                return Probes.RESEARCH_3
            case "research_4":
                return Probes.RESEARCH_4
            case "research_5":
                return Probes.RESEARCH_5
            case "research_6":
                return Probes.RESEARCH_6
            case "boost_1":
                return Probes.BOOST_1
            case "boost_2":
                return Probes.BOOST_2
            case "duplicate":
                return Probes.DUPLICATE
            case "storage":
                return Probes.STORAGE
            case _:
                raise NameError(f"Wrong probe name: {name}")


class Inventory(BaseModel):
    research_1: int = 0
    research_2: int = 0
    research_3: int = 0
    research_4: int = 0
    research_5: int = 0
    research_6: int = 0

    boost_1: int = 0
    boost_2: int = 0

    duplicate: int = 0

    storage: int = 0

    def __repr__(self) -> str:
        output = ""
        for attr in self:
            if attr[-1]:
                output += f"{attr[0]}: {attr[-1]}, "

        if not len(output):
            return "empty"
        return "(" + output.removesuffix(", ") + ")"

    def __str__(self) -> str:
        output = ""
        for attr in self:
            if attr[-1]:
                output += f"{attr[0]}: {attr[-1]}, "

        if not len(output):
            return "empty"
        return output.removesuffix(", ")


class FrontierNetwork:
    def __init__(self) -> None:
        self.sites: dict[int, Site] = {}
        for record in pandas.read_csv(DataProbePaths.SITES, sep="\t").to_dict(
            orient="records"
        ):
            self.sites[record["Site"]] = Site(
                production=record["M"],
                profit=record["G"],
                secret_spots=record["Sightseeing Spots"],
                precious_resources=set()
                if record["Rare Resources"] == " "
                else {
                    precious_resource.strip()
                    for precious_resource in record["Rare Resources"].split(",")
                },
                connection={int(site) for site in record["Connections"].split(",")},
            )


class Value(BaseModel):
    profit: int
    storage: int
    resource: set[PreciousResource]


class Library:
    def __init__(self) -> None:
        self.library: dict[
            int,
            dict[
                int,
                dict[
                    int,
                    dict[
                        int,
                        dict[
                            int,
                            dict[
                                int,
                                dict[
                                    int,
                                    dict[
                                        int,
                                        dict[int, dict[int, list[dict[int, Probe]]]],
                                    ],
                                ],
                            ],
                        ],
                    ],
                ],
            ],
        ] = {}

    def __contains__(self, inventory: Inventory) -> bool:
        library = self.library
        if inventory.research_1 not in library:
            return False

        library = library[inventory.research_1]
        if inventory.research_2 not in library:
            return False

        library = library[inventory.research_2]
        if inventory.research_3 not in library:
            return False

        library = library[inventory.research_3]
        if inventory.research_4 not in library:
            return False

        library = library[inventory.research_4]
        if inventory.research_5 not in library:
            return False

        library = library[inventory.research_5]
        if inventory.research_6 not in library:
            return False

        library = library[inventory.research_6]
        if inventory.boost_1 not in library:
            return False

        library = library[inventory.boost_1]
        if inventory.boost_2 not in library:
            return False

        library = library[inventory.boost_2]
        if inventory.duplicate not in library:
            return False

        library = library[inventory.duplicate]
        return inventory.storage in library

    def __getitem__(self, key: Inventory) -> list[dict[int, Probe]]:
        return self.library[key.research_1][key.research_2][key.research_3][
            key.research_4
        ][key.research_5][key.research_6][key.boost_1][key.boost_2][key.duplicate][
            key.storage
        ]

    def __setitem__(self, key: Inventory, value: list[dict[int, Probe]]) -> None:
        library = self.library
        if key.research_1 not in library:
            library[key.research_1] = {}

        library = library[key.research_1]
        if key.research_2 not in library:
            library[key.research_2] = {}

        library = library[key.research_2]
        if key.research_3 not in library:
            library[key.research_3] = {}

        library = library[key.research_3]
        if key.research_4 not in library:
            library[key.research_4] = {}

        library = library[key.research_4]
        if key.research_5 not in library:
            library[key.research_5] = {}

        library = library[key.research_5]
        if key.research_6 not in library:
            library[key.research_6] = {}

        library = library[key.research_6]
        if key.boost_1 not in library:
            library[key.boost_1] = {}

        library = library[key.boost_1]
        if key.boost_2 not in library:
            library[key.boost_2] = {}

        library = library[key.boost_2]
        if key.duplicate not in library:
            library[key.duplicate] = {}

        library[key.duplicate][key.storage] = value
