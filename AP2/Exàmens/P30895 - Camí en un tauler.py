from yogi import read, tokens
import heapq

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

Board = list[list[int]]
Point = tuple[int, int] # position (x, y) = (cols, rows)

def minimum_cost(board: Board) -> int:
    n = len(board)
    src = (n // 2, n // 2)

    min_cost = 500 * 1000
    perif_count = 0
    dists = [[-1] * n for _ in range(n)]
    dists[src[1]][src[0]] = board[src[1]][src[0]]
    pq = [(dists[src[1]][src[0]], src)]

    while pq:
        _, curr_node = heapq.heappop(pq)
        curr_x, curr_y = curr_node

        if curr_x == 0 or curr_x == n - 1 or curr_y == 0 or curr_y == n - 1:
            perif_count += 1
            min_cost = min(min_cost, dists[curr_y][curr_x])

        for dx, dy in DIRECTIONS:
            adj_x, adj_y = curr_x + dx, curr_y + dy
            if 0 <= adj_x < n and 0 <= adj_y < n:
                new_dist = dists[curr_y][curr_x] + board[adj_y][adj_x]
                if dists[adj_y][adj_x] == -1 or new_dist < dists[adj_y][adj_x]:
                    dists[adj_y][adj_x] = new_dist
                    heapq.heappush(pq, (dists[adj_y][adj_x], (adj_x, adj_y)))
                    
    return min_cost

def main() -> None:
    for n in tokens(int):
        if n == 1:
            print(read(int))
        else:
            board = [[read(int) for _ in range(n)] for _ in range(n)]
            print(minimum_cost(board))  

if __name__ == "__main__":
    main()
