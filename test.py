import unittest
from unittest import TestCase

from data_probe_optimizer.type import FrontierNetwork, Probes
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
            504: Probes.DUPLICATE,
            508: Probes.DUPLICATE,
            509: Probes.DUPLICATE,
            507: Probes.DUPLICATE,
            511: Probes.DUPLICATE,
            505: Probes.DUPLICATE,
            510: Probes.DUPLICATE,
            513: Probes.DUPLICATE,
        }

        for site_num in self.network.sites.keys():
            if site_num not in probes:
                probes[site_num] = Probes.BASIC

        self.calculator.probes = probes

        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 8  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.8  # type: ignore
        )

        self.calculator.probes[513] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 7  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.5  # type: ignore
        )

        self.calculator.probes[510] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 6  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.5  # type: ignore
        )

        self.calculator.probes[505] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 5  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.5  # type: ignore
        )

        self.calculator.probes[511] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 4  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.3  # type: ignore
        )

        self.calculator.probes[507] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 3  # type: ignore
        assert (
            self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1.3  # type: ignore
        )

        self.calculator.probes[509] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 2  # type: ignore
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1  # type: ignore

        self.calculator.probes[508] = Probes.BASIC
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 1  # type: ignore
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1  # type: ignore

        self.calculator.probes[101] = Probes.DUPLICATE
        assert self.calculator._ValueCalculator__calculate_combo_size(504) == 1  # type: ignore
        assert self.calculator._ValueCalculator__calculate_combo_bonus(504) == 1  # type: ignore

    def test_boost(self) -> None:
        probes = {
            504: Probes.STORAGE,
        }

        value = self.calculator.perform(probes)
        assert value.storage == 9000

        probes[508] = Probes.DUPLICATE
        value = self.calculator.perform(probes)
        assert value.storage == 12000

        probes[511] = Probes.DUPLICATE
        probes[509] = Probes.DUPLICATE
        value = self.calculator.perform(probes)
        assert value.storage == 12900

        probes[512] = Probes.BOOST_2
        value = self.calculator.perform(probes)
        assert value.storage == 19140

        probes[503] = Probes.STORAGE
        probes[502] = Probes.STORAGE
        value = self.calculator.perform(probes)
        assert value.storage == 27840

        probes[507] = Probes.STORAGE
        value = self.calculator.perform(probes)
        assert value.storage == 40980


if __name__ == "__main__":
    unittest.main()
