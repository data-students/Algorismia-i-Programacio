from yogi import tokens, read
from collections import deque


DIRECTIONS = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)] 

Position = tuple[int, int] # tuple of the (x, y) = (cols, rows) position
StrMatrix = list[list[str]]
BoolMatrix = list[list[bool]]

def islands(M: StrMatrix, visited: BoolMatrix) -> int:
    rows, cols = len(M), len(M[0])
    
    def bfs(s: Position) -> None:
        dq = deque([s])
        while dq:
            curr_pos = dq.popleft()
            for dir in DIRECTIONS:
                adj_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])
                if 0 <= adj_pos[0] < cols and 0 <= adj_pos[1] < rows and not visited[adj_pos[1]][adj_pos[0]]:
                    visited[adj_pos[1]][adj_pos[0]] = True
                    dq.append(adj_pos)

    count = 0
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                visited[row][col] = True
                bfs((col, row))
                count += 1
    return count


def read_matrix(n: int, m: int) -> tuple[StrMatrix, BoolMatrix]:

    matrix: StrMatrix = []
    visited: BoolMatrix = []

    for _ in range(n):
        mat_vector: list[str] = []
        vis_vector: list[bool] = []
        row = read(str)
        for ipt in row:
            mat_vector.append(str(ipt))
            vis_vector.append(bool(ipt == "."))
        matrix.append(mat_vector)
        visited.append(vis_vector)
    
    return matrix, visited


def main() -> None:
    for n in tokens(int):
        m = read(int)
        matrix, visited = read_matrix(n, m)
        print(islands(matrix, visited))


if __name__ == "__main__":
    main()
