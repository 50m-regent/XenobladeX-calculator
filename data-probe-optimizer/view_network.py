import networkx
from matplotlib import pyplot

from type import FrontierNetwork


def visualize_network() -> None:
    graph = networkx.Graph()

    network = FrontierNetwork()
    for site1 in range(len(network.sites)):
        if not network.sites[site1]:
            continue

        graph.add_node(site1)
        for site2 in network.sites[site1].connection:
            graph.add_node(site2)
            graph.add_edge(site1, site2)

    pyplot.figure(figsize=(18, 12))
    networkx.draw(graph, with_labels=True, pos=networkx.planar_layout(graph))
    pyplot.show()


if __name__ == "__main__":
    visualize_network()
