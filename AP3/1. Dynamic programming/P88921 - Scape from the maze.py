"""IDEA: Hacer un BFS"""

from yogi import read
from collections import deque

DIRECTIONS = [(1, 0), (0, 1)] # (down one row) or (down one col) (dr, dc)
LIMIT = 1_000_000

def diff_paths(maze: list[list[str]]) -> int:
    n, m = len(maze), len(maze[0])
    paths = [[0]*m for _ in range(n)]
    paths[0][0] = 1

    dq = deque([(0, 0)])

    while dq:
        r, c = dq.popleft()
        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc

            # Si esta fuera de los limites o en una pared
            if new_r >= n or new_c >= m or maze[new_r][new_c] == "X":
                continue
            
            # Poda: Añadir a la dq si no lo hemos visitado
            if paths[new_r][new_c] == 0:
                dq.append((new_r, new_c))

            # Poner como tope el limite 1.000.000
            paths[new_r][new_c] = min(paths[new_r][new_c] + paths[r][c], LIMIT)

    return paths[n - 1][m - 1]

def main() -> None:
    n = read(int)
    while n != 0:
        _ = read(int)
        maze = [list(read(str)) for _ in range(n)]
        paths = diff_paths(maze)
        print(paths) if paths != LIMIT else print("!!!")
        n = read(int)

if __name__ == "__main__":
    main()

