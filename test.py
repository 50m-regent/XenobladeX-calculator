import unittest
from unittest import TestCase

from icecream import ic

from data_probe_optimizer.type import FrontierNetwork, Probes
from data_probe_optimizer.evaluate import ProbeTree, ValueCalculator


class TestTypes(TestCase):
    def test_graph(self) -> None:
        network = FrontierNetwork()
        for site_num, site in network.sites.items():
            for connected_site_num in site.connection:
                assert site_num in network.sites[connected_site_num].connection


class TestValues(TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.network = FrontierNetwork()

    def test_base(self) -> None:
        values = ValueCalculator().perform({})

        assert values.profit == 27675
        assert values.storage == 6000

    def test_combo(self) -> None:
        probes = {
            504: Probes.DUPLICATE,
            508: Probes.DUPLICATE,
            509: Probes.DUPLICATE,
            507: Probes.DUPLICATE,
            511: Probes.DUPLICATE,
            505: Probes.DUPLICATE,
            510: Probes.DUPLICATE,
            513: Probes.DUPLICATE,
        }

        calculator = ValueCalculator()

        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 8  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.8  # type: ignore
        )

        probes[513] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 7  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5  # type: ignore
        )

        probes[510] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 6  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5  # type: ignore
        )

        probes[505] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 5  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5  # type: ignore
        )

        probes[511] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 4  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.3  # type: ignore
        )

        probes[507] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 3  # type: ignore
        assert (
            calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.3  # type: ignore
        )

        probes[509] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 2  # type: ignore
        assert calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1  # type: ignore

        probes[508] = Probes.BASIC
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 1  # type: ignore
        assert calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1  # type: ignore

        probes[101] = Probes.DUPLICATE
        assert calculator._ValueCalculator__calculate_combo_size(504, probes) == 1  # type: ignore
        assert calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1  # type: ignore

    def test_boost(self) -> None:
        probes = {
            504: Probes.STORAGE,
        }

        calculator = ValueCalculator()

        value = calculator.perform(probes)
        assert value.storage == 9000

        probes[508] = Probes.DUPLICATE
        value = calculator.perform(probes)
        assert value.storage == 12000

        probes[511] = Probes.DUPLICATE
        probes[509] = Probes.DUPLICATE
        value = calculator.perform(probes)
        assert value.storage == 12900

        probes[512] = Probes.BOOST_2
        value = calculator.perform(probes)
        assert value.storage == 19140

        probes[503] = Probes.STORAGE
        probes[502] = Probes.STORAGE
        value = calculator.perform(probes)
        assert value.storage == 27840

        probes[507] = Probes.STORAGE
        value = calculator.perform(probes)
        assert value.storage == 40980


class TestTree(TestCase):
    def test_center(self) -> None:
        probes = {
            504: Probes.RESEARCH_1,
            508: Probes.RESEARCH_2,
            509: Probes.RESEARCH_3,
            507: Probes.RESEARCH_4,
            511: Probes.RESEARCH_5,
            505: Probes.RESEARCH_6,
            510: Probes.DUPLICATE,
            513: Probes.STORAGE,
        }
        tree = ProbeTree(probes)

        assert tree.root.probe.name == "research_2"


if __name__ == "__main__":
    unittest.main()
