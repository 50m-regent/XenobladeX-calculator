from data_probe_optimizer.search import Optimizer
from data_probe_optimizer.type import Probes


def main():
    inventory = {
        Probes.STORAGE: 1,
        Probes.DUPLICATE: 1,
    }
    optimizer = Optimizer(storage_weight=1)

    best_probes, value = optimizer.search(probes={}, inventory=inventory, log=True)

    print(best_probes)
    print(value)


if __name__ == "__main__":
    main()
