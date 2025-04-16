import networkx
from matplotlib import pyplot

from type import FrontierNetwork


def visualize_network() -> None:
    graph = networkx.Graph()

    network = FrontierNetwork()
    for site_num_1, site_1 in network.sites.items():
        graph.add_node(site_num_1)
        for site_num_2 in site_1.connection:
            graph.add_node(site_num_2)
            graph.add_edge(site_num_1, site_num_2)

    pyplot.figure(figsize=(18, 12))
    networkx.draw(graph, with_labels=True, pos=networkx.planar_layout(graph))
    pyplot.show()


if __name__ == "__main__":
    visualize_network()
