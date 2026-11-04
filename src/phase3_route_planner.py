import heapq

graph = {
    "Warehouse": {"A": 4, "B": 6},
    "A": {"Warehouse": 4, "B": 2, "C": 5},
    "B": {"Warehouse": 6, "A": 2, "C": 3, "D": 4},
    "C": {"A": 5, "B": 3, "D": 2},
    "D": {"B": 4, "C": 2}
}

warehouse = "Warehouse"
customers = ["A", "B", "C", "D"]


def dijkstra(graph, start):
    distances = {}
    previous = {}

    for node in graph:
        distances[node] = float("inf")
        previous[node] = None

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, road_distance in graph[current_node].items():
            new_distance = current_distance + road_distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous

def get_path(previous, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path

all_distances = {}
all_previous = {}

for location in graph:
    distances, previous = dijkstra(graph, location)
    all_distances[location] = distances
    all_previous[location] = previous

print("================================")
print("MINI-COURIER PLANNER - PHASE 3")
print("================================")

print("\nWEIGHTED ROAD GRAPH (Distance in km)")

for location, roads in graph.items():
    print(location, "->", roads)

print("\nSHORTEST PATHS FROM WAREHOUSE")

distances = all_distances[warehouse]
previous = all_previous[warehouse]

for customer in customers:
    path = get_path(previous, warehouse, customer)

    print(
        warehouse, "to", customer,
        "| Path:", " -> ".join(path),
        "| Distance:", distances[customer], "km"
    )

def nearest_neighbor(graph, start, customers, all_distances):
    current = start
    unvisited = customers.copy()
    route = [start]
    total_distance = 0

    while unvisited:
        next_customer = min(
            unvisited,
            key=lambda customer: all_distances[current][customer]
        )

        total_distance += all_distances[current][next_customer]
        route.append(next_customer)

        unvisited.remove(next_customer)
        current = next_customer

    total_distance += all_distances[current][start]
    route.append(start)

    return route, total_distance


route, total_distance = nearest_neighbor(
    graph, warehouse, customers, all_distances
)

print("\nNEAREST-NEIGHBOR DELIVERY ROUTE")
print(" -> ".join(route))

print("\nROUTE SEGMENT DETAILS")

for i in range(len(route) - 1):
    start = route[i]
    destination = route[i + 1]

    path = get_path(
        all_previous[start],
        start,
        destination
    )

    distance = all_distances[start][destination]

    print(
        start, "to", destination,
        "| Shortest path:", " -> ".join(path),
        "| Distance:", distance, "km"
    )

print("\nTOTAL ROUTE DISTANCE:", total_distance, "km")
print("Customers visited:", len(customers))
print("Warehouse return:", "Yes")

