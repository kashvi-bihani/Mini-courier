parcels = [
    {"id": "P1", "weight": 3, "priority": 1, "deadline": 10, "value": 100},
    {"id": "P2", "weight": 4, "priority": 2, "deadline": 15, "value": 150},
    {"id": "P3", "weight": 2, "priority": 1, "deadline": 8, "value": 80},
    {"id": "P4", "weight": 5, "priority": 3, "deadline": 20, "value": 200},
    {"id": "P5", "weight": 1, "priority": 2, "deadline": 12, "value": 60}
]

vehicle_capacity = 10


def merge_sort(parcel_list):
    if len(parcel_list) <= 1:
        return parcel_list

    mid = len(parcel_list) // 2

    left = merge_sort(parcel_list[:mid])
    right = merge_sort(parcel_list[mid:])

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


sorted_parcels = merge_sort(parcels)

print("=================================")
print("MINI-COURIER PLANNER - PHASE 2")
print("=================================")

print("\nPARCELS SORTED BY DEADLINE")
print("ID\tWeight\tDeadline\tValue")

for parcel in sorted_parcels:
    print(
        parcel["id"], "\t",
        parcel["weight"], "\t",
        parcel["deadline"], "\t\t",
        parcel["value"]
    )


n = len(parcels)
capacity = vehicle_capacity

dp = [[0 for w in range(capacity + 1)]
      for i in range(n + 1)]

for i in range(1, n + 1):
    weight = parcels[i - 1]["weight"]
    value = parcels[i - 1]["value"]

    for w in range(capacity + 1):
        dp[i][w] = dp[i - 1][w]


        if weight <= w:
            selected_value = value + dp[i - 1][w - weight]
            dp[i][w] = max(dp[i][w], selected_value)

print("\nDYNAMIC PROGRAMMING TABLE")
print("Rows = Number of parcels.csv considered")
print("Columns = Available capacity in kg")

print("i/w", end="\t")
for w in range(capacity + 1):
    print(w, end="\t")
print()

for i in range(n + 1):
    print(i, end="\t")
    for w in range(capacity + 1):
        print(dp[i][w], end="\t")
    print()

selected_parcels = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        parcel = parcels[i - 1]
        selected_parcels.append(parcel)
        w -= parcel["weight"]

selected_parcels.reverse()

total_weight = sum(p["weight"] for p in selected_parcels)
total_value = sum(p["value"] for p in selected_parcels)

print("\nOPTIMAL PACKING PLAN")
print("Selected Parcels:")

for parcel in selected_parcels:
    print(
        parcel["id"],
        "| Weight:", parcel["weight"], "kg",
        "| Value:", parcel["value"]
    )

print("\nTotal Weight:", total_weight, "kg")
print("Vehicle Capacity:", vehicle_capacity, "kg")
print("Total Parcel Value:", total_value)
print("Remaining Capacity:", vehicle_capacity - total_weight, "kg")

