from __future__ import annotations

from pydantic import BaseModel

from .type import FrontierNetwork, Probe, ProbeType, Value, PreciousResource
from .constants import BASIC_PROFITS

network = FrontierNetwork()


class Node(BaseModel):
    children: list[Node] = []
    probe: Probe


class ProbeTree:
    def __init__(self, probes: dict[int, Probe]) -> None:
        for site in probes:
            if probes[site].type == ProbeType.BASIC:
                probes.pop(site)

        start = next(iter(probes))
        path = ProbeTree.__get_longest_path(start, probes)
        path = ProbeTree.__get_longest_path(path[-1], probes)

        center = path[len(path) // 2]

        self.root = self.__create_tree(center, probes)

    @staticmethod
    def __get_longest_path(
        now: int, probes: dict[int, Probe], root: int = 0
    ) -> list[int]:
        path = [now]
        longest = []
        for neighbor in network.sites[now].connection:
            if neighbor == root:
                continue
            if neighbor not in probes:
                continue

            candidate = ProbeTree.__get_longest_path(neighbor, probes, now)
            if len(candidate) > len(longest):
                longest = candidate

        return path + longest

    @staticmethod
    def __create_tree(now: int, probes: dict[int, Probe], parent: int = 0) -> Node:
        node = Node(probe=probes[now])

        for neighbor in network.sites[now].connection:
            if neighbor == parent:
                continue
            if neighbor not in probes:
                continue
            node.children.append(ProbeTree.__create_tree(neighbor, probes, now))

        return node


class ValueCalculator:
    resources = {
        PreciousResource.ARC_SAND_ORE,
        PreciousResource.AURORITE,
        PreciousResource.BOILED_EGG_ORE,
        PreciousResource.BONJELIUM,
        PreciousResource.CIMMERIAN_CINNABAR,
        PreciousResource.DAWNSTONE,
        PreciousResource.ENDURON_LEAD,
        PreciousResource.EVERFREEZE_ORE,
        PreciousResource.FOUCAULTIUM,
        PreciousResource.INFERNIUM,
        PreciousResource.LIONBONE_BORT,
        PreciousResource.MARINE_RUTILE,
        PreciousResource.OUROBOROS_CRYSTAL,
        PreciousResource.PARHELION_PLATINUM,
        PreciousResource.WHITE_COMETITE,
    }

    def __init__(self) -> None:
        pass

    def __calculate_combo_size(
        self,
        site: int,
        probes: dict[int, Probe],
        root: int | None = None,
    ) -> int:
        if not root:
            root = site

        if site not in probes:
            return 0

        if probes[site].name != probes[root].name:
            return 0
        else:
            combo_size = 1

        for neighbor in network.sites[site].connection:
            if neighbor == root:
                continue
            combo_size += self.__calculate_combo_size(neighbor, probes, root=site)

        return combo_size

    def __calculate_combo_bonus(self, site: int, probes: dict[int, Probe]) -> float:
        match self.__calculate_combo_size(site, probes):
            case 1 | 2:
                return 1
            case 3 | 4:
                return 1.3
            case 5 | 6 | 7:
                return 1.5
            case _:
                return 1.8

    def __calculate_boost(self, site: int, probes: dict[int, Probe]) -> float:
        if site not in probes:
            return 1

        boost = probes[site].boost
        if probes[site].type == ProbeType.DUPLICATE:
            for neighbor in network.sites[site].connection:
                if neighbor not in probes:
                    continue
                boost *= probes[neighbor].boost

        if boost > 1:
            return boost * self.__calculate_combo_bonus(site, probes)

        return boost

    def __calculate_profit(self, site: int, probes: dict[int, Probe]) -> int:
        profit = probes[site].profit
        profit_value = network.sites[site].profit_value

        if probes[site].type == ProbeType.DUPLICATE:
            for neighbor in network.sites[site].connection:
                if neighbor not in probes:
                    continue
                if probes[neighbor].type != ProbeType.RESEARCH:
                    continue

                profit += probes[neighbor].profit

        if profit < 2:
            return int(profit * profit_value)

        profit_value += 1000 * network.sites[site].secret_spots

        for neighbor in network.sites[site].connection:
            profit *= self.__calculate_boost(neighbor, probes)

        profit *= self.__calculate_combo_bonus(site, probes)

        return int(profit * profit_value)

    def __calculate_storage(self, site: int, probes: dict[int, Probe]) -> int:
        storage = probes[site].storage
        if probes[site].type == ProbeType.DUPLICATE:
            for neighbor in network.sites[site].connection:
                if neighbor not in probes:
                    continue
                if probes[neighbor].type != ProbeType.STORAGE:
                    continue

                storage += probes[neighbor].storage

        if storage < 3000:
            return int(storage)

        storage *= self.__calculate_combo_bonus(site, probes)

        for neighbor in network.sites[site].connection:
            storage *= self.__calculate_boost(neighbor, probes)

        return int(storage)

    def perform(self, probes: dict[int, Probe]) -> Value:
        profit = 27675
        storage = 6000

        for site in probes:
            if probes[site].type == ProbeType.BASIC:
                continue

            profit -= BASIC_PROFITS[site]
            # for resource in network.sites[site].precious_resources:
            #     if resource not in self.resources:
            #         continue
            #     self.resources.remove(resource)

            profit += self.__calculate_profit(site, probes)
            storage += self.__calculate_storage(site, probes)

        return Value(profit=profit, storage=storage, resource=set())
