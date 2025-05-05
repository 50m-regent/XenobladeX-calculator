from data_probe_optimizer.search import Optimizer
from data_probe_optimizer.evaluate import ValueCalculator
from data_probe_optimizer.type import Inventory


def main():
    inventory = Inventory(storage=11, duplicate=3, boost_2=3, boost_1=0)
    optimizer = Optimizer(storage_weight=1)

    best_probes_list = optimizer.get_optimize_probes(
        inventory=inventory  # , max_candidates=1024
    )

    calculator = ValueCalculator()

    for best_probes in best_probes_list:
        for site, probe in best_probes.items():
            print(site, probe.name)
        print(calculator.perform(best_probes))


if __name__ == "__main__":
    main()
