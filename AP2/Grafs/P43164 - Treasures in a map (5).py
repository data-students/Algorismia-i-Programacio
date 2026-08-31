import yogi
from typing import TypeAlias
from dataclasses import dataclass
from collections import deque

@dataclass
class Point:
    x: int
    y: int

TreasureMap: TypeAlias = list[list[str]]

def cal_max_distance(map: TreasureMap, ini: Point) -> int:

    rows, cols = len(map), len(map[0])
    second_furthest = 0
    furthest = 0

    dq: deque[tuple[Point, int]] = deque() # Point: point, int: distance
    visited = [[False]*cols for _ in range(rows)]
    dq.append((ini, 1))
    visited[ini.y][ini.x] = True

    while dq:
        curr_point, dist = dq.popleft()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = curr_point.x + dx, curr_point.y + dy
            if 0 <= x < cols and 0 <= y < rows and not visited[y][x] and map[y][x] != "X":
                if map[y][x] == "t":
                    second_furthest = furthest
                    furthest = dist
                dq.append((Point(x, y), dist + 1))
                visited[y][x] = True

    return second_furthest


def main() -> None:
    n, _ = yogi.read(int), yogi.read(int) # n: rows, _: cols
    map = [list(yogi.read(str)) for _ in range(n)]

    r, c = yogi.read(int) - 1, yogi.read(int) - 1
    max_distance = cal_max_distance(map, Point(c, r))
    print(f"second maximum distance: {max_distance}") if max_distance else print("we cannot reach two or more treasures")

if __name__ == "__main__":
    main()
