from yogi import read, tokens
from sys import maxsize as numero_muy_grande

AdjMat = list[list[int]]

def min_cost_rec(costs: AdjMat, curr_path: list[int], visited: list[bool], curr_cost: int, min_cost: int) -> int:
    n = len(costs)
    curr_node = curr_path[-1]

    if len(curr_path) == n:
        return curr_cost + costs[curr_node][0]
    
    for adj_node in range(n):
        if not visited[adj_node] and curr_cost + costs[curr_node][adj_node] < min_cost:
            visited[adj_node] = True
            curr_path.append(adj_node)
            find_cost = min_cost_rec(costs, curr_path, visited, curr_cost + costs[curr_node][adj_node], min_cost)
            if find_cost < min_cost:
                min_cost = find_cost
            curr_path.pop()
            visited[adj_node] = False
    
    return min_cost


def min_cost(costs: AdjMat) -> int:

    n = len(costs)
    in_path = [0] # Camino inicializado con un nodo cualquiera
    visited = [True] + [False] * (n - 1)

    return min_cost_rec(costs, in_path, visited, 0, numero_muy_grande)

def main() -> None:
    for n in tokens(int):
        adj_mat = [[read(int) for _ in range(n)] for _ in range(n)]
        print(min_cost(adj_mat))

if __name__ == "__main__":
    main()