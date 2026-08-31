from collections import deque
from yogi import read, tokens

Board = list[list[str]]
Point = tuple[int, int]  # tuple of the positions [x, y] == [row, col]

DIRECTIONS = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def valid_moves(board: Board, p: Point) -> list[Point]:
    rows = len(board)
    cols = len(board[0])

    moves: list[Point] = []

    for dx, dy in DIRECTIONS:
        move = (p[0] + dx, p[1] + dy)
        if 0 <= move[0] < cols and 0 <= move[1] < rows and board[move[1]][move[0]] != "X":
            moves.append(move)
    
    return moves

def minimum_steps(board: Board, src: Point) -> int:
    rows = len(board)
    cols = len(board[0])

    dists = [[-1] * cols for _ in range(rows)]
    dists[src[1]][src[0]] = 0

    dq = deque([src])
    while dq:
        curr_x, curr_y = dq.popleft()

        if board[curr_y][curr_x] == "p":
            return dists[curr_y][curr_x]
        
        for adj_x, adj_y in valid_moves(board, (curr_x, curr_y)):
            if dists[adj_y][adj_x] == -1:
                dists[adj_y][adj_x] = dists[curr_y][curr_x] + 1
                dq.append((adj_x, adj_y))

    return -1

def main() -> None:
    for rows in tokens(int):
        _ = read(int) # number of cols (we do not use this variable)
        board = [list(read(str)) for _ in range(rows)]
        start_y, start_x = read(int) - 1, read(int) - 1

        min_steps = minimum_steps(board, (start_x, start_y))
        print(min_steps) if min_steps != -1 else print("no")


if __name__ == "__main__":
    main()
