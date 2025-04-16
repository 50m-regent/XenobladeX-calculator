import unittest
from unittest import TestCase

from type import FrontierNetwork, ProbeType
from data_probe_optimizer.evaluate import ValueCalculator


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
        self.calculator = ValueCalculator(self.network)

    def test_base(self) -> None:
        values = self.calculator.perform({})

        assert values.profit == 27675
        assert values.storage == 6000

    def test_combo(self) -> None:
        probes = {
            504: ProbeType.DUPLICATE,
            508: ProbeType.DUPLICATE,
            509: ProbeType.DUPLICATE,
            507: ProbeType.DUPLICATE,
            511: ProbeType.DUPLICATE,
            505: ProbeType.DUPLICATE,
            510: ProbeType.DUPLICATE,
            513: ProbeType.DUPLICATE,
        }

        for site_num in self.network.sites.keys():
            if site_num not in probes:
                probes[site_num] = ProbeType.BASIC

        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 8
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.8
        )

        probes[513] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 7
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5
        )

        probes[510] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 6
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5
        )

        probes[505] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 5
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.5
        )

        probes[511] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 4
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.3
        )

        probes[507] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 3
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1.3
        )

        probes[509] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 2
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1

        probes[508] = ProbeType.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 1
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1

        probes[101] = ProbeType.DUPLICATE
        assert self.calculator._ValueCalculator__calculate_combo_size(504, probes) == 1
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504, probes) == 1

    def test_boost(self) -> None:
        probes = {
            504: ProbeType.STORAGE,
        }

        value = self.calculator.perform(probes)
        assert value.storage == 9000

        probes[508] = ProbeType.DUPLICATE
        value = self.calculator.perform(probes)
        assert value.storage == 12000

        probes[511] = ProbeType.DUPLICATE
        probes[509] = ProbeType.DUPLICATE
        value = self.calculator.perform(probes)
        assert value.storage == 12900

        probes[512] = ProbeType.BOOST_2
        value = self.calculator.perform(probes)
        assert value.storage == 19140

        probes[503] = ProbeType.STORAGE
        probes[502] = ProbeType.STORAGE
        value = self.calculator.perform(probes)
        assert value.storage == 27840

        probes[507] = ProbeType.STORAGE
        value = self.calculator.perform(probes)
        assert value.storage == 40980


if __name__ == "__main__":
    unittest.main()
