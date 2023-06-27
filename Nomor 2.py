import graphlib
import time

# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start]
    total_distance = 0

    start_time = time.time()

    def backtrack(curr_node):
        nonlocal total_distance
        visited[curr_node] = True

        # Menampilkan hasil setiap iterasi
        print(f"Iteration {len(path)}: Visited {curr_node}")

        # Base case: Semua node telah dikunjungi
        if len(path) == num_nodes:
            total_distance += graph[curr_node][start]  # Menambahkan jarak kembali ke titik awal
            return

        for next_node in range(num_nodes):
            if not visited[next_node]:
                path.append(next_node)
                total_distance += graph[curr_node][next_node]
                backtrack(next_node)
                path.pop()
                total_distance -= graph[curr_node][next_node]

        visited[curr_node] = False

    backtrack(start)

    end_time = time.time()
    execution_time = end_time - start_time

    return path, total_distance, execution_time

# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra(graph, start):
    num_nodes = len(graph)
    distance = [float('inf')] * num_nodes
    distance[start] = 0
    visited = [False] * num_nodes

    start_time = time.time()

    for _ in range(num_nodes):
        # Menemukan node dengan jarak terpendek yang belum dikunjungi
        min_dist = float('inf')
        min_node = -1
        for node in range(num_nodes):
            if not visited[node] and distance[node] < min_dist:
                min_dist = distance[node]
                min_node = node

        visited[min_node] = True

        # Menampilkan hasil setiap iterasi
        print(f"Iteration {min_node+1}: Visited {min_node}")

        # Memperbarui jarak ke node-node tetangga
        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[min_node][neighbor] > 0:
                new_dist = distance[min_node] + graph[min_node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist

    end_time = time.time()
    execution_time = end_time - start_time

    # Membangun shortest path berdasarkan distance yang telah dihitung
    path = [start]
    curr_node = start
    while curr_node != start or len(path) < num_nodes:
        neighbors = [(node, graph[curr_node][node]) for node in range(num_nodes) if graph[curr_node][node] > 0]
        min_dist = min(neighbors, key=lambda x: x[1])
        path.append(min_dist[0])
        curr_node = min_dist[0]

    return path, distance[start], execution_time

# Fungsi untuk menampilkan hasil akhir shortest path
def print_shortest_path(path, distance):
    print("Shortest path:", path)
    print("Total distance:", distance)

# Graph untuk pengujian
graphlib