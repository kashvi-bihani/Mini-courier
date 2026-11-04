import random
import time
import csv
import heapq
import statistics
import matplotlib.pyplot as plt

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["deadline"] <= right[j]["deadline"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def knapsack(parcels, capacity):
    n = len(parcels)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node].items():
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances


def create_graph(number_of_nodes):
    graph = {
        i: {} for i in range(number_of_nodes)
    }

    for i in range(number_of_nodes - 1):
        weight = random.randint(1, 20)
        graph[i][i + 1] = weight
        graph[i + 1][i] = weight

    for i in range(number_of_nodes):
        for j in range(i + 2, number_of_nodes):
            if random.random() < 0.12:
                weight = random.randint(1, 20)
                graph[i][j] = weight
                graph[j][i] = weight

    return graph

def nearest_neighbor(distances, start):
    unvisited = set(distances.keys())
    unvisited.remove(start)

    route = [start]
    current = start
    total_distance = 0

    while unvisited:
        next_node = min(
            unvisited,
            key=lambda node: distances[current][node]
        )

        total_distance += distances[current][next_node]
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    total_distance += distances[current][start]
    route.append(start)

    return route, total_distance

def measure_time(function, repeats=3):
    times = []

    for _ in range(repeats):
        start_time = time.perf_counter()
        function()
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    return statistics.median(times)


results = []


def save_result(algorithm, size, runtime, correct):
    results.append({
        "Algorithm": algorithm,
        "Input Size": size,
        "Runtime (seconds)": runtime,
        "Correct": correct
    })


random.seed(42)


print("================================")
print("MINI-COURIER PLANNER - PHASE 4")
print("================================")

print("\nTESTING MERGE SORT")

for size in [100, 500, 1000, 5000]:
    parcels = [
        {
            "id": i,
            "weight": random.randint(1, 10),
            "deadline": random.randint(1, 1000),
            "value": random.randint(10, 200)
        }
        for i in range(size)
    ]

    sorted_parcels = merge_sort(parcels)

    runtime = measure_time(
        lambda: merge_sort(parcels)
    )

    correct = all(
        sorted_parcels[i]["deadline"]
        <= sorted_parcels[i + 1]["deadline"]
        for i in range(len(sorted_parcels) - 1)
    )

    save_result("Merge Sort", size, runtime, correct)
    print(
        "Parcels:", size,
        "| Time:", round(runtime, 6), "seconds",
        "| Correct:", correct
    )

print("\nTESTING KNAPSACK DYNAMIC PROGRAMMING")

capacity = 100

for size in [20, 50, 100, 200]:
    parcels = [
        {
            "weight": random.randint(1, 20),
            "value": random.randint(10, 200)
        }
        for _ in range(size)
    ]

    best_value = knapsack(parcels, capacity)

    runtime = measure_time(
        lambda: knapsack(parcels, capacity)
    )

    correct = (
        best_value >= 0
        and best_value <= sum(p["value"] for p in parcels)
    )

    save_result("Knapsack DP", size, runtime, correct)
    print(
        "Parcels:", size,
        "| Capacity:", capacity,
        "| Best Value:", best_value,
        "| Time:", round(runtime, 6), "seconds",
        "| Correct:", correct
    )

for size in [10, 20, 40, 80]:
    print("\nTESTING GRAPH WITH", size, "LOCATIONS")

    graph = create_graph(size)

    distances = dijkstra(graph, 0)

    dijkstra_time = measure_time(
        lambda: dijkstra(graph, 0)
    )

    dijkstra_correct = (
        distances[0] == 0
        and all(distance < float("inf")
                for distance in distances.values())
    )

    save_result(
        "Dijkstra", size, dijkstra_time, dijkstra_correct
    )

    print(
        "Dijkstra Time:", round(dijkstra_time, 6), "seconds",
        "| Correct:", dijkstra_correct
    )
    all_distances = {
        node: dijkstra(graph, node)
        for node in graph
    }

    route, route_distance = nearest_neighbor(all_distances, 0)

    nearest_time = measure_time(
        lambda: nearest_neighbor(all_distances, 0)
    )

    route_correct = (
        len(route) == size + 1
        and route[0] == 0
        and route[-1] == 0
        and len(set(route[:-1])) == size
    )

    save_result(
        "Nearest Neighbor", size, nearest_time, route_correct
    )

    print(
        "Nearest Neighbor Time:", round(nearest_time, 6),
        "seconds",
        "| Route Distance:", route_distance,
        "| Correct:", route_correct
    )

print("\n" + "=" * 65)
print("RUNTIME COMPARISON TABLE")
print("=" * 65)

print(
    "{:<20} {:<12} {:<18} {:<10}".format(
        "Algorithm", "Input Size", "Time (seconds)", "Correct"
    )
)

for result in results:
    print(
        "{:<20} {:<12} {:<18} {:<10}".format(
            result["Algorithm"],
            result["Input Size"],
            round(result["Runtime (seconds)"], 6),
            result["Correct"]
        )
    )

with open("../phase4_runtime_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Algorithm",
            "Input Size",
            "Runtime (seconds)",
            "Correct"
        ]
    )
    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to phase4_runtime_results.csv")

algorithms = [
    "Merge Sort",
    "Knapsack DP",
    "Dijkstra",
    "Nearest Neighbor"
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for ax, algorithm in zip(axes.flatten(), algorithms):
    algorithm_results = [
        result for result in results
        if result["Algorithm"] == algorithm
    ]

    sizes = [r["Input Size"] for r in algorithm_results]
    times = [r["Runtime (seconds)"] for r in algorithm_results]

    ax.plot(sizes, times, marker="o")
    ax.set_title(algorithm)
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Runtime (seconds)")
    ax.grid(True)

plt.tight_layout()
plt.savefig("../phase4_runtime_chart.png", dpi=300)
plt.show()

