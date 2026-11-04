
# Mini-Courier Planner

## Project Overview
Mini-Courier Planner is a Python-based project that simulates an intelligent courier delivery planning system.

The project uses sorting, Dynamic Programming, graph algorithms, and approximation techniques to prioritize parcels, optimize vehicle capacity, find shortest delivery paths, and analyze algorithm performance.

## Objectives
- Prioritize parcels based on delivery deadlines.
- Select the best combination of parcels within vehicle capacity.
- Find shortest paths between delivery locations.
- Generate an approximate delivery route.
- Measure and compare algorithm execution times.

## Technologies Used
- Python
- Heap Queue (heapq)
- Matplotlib
- CSV
- PyCharm

## Project Phases

### Phase 1: Courier Problem Design and Planning
Defined parcel attributes, delivery locations, weighted graph, and vehicle capacity.

### Phase 2: Package Prioritization and Box Filling
- Merge Sort is used to sort parcels based on deadlines.
- Knapsack Dynamic Programming is used to select parcels with maximum total value within the vehicle capacity.

### Phase 3: Route Maker and Graph Processing
- Dijkstra's Algorithm finds shortest paths.
- Nearest Neighbor approximation generates a delivery route.

### Phase 4: Performance Testing and Optimization
- Tested algorithms using different input sizes.
- Recorded execution times.
- Generated runtime comparison charts.
- Saved performance results in a CSV file.

### Phase 5: Final Report and Demonstration
Prepared project documentation, screenshots, results, and final demonstration.

## Sample Dataset
The `datasets` folder contains:
- `parcels.csv`: Sample parcel information.
- `delivery_graph.csv`: Weighted delivery connections and distances.




