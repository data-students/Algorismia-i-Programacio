import heapq
from yogi import read, tokens
from dataclasses import dataclass

Node = int
listAdj = Node
Graph = list[listAdj]
Map = list[list[str]]

@dataclass
class Point:
    x: int
    y: int 
    def __hash__(self) -> int:
        return hash((self.x, self.y))

USER_MOVES = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]

def heuristic(map: Map, curr: Point, end: Point) -> int:
    """Manhattan distance"""
    return abs(end.y - curr.y) + abs(end.x - curr.x)

def get_valid_moves(map: Map, curr: Point, end: Point) -> list[Point]:
    """..."""
    r = len(map)
    c = len(map[0])
    valid_moves: list[Point] = []

    for usr_dir in USER_MOVES:
        adj_x = curr.x + usr_dir.x
        adj_y = curr.y + usr_dir.y

        if not (0 <= adj_x < c and 0 <= adj_y < r):
            continue
        adj = Point(adj_x, adj_y)
        is_valid = True

        # Mirar que no hayan monstruos al rededor
        for mstr_dir in USER_MOVES:
            mstr_x = adj.x + mstr_dir.x
            mstr_y = adj.y + mstr_dir.y
            if 0 <= mstr_x < c and 0 <= mstr_y < r and map[mstr_y][mstr_x] == "M":
                is_valid = False
                break
        if is_valid:
            valid_moves.append(adj)

    return valid_moves

def a_star(map: Map, ini: Point, end: Point) -> bool:

    counter = 0 # Para evitar que en la pq (tuple[f, counter, posicion]) se hagan comparaciones con la posicion
    f: dict[Point, int] = {}
    g: dict[Point, int] = {}
    
    f[ini] = heuristic(map, ini, end)
    g[ini] = 0
    pq: list[tuple[int, int, Point]] = [] # sorted by f (can't sort Point)
    heapq.heappush(pq, (f[ini], counter, ini))

    while pq:
        _, _, curr_p = heapq.heappop(pq)
        if curr_p == end:
            return True
        
        for adj_p in get_valid_moves(map, curr_p, end):
            adj_g = g[curr_p] + 1

            if adj_p not in g:
                g[adj_p] = -1 # "-1" indica distància infinita
                
            if adj_g < g[adj_p] or g[adj_p] == -1:
                g[adj_p] = adj_g
                f[adj_p] = adj_g + heuristic(map, curr_p, adj_p)
                heapq.heappush(pq, (f[adj_p], counter, adj_p))
                counter += 1

    return False

def read_map(r: int, c: int) -> tuple[list[list[str]], Point, Point]:
    """..."""
    ini, end = Point(-1, -1), Point(-1, -1)
    map: list[list[str]] = []
    for i in range(r):
        row: list[str] = []
        for j, n in enumerate(read(str)):
            if n == "I":
                ini = Point(j, i)
            elif n == "F":
                end = Point(j, i)
            row.append(n)
        map.append(row)
    
    return map, ini, end

def main() -> None:
    for r in tokens(int):
        c = read(int)
        map, ini, end = read_map(r, c)
        print("SI" if a_star(map, ini, end) else "NO")

if __name__ == "__main__":
    main()