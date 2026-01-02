import heapq
import networkx as nx


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def create_test_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 5),
        ("B", "D", 10),
        ("C", "E", 3),
        ("E", "D", 4),
        ("D", "A", 7),
    ])
    return graph


def test_dijkstra_distances():
    graph = create_test_graph()
    distances = dijkstra(graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 4
    assert distances["C"] == 2
    assert distances["E"] == 5
    assert distances["D"] == 7


def test_single_vertex():
    graph = nx.Graph()
    graph.add_node("A")

    distances = dijkstra(graph, "A")
    assert distances == {"A": 0}


def test_linear_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 2),
        ("C", "D", 3),
    ])

    distances = dijkstra(graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == 3
    assert distances["D"] == 6


def run_tests():
    test_dijkstra_distances()
    test_single_vertex()
    test_linear_graph()
    print("All tests passed.")


def main():
    graph = create_test_graph()
    start_vertex = "A"
    distances = dijkstra(graph, start_vertex)

    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")


if __name__ == "__main__":
    run_tests()
    main()
