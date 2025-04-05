import unittest
from unittest import TestCase

from type import FrontierNetwork


class TestTypes(TestCase):
    def test_graph(self) -> None:
        for spot, connected_spots in FrontierNetwork.NETWORK.items():
            for connected_spot in connected_spots:
                assert spot in FrontierNetwork.NETWORK[connected_spot]


if __name__ == "__main__":
    unittest.main()
