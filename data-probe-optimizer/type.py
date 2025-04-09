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


class FrontierNetwork:
    def __init__(self) -> None:
        self.sites: list[Site | None] = [None] * 517
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
