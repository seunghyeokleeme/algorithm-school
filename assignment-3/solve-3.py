# 방향성이 없는 그래프를 위한 다익스트라 알고리즘 구현
# 필요한 라이브러리를 가져옵니다.
import heapq
import time

# 그래프를 나타내는 클래스입니다.
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}

    # 간선을 그래프에 추가합니다.
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # 방향성이 없기 때문에 양방향으로 추가합니다.

    # 시작 노드로부터 다른 모든 노드까지의 최단 거리를 찾는 함수입니다.
    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0
        pq = [(0, src)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # 현재 노드의 인접 노드들을 확인합니다.
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                # 더 짧은 경로를 찾았다면 distances를 업데이트하고 우선순위 큐에 추가합니다.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# 모든 노드 쌍에 대한 최단 경로를 찾는 함수입니다.
def find_all_pairs_shortest_path(graph):
    all_pairs = {}
    for node in range(len(graph.graph)):
        all_pairs[node] = graph.dijkstra(node)
    return all_pairs

# 그래프를 생성하고 간선을 추가합니다.
g = Graph(10)  # 10개의 노드가 있는 그래프
edges = [
    (0, 1, 12), (0, 2, 15), (2, 3, 21), (1, 4, 4),
    (2, 5, 10), (2, 6, 7), (3, 7, 25), (4, 5, 3),
    (4, 8, 13), (5, 6, 10), (6, 7, 19), (6, 9, 9),
    (7, 9, 5), (8, 9, 15)
]

# A, B, C, D, E, F, G, H, I, J에 해당하는 인덱스를 사용합니다.
for edge in edges:
    g.add_edge(*edge)

# 함수의 실행 전 시간을 기록합니다.
start_time = time.time();

# 모든 노드 쌍의 최단 경로를 찾습니다.
all_pairs_shortest_path = find_all_pairs_shortest_path(g)

# 함수의 실행 후 시간을 기록합니다.
end_time = time.time();

# 실행 시간을 계산합니다.
excution_time1 = end_time - start_time

# 결과를 출력합니다.
for idx in all_pairs_shortest_path:
    print("".join(f"{dist:7}" for dist in all_pairs_shortest_path[idx]))

print("-"*70);

def floyd_warshall(vertices, edges):
    # 초기 거리는 무한대로 설정합니다.
    dist = [[float('inf')] * vertices for _ in range(vertices)]
    
    # 자기 자신으로의 거리는 0으로 설정합니다.
    for i in range(vertices):
        dist[i][i] = 0
    
    # 간선의 거리로 dist 배열을 초기화합니다.
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w  # 무방향 그래프의 경우 양쪽 방향을 초기화합니다.
    
    # 플로이드-워셜 알고리즘을 적용합니다.
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# 그래프를 생성하고 간선을 추가합니다.
vertices = 10

# 함수의 실행 전 시간을 기록합니다.
start_time = time.time();

# 알고리즘을 실행하여 모든 쌍의 최단 경로를 계산합니다.
shortest_paths = floyd_warshall(vertices, edges)

# 함수의 실행 후 시간을 기록합니다.
end_time = time.time();

# 실행 시간을 계산합니다.
excution_time2 = end_time - start_time

# 결과를 출력합니다.
for row in shortest_paths:
    print("".join(f"{dist if dist != float('inf') else 'INF':7}" for dist in row))

print(f"1의 실행 시간: {excution_time1:.4f}s, 2의 실행 시간: {excution_time2:.4f}s")