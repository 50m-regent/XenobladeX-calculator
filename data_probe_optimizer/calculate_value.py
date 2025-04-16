from .type import FrontierNetwork, ProbeType, Value


class ValueCalculator:
    def __init__(self, network: FrontierNetwork) -> None:
        self.network = network

    def __calculate_combo_size(
        self,
        site: int,
        probes: dict[int, ProbeType],
        root: int | None = None,
    ) -> int:
        if not root:
            root = site

        if probes[site] != probes[root]:
            return 0
        else:
            combo_size = 1

        for neighbor in self.network.sites[site].connection:
            if neighbor == root:
                continue
            combo_size += self.__calculate_combo_size(neighbor, probes, root=site)

        return combo_size

    def __calculate_combo_bonus(self, site: int, probes: dict[int, ProbeType]) -> float:
        match self.__calculate_combo_size(site, probes):
            case 1 | 2:
                return 1
            case 3 | 4:
                return 1.3
            case 5 | 6 | 7:
                return 1.5
            case _:
                return 1.8

    def __calculate_boost(self, site: int, probes: dict[int, ProbeType]) -> float:
        boost = probes[site].value.boost
        if probes[site] == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                boost *= probes[neighbor].value.boost

        if boost != 1:
            return boost * self.__calculate_combo_bonus(site, probes)

        return boost

    def __calculate_profit(self, site: int, probes: dict[int, ProbeType]) -> int:
        profit = probes[site].value.profit
        profit_value = self.network.sites[site].profit_value

        if probes[site] == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                if probes[neighbor] not in {
                    ProbeType.RESEARCH_1,
                    ProbeType.RESEARCH_2,
                    ProbeType.RESEARCH_3,
                    ProbeType.RESEARCH_4,
                    ProbeType.RESEARCH_5,
                    ProbeType.RESEARCH_6,
                }:
                    continue

                profit += probes[neighbor].value.profit

        if probes[site] in {
            ProbeType.RESEARCH_1,
            ProbeType.RESEARCH_2,
            ProbeType.RESEARCH_3,
            ProbeType.RESEARCH_4,
            ProbeType.RESEARCH_5,
            ProbeType.RESEARCH_6,
            ProbeType.DUPLICATE,
        }:
            profit_value += 1000 * self.network.sites[site].secret_spots

            for neighbor in self.network.sites[site].connection:
                profit *= self.__calculate_boost(neighbor, probes)

            profit *= self.__calculate_combo_bonus(site, probes)

        return int(profit * profit_value)

    def __calculate_storage(self, site: int, probes: dict[int, ProbeType]) -> int:
        storage = probes[site].value.storage
        if probes[site] == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                if probes[neighbor] != ProbeType.STORAGE:
                    continue

                storage += probes[neighbor].value.storage

        if probes[site] in {ProbeType.STORAGE, ProbeType.DUPLICATE}:
            storage *= self.__calculate_combo_bonus(site, probes)

            for neighbor in self.network.sites[site].connection:
                storage *= self.__calculate_boost(neighbor, probes)

        return int(storage)

    def perform(self, probes: dict[int, ProbeType]) -> Value:
        for site_num in self.network.sites.keys():
            if site_num not in probes:
                probes[site_num] = ProbeType.BASIC

        value = Value(profit=450, storage=6000, resource=set())
        for site in self.network.sites.keys():
            value.profit += self.__calculate_profit(site, probes)
            value.storage += self.__calculate_storage(site, probes)

            if probes[site] == ProbeType.BASIC:
                value.resource.update(self.network.sites[site].precious_resources)

        return value
