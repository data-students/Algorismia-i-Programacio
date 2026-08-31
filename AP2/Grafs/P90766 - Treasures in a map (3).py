import yogi
from typing import TypeAlias
from dataclasses import dataclass
from collections import deque

@dataclass
class Point:
    x: int
    y: int

TreasureMap: TypeAlias = list[list[str]]

def cal_reachable(map: TreasureMap, ini: Point) -> int:

    rows, cols = len(map), len(map[0])

    dq: deque[Point] = deque()
    visited = [[False]*cols for _ in range(rows)]
    dq.append(ini)
    visited[ini.y][ini.x] = True
    tresures_reachable = 0
    
    while dq:
        curr_point = dq.popleft()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = curr_point.x + dx, curr_point.y + dy
            if 0 <= x < cols and 0 <= y < rows and not visited[y][x] and map[y][x] != "X":
                if map[y][x] == "t":
                    tresures_reachable += 1
                dq.append(Point(x, y))
                visited[y][x] = True
    return tresures_reachable


def main() -> None:
    n, _ = yogi.read(int), yogi.read(int) # n: rows, _: cols
    map = [list(yogi.read(str)) for _ in range(n)]

    r, c = yogi.read(int) - 1, yogi.read(int) - 1

    print(cal_reachable(map, Point(c, r)))

if __name__ == "__main__":
    main()