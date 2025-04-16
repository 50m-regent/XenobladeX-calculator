from data_probe_optimizer.search import Optimizer
from data_probe_optimizer.type import ProbeType
from data_probe_optimizer.postprocess import sanitize_probes


def main():
    inventory = {
        ProbeType.STORAGE: 1,
        ProbeType.DUPLICATE: 1,
        # ProbeType.BOOST_1: 1,
    }
    optimizer = Optimizer(storage_weight=1)

    best_probes, value = optimizer.search(probes={}, inventory=inventory)

    best_probes = sanitize_probes(best_probes)

    print(best_probes)
    print(value)


if __name__ == "__main__":
    main()
