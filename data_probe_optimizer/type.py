from enum import Enum
from pathlib import Path

import pandas
from pydantic import BaseModel


class DataProbePaths:
    SITES = Path(__file__).parent / "sites.tsv"


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
    MINING = 0
    RESEARCH = 1
    BOOST = 2
    STORAGE = 3
    DUPLICATE = 4


class Probe(BaseModel):
    production: float = 0.5
    profit: float = 0.5
    storage: int = 0

    boost: float = 1

    type: ProbeType

    def __hash__(self) -> int:
        return int(
            self.production * 10
            + self.profit * 10 * 100
            + self.storage * 100000
            + self.boost * 10000
        )


class Probes:
    BASIC = Probe(type=ProbeType.MINING)

    RESEARCH_1 = Probe(production=0.3, profit=2, type=ProbeType.RESEARCH)
    RESEARCH_2 = Probe(production=0.3, profit=2.5, type=ProbeType.RESEARCH)
    RESEARCH_3 = Probe(production=0.3, profit=3, type=ProbeType.RESEARCH)
    RESEARCH_4 = Probe(production=0.3, profit=3.5, type=ProbeType.RESEARCH)
    RESEARCH_5 = Probe(production=0.3, profit=4, type=ProbeType.RESEARCH)
    RESEARCH_6 = Probe(production=0.3, profit=4.5, type=ProbeType.RESEARCH)

    BOOST_1 = Probe(production=0.1, profit=0.1, boost=1.5, type=ProbeType.BOOST)
    BOOST_2 = Probe(production=0.1, profit=0.1, boost=2, type=ProbeType.BOOST)

    DUPLICATE = Probe(production=0, profit=0, type=ProbeType.DUPLICATE)

    STORAGE = Probe(production=0.1, profit=0.1, storage=3000, type=ProbeType.STORAGE)


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
