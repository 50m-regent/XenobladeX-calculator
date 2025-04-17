from copy import deepcopy

from tqdm import tqdm

from .evaluate import ValueCalculator
from .type import FrontierNetwork, Probe, Value


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
        probes: dict[int, Probe],
        inventory: dict[Probe, int],
        log: bool = False,
    ) -> tuple[dict[int, Probe], Value]:
        best_score = 0
        best_probes = deepcopy(probes)

        sites = tqdm(self.network.sites.keys()) if log else self.network.sites.keys()
        for site in sites:
            if site in probes:
                continue
            for probe in inventory.keys():
                if inventory[probe] == 0:
                    continue

                probes[site] = probe
                inventory[probe] -= 1

                searched_probes, value = self.search(probes, inventory)
                score = self.calculate_score(value)

                probes.pop(site)
                inventory[probe] += 1

                if best_score > score:
                    continue

                best_score = score
                best_probes = deepcopy(searched_probes)

        return best_probes, self.calculator.perform(best_probes)
