parcels = [
    {"id": "P1", "weight": 3, "priority": 1, "deadline": 10, "value": 100},
    {"id": "P2", "weight": 4, "priority": 2, "deadline": 15, "value": 150},
    {"id": "P3", "weight": 2, "priority": 1, "deadline": 8, "value": 80},
    {"id": "P4", "weight": 5, "priority": 3, "deadline": 20, "value": 200},
    {"id": "P5", "weight": 1, "priority": 2, "deadline": 12, "value": 60}
]

locations = ["Warehouse", "A", "B", "C", "D"]


graph = {
    "Warehouse": {"A": 4, "B": 6},
    "A": {"Warehouse": 4, "B": 2, "C": 5},
    "B": {"Warehouse": 6, "A": 2, "C": 3, "D": 4},
    "C": {"A": 5, "B": 3, "D": 2},
    "D": {"B": 4, "C": 2}
}


vehicle_capacity = 10


print("MINI-COURIER PLANNER")
print("=====================")

print("\nPARCEL DETAILS")
for parcel in parcels:
    print(
        parcel["id"],
        "| Weight:", parcel["weight"], "kg",
        "| Priority:", parcel["priority"],
        "| Deadline:", parcel["deadline"],
        "| Value:", parcel["value"]
    )


print("\nDELIVERY LOCATIONS")
print(locations)


print("\nROAD NETWORK (Distance in km)")
for location, roads in graph.items():
    print(location, "->", roads)


print("\nVEHICLE CAPACITY:", vehicle_capacity, "kg")


print("\nALGORITHM PLAN")
print("1. Sorting: Prioritize parcels.csv by deadline or priority.")
print("2. Knapsack DP: Select parcels.csv within vehicle capacity.")
print("3. Dijkstra: Find shortest paths between locations.")
print("4. Nearest Neighbor: Plan the delivery sequence.")

