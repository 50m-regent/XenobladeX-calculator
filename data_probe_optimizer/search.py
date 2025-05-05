import pickle
import random
import shutil

from tqdm import tqdm

from .evaluate import ValueCalculator
from .type import FrontierNetwork, Library, Value, Inventory, Probe, Probes

terminal_size = shutil.get_terminal_size()


class Optimizer:
    def __init__(
        self,
        storage_weight: float | None = None,
        profit_weight: float | None = None,
    ) -> None:
        self.network = FrontierNetwork()

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

        self.library = Library()
        self.library[Inventory()] = [{}]

        self.calculator = ValueCalculator()

    def __calculate_score(self, value: Value) -> float:
        return self.storage_weight * value.storage + self.profit_weight * value.profit

    def get_optimize_probes(
        self,
        inventory: Inventory,
        depth: int = 0,
        max_candidates: int | None = None,
    ) -> list[dict[int, Probe]]:
        if inventory in self.library:
            return self.library[inventory]

        self.library[inventory] = []

        best_score = 0
        for attr in tqdm(
            inventory,
            desc="\t" * depth + f"Calculating: {inventory}",
            ncols=terminal_size[0] - depth * 3,
            leave=False,
            total=len(inventory.model_dump()),
        ):
            if attr[-1] == 0:
                continue

            inventory.__setattr__(attr[0], attr[-1] - 1)

            description = "\t" * depth + f"Calculating {inventory} + {attr[0]}"
            best_probes_list = self.get_optimize_probes(
                inventory, depth=depth + 1, max_candidates=max_candidates
            )

            inventory.__setattr__(attr[0], attr[-1])

            for probes in tqdm(
                best_probes_list,
                desc=description,
                ncols=terminal_size[0] - depth * 3,
                leave=False,
            ):
                for site in self.network.sites:
                    if site in probes:
                        continue
                    if len(probes) and all(
                        [
                            neighbor not in probes
                            for neighbor in self.network.sites[site].connection
                        ]
                    ):
                        continue

                    probes[site] = Probes.from_name(attr[0])
                    score = self.__calculate_score(self.calculator.perform(probes))

                    if score > best_score:
                        self.library[inventory] = [pickle.loads(pickle.dumps(probes))]
                        best_score = score
                    elif score == best_score:
                        self.library[inventory].append(
                            pickle.loads(pickle.dumps(probes))
                        )

                    probes.pop(site)

        if max_candidates:
            random.shuffle(self.library[inventory])
            self.library[inventory] = self.library[inventory][:max_candidates]

        return self.library[inventory]
