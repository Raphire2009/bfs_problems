import pandas as pd
import time
import os
from collections import defaultdict, deque

# -------------------------------
# Detect dataset type (improved)
# -------------------------------
def detect_dataset(df):
    if df.shape[1] == 2:
        print("Dataset has 2 columns → POSSIBLE graph structure")
        return "graph"
    else:
        print("Dataset has more than 2 columns → Tabular data")
        return "table"

    # -------------------------------
    # Build graph safely
    # -------------------------------
def build_graph(df):
    graph = defaultdict(list)

    for _, row in df.iterrows():
        try:
            a = row.iloc[0]
            b = row.iloc[1]

            graph[a].append(b)
            graph[b].append(a)

        except Exception as e:
            print("Error reading row:", e)
            continue

        return graph

        # -------------------------------
        # BFS Search
        # -------------------------------
def bfs(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == target:
            return True

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

            return False

        # -------------------------------
        # Linear Search
        # -------------------------------
def linear_search(df, column, value):
    return df[df[column].astype(str) == value]

# -------------------------------
# Dictionary Search
# -------------------------------
def build_lookup(df, key_column):
    lookup = {}
    for _, row in df.iterrows():
        lookup[str(row[key_column])] = row
        return lookup

    # -------------------------------
    # MAIN PROGRAM
    # -------------------------------
def main():
    print("=== INTERACTIVE SEARCH ENGINE ===\n")

    # Ask for file path (loop until correct)
    while True:
        file_path = input("Enter CSV file path: ").strip()

        if os.path.exists(file_path):
            print("✅ File found!\n")
            break
        else:
            print("❌ File not found, try again.\n")

            # Load file safely
            try:
                df = pd.read_csv(file_path)
            except Exception as e:
                print("Error loading CSV:", e)
                return

            print("Columns detected:", list(df.columns), "\n")

            # Detect dataset
            dataset_type = detect_dataset(df)

            # -------------------------------
            # GRAPH CASE → BFS
            # -------------------------------
            if dataset_type == "graph":

                use_bfs = input("\nUse BFS? (yes/no): ").lower()

                if use_bfs != "yes":
                    print("Skipping BFS.")
                    return

                graph = build_graph(df)

                start = input("Enter start node: ")
                target = input("Enter target node: ")

                start_time = time.time()
                found = bfs(graph, start, target)
                end_time = time.time()

                print("\nResult:", found)
                print("Time Complexity: O(V + E)")
                print("Execution Time:", end_time - start_time, "seconds")

                # -------------------------------
                # TABLE CASE → Search methods
                # -------------------------------
            else:
                    print("\nChoose search method:")
                    print("1. Linear Search (O(n))")
                    print("2. Dictionary Search (O(1))")

                    choice = input("Enter choice (1 or 2): ")

                    column = input("Enter column name: ")

                    if column not in df.columns:
                        print("❌ Invalid column name!")
                        return

                    target = input("Enter value to search: ")

                    # -------------------------------
                    # LINEAR SEARCH
                    # -------------------------------
                    if choice == "1":
                        start_time = time.time()
                        result = linear_search(df, column, target)
                        end_time = time.time()

                        print("\nResult:\n", result)
                        print("Time Complexity: O(n)")
                        print("Execution Time:", end_time - start_time, "seconds")

                        # -------------------------------
                        # DICTIONARY SEARCH
                        # -------------------------------
                    elif choice == "2":
                        print("\nBuilding lookup table...")

                        build_start = time.time()
                        lookup = build_lookup(df, column)
                        build_end = time.time()

                        search_start = time.time()
                        result = lookup.get(target, "Not found")
                        search_end = time.time()

                        print("\nResult:\n", result)
                        print("Build Time:", build_end - build_start, "seconds")
                        print("Search Time:", search_end - search_start, "seconds")
                        print("Time Complexity: O(1) lookup, O(n) preprocessing")

                    else:
                        print("❌ Invalid choice!")

                        # Run program
if __name__ == "__main__":
    main()