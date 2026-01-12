import networkx as nx

def get_best_route(start, end):
    G = nx.Graph()

    # Graph edges (distance / cost)
    G.add_weighted_edges_from([
        ('Warehouse', 'A', 12),
        ('A', 'B', 7),
        ('B', 'C', 6),
        ('C', 'Destination', 5),
        ('Warehouse', 'Destination', 30)
    ])

    # Shortest path using Dijkstra
    path = nx.dijkstra_path(G, start, end)
    cost = nx.dijkstra_path_length(G, start, end)

    return path, cost
