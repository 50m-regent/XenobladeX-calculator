from copy import deepcopy

from icecream import ic

from .calculate_value import ValueCalculator
from .type import FrontierNetwork, ProbeType, Value


class Optimizer:
    def __init__(
        self,
        storage_weight: float | None = None,
        profit_weight: float | None = None,
    ) -> None:
        self.network = FrontierNetwork()
        self.calculator = ValueCalculator(self.network)

        if not storage_weight and not profit_weight:
            raise ValueError("Either storage weight or profit weight must be set.")
        if not storage_weight:
            assert profit_weight
            self.storage_weight = 1 - profit_weight
            self.profit_weight = profit_weight
        if not profit_weight:
            assert storage_weight
            self.storage_weight = storage_weight
            self.profit_weight = 1 - storage_weight

    def calculate_score(self, value: Value) -> float:
        return self.storage_weight * value.storage + self.profit_weight * value.profit

    def search(
        self,
        probes: dict[int, ProbeType],
        inventory: dict[ProbeType, int],
    ) -> tuple[dict[int, ProbeType], Value]:
        best_score = 0
        best_probes = probes
        for site in self.network.sites.keys():
            if site in probes:
                continue
            for probe in inventory.keys():
                if inventory[probe] == 0:
                    continue

                copied_probes = deepcopy(probes)
                copied_inventory = deepcopy(inventory)

                copied_probes[site] = probe
                copied_inventory[probe] -= 1

                searched_probes, value = self.search(copied_probes, copied_inventory)
                score = self.calculate_score(value)

                if best_score > score:
                    continue

                best_score = score
                best_probes = searched_probes

        ic(probes)
        ic(inventory)
        print("------------------------")

        return best_probes, self.calculator.perform(best_probes)
