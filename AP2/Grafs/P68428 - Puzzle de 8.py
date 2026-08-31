import yogi
import heapq
from typing import Optional

WINNER_BOARD_LIST = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
    ]

WINNER_BOARD_DICT = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 0: (2, 2)
    }

Point = tuple[int, int] # tuple[row, col]

Board = list[list[int]]

def move_board(board: Board, p1: Point, p2: Point) -> None:
    """Aplica un moviment a un tauler, intercanviant dos posicions."""  
    board[p1[0]][p1[1]], board[p2[0]][p2[1]] = board[p2[0]][p2[1]], board[p1[0]][p1[1]]

ListAdj = list[Board]
Graph = list[ListAdj]

def adj_boards(board: Board) -> list[Board]:

    boards: list[Board] = []
    pos_0: Point = (-1, -1)

    for i in range(3):
        for j in range(3):
            n = board[i][j]
            if n == 0:
                pos_0 = (i, j)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dir in directions:
        row, col = pos_0[0] + dir[0], pos_0[1] + dir[1]
        if 0 <= col <= 2 and 0 <= row <= 2:
            adj_board = [board[i][:] for i in range(len(board))] ###############
            move_board(adj_board, pos_0, (row, col))
            boards.append(adj_board)
    return boards

def is_solvable(board: Board):
    """A game is solvable if the number of inversions of the numbers is even"""
    pieces = [board[i][j] for i in range(len(board)) for j in range(len(board)) if board[i][j] != 0]
    
    # Num inversions
    inversions = 0
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            if pieces[i] > pieces[j]:
                inversions += 1
    
    return inversions % 2 == 0

def heuristic(board: Board) -> int:
    
    h = 0
    for i in range(3):
        for j in range(3):
            n = board[i][j]
            if n != 0:
                x, y = WINNER_BOARD_DICT[board[i][j]]
                h += abs(x - i) + abs(y - j)
    return h 

def a_star_min_mov(board: Board) -> Optional[int]:

    g: dict[str, int] = {} # key: str(Board), value: f = g + h

    counter = 0
    g[str(board)] = 0
    pq = [(heuristic(board), counter,  board)]

    while pq:
        curr_f, _, curr_node = heapq.heappop(pq)
        if curr_node == WINNER_BOARD_LIST:
            return curr_f
        for adj_node in adj_boards(curr_node):
            new_g = g[str(curr_node)] + 1
            if str(adj_node) not in g or new_g < g[str(adj_node)]:
                g[str(adj_node)] = new_g
                counter += 1
                heapq.heappush(pq, (new_g + heuristic(adj_node), counter, adj_node))
    return None

def main() -> None:
    """..."""
    board = Board([[yogi.read(int) for _ in range(3)] for _ in range(3)])

    print(a_star_min_mov(board)) if is_solvable(board) else print(None)

if __name__ == "__main__":
    main()