from .type import FrontierNetwork, Probe, Probes, ProbeType, Value


class ValueCalculator:
    def __init__(self, network: FrontierNetwork) -> None:
        self.network = network

    def __calculate_combo_size(
        self,
        site: int,
        root: int | None = None,
    ) -> int:
        if not root:
            root = site

        if hash(self.probes[site]) != hash(self.probes[root]):
            return 0
        else:
            combo_size = 1

        for neighbor in self.network.sites[site].connection:
            if neighbor == root:
                continue
            combo_size += self.__calculate_combo_size(neighbor, root=site)

        return combo_size

    def __calculate_combo_bonus(self, site: int) -> float:
        match self.__calculate_combo_size(site):
            case 1 | 2:
                return 1
            case 3 | 4:
                return 1.3
            case 5 | 6 | 7:
                return 1.5
            case _:
                return 1.8

    def __calculate_boost(self, site: int) -> float:
        boost = self.probes[site].boost
        if self.probes[site].type == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                boost *= self.probes[neighbor].boost

        if boost > 1:
            return boost * self.__calculate_combo_bonus(site)

        return boost

    def __calculate_profit(self, site: int) -> int:
        profit = self.probes[site].profit
        profit_value = self.network.sites[site].profit_value

        if self.probes[site].type == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                if self.probes[neighbor].type != ProbeType.RESEARCH:
                    continue

                profit += self.probes[neighbor].profit

        if profit < 2:
            return int(profit * profit_value)

        profit_value += 1000 * self.network.sites[site].secret_spots

        for neighbor in self.network.sites[site].connection:
            profit *= self.__calculate_boost(neighbor)

        profit *= self.__calculate_combo_bonus(site)

        return int(profit * profit_value)

    def __calculate_storage(self, site: int) -> int:
        storage = self.probes[site].storage
        if self.probes[site].type == ProbeType.DUPLICATE:
            for neighbor in self.network.sites[site].connection:
                if self.probes[neighbor].type != ProbeType.STORAGE:
                    continue

                storage += self.probes[neighbor].storage

        if storage < 3000:
            return int(storage)

        storage *= self.__calculate_combo_bonus(site)

        for neighbor in self.network.sites[site].connection:
            storage *= self.__calculate_boost(neighbor)

        return int(storage)

    def perform(self, probes: dict[int, Probe]) -> Value:
        self.probes = {
            site: probes[site] if site in probes else Probes.BASIC
            for site in self.network.sites.keys()
        }

        profit = 450
        storage = 6000
        resources = []
        for site in self.network.sites.keys():
            profit += self.__calculate_profit(site)
            storage += self.__calculate_storage(site)

            if self.probes[site].type == ProbeType.MINING:
                resources.extend(self.network.sites[site].precious_resources)

        return Value(profit=profit, storage=storage, resource=set(resources))
