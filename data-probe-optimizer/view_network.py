import networkx
from matplotlib import pyplot

from type import FrontierNetwork


def visualize_network() -> None:
    graph = networkx.Graph()

    for spot1 in FrontierNetwork.NETWORK:
        graph.add_node(spot1)
        for spot2 in FrontierNetwork.NETWORK[spot1]:
            graph.add_node(spot2)
            graph.add_edge(spot1, spot2)

    pyplot.figure(figsize=(18, 12))
    networkx.draw(graph, with_labels=True, pos=networkx.planar_layout(graph))
    pyplot.show()


if __name__ == "__main__":
    visualize_network()
