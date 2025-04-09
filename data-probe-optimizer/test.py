import unittest
from unittest import TestCase

from type import FrontierNetwork


class TestTypes(TestCase):
    def test_graph(self) -> None:
        network = FrontierNetwork()
        for site in range(len(network.sites)):
            if not network.sites[site]:
                continue

            for connected_site in network.sites[site].connection:
                assert site in network.sites[connected_site].connection


if __name__ == "__main__":
    unittest.main()
