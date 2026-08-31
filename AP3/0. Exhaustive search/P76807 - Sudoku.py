from yogi import read
from typing import Optional

Board = list[list[str]]

def update_valids(v_row: list[list[bool]], v_col: list[list[bool]], v_box: list[list[bool]],
                  r: int, c: int, x: int, update_state: bool) -> None:
    """Updates the val lists with the true/false (uptade_state) true/false corresponding
    to insert/delete x into board[r][c]"""
    v_row[r][x - 1] = update_state
    v_col[c][x - 1] = update_state
    v_box[r // 3 * 3 + c // 3][x - 1] = update_state

def solve_rec(board: Board, v_row: list[list[bool]], v_col: list[list[bool]], 
              v_box: list[list[bool]], idx: int) -> Optional[Board]:
    """..."""    
    if idx == 81:
        return board
    else:
        r, c = idx // 9, idx % 9
        if board[r][c] == ".":
            for i in range(9):
                if not v_row[r][i] and not v_col[c][i] and not v_box[r // 3 * 3 + c // 3][i]:
                    board[r][c] = str(i + 1)
                    update_valids(v_row, v_col, v_box, r, c, int(board[r][c]), True)
                    if solve_rec(board, v_row, v_col, v_box, idx + 1):
                        return board
                    update_valids(v_row, v_col, v_box, r, c, int(board[r][c]), False)
                    board[r][c] = "."
        else:
            return solve_rec(board, v_row, v_col, v_box, idx + 1) 

def find_sol_sudoku (board: Board) -> Optional[Board]:
    """..."""
    v_row = [[False] * 9 for _ in range(9)]
    v_col = [[False] * 9 for _ in range(9)]
    v_box = [[False] * 9 for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                update_valids(v_row, v_col, v_box, r, c, int(board[r][c]), True)

    return solve_rec(board, v_row, v_col, v_box, 0)

def write_sudoku(board: Board) -> None:
    """..."""
    print()
    print("\n".join(" ".join([board[r][c] for c in range(9)]) for r in range(9)))

def main() -> None:
    n = read(int)
    print(n)
    for _ in range(n):
        board = [[read(str) for _ in range(9)] for _ in range(9)]
        sol = (find_sol_sudoku(board))
        if sol:
            write_sudoku(sol)
        else:
            print("No solution to this sudoku!")

if __name__ == "__main__":
    main()