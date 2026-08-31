from yogi import read
from typing import TypeAlias


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


Skyline: TypeAlias = list[Point]


def read_skyline() -> Skyline:
    return [Point(read(int), read(int)) for _ in range(read(int))]


def print_skyline(s: Skyline) -> None:
    print(len(s), end='')
    for p in s:
        print('', p.x, p.y, end='')
    print()


def skyline_superposition(a: Skyline, b: Skyline) -> Skyline:
    
    i = 0 # position of the list of the skyline A
    j = 0 # position of the list of the skyline B
    skyline = list[Point]()
    current_hight_a = 0
    current_hight_b = 0

    while i < len(a) and j < len(b):
        if a[i].x < b[j].x:
            x = a[i].x
            current_hight_a = a[i].y
            max_height = max(current_hight_a, current_hight_b)
            if not skyline or skyline[-1].y != max_height:
                skyline.append(Point(x, max_height))
            i += 1

        elif b[j].x < a[i].x:
            x = b[j].x
            current_hight_b = b[j].y
            max_height = max(current_hight_a, current_hight_b)
            if not skyline or skyline[-1].y != max_height:
                skyline.append(Point(x, max_height))
            j += 1

        else:
            x = a[i].x
            current_hight_a = a[i].y
            current_hight_b = b[j].y
            max_height = max(current_hight_a, current_hight_b)
            if not skyline or skyline[-1].y != max_height:
                skyline.append(Point(x, max_height))
            i += 1
            j += 1
        
    skyline.extend(a[i:])
    skyline.extend(b[j:])

    return skyline


def skyline(skylines: list[Skyline]) -> Skyline:
    
    if len(skylines) <= 1:
        return skylines[0]
    else:
        mid = len(skylines) // 2
        half1 = skyline(skylines[:mid])
        half2 = skyline(skylines[mid:])
        return skyline_superposition(half1, half2)

def main() -> None:
    print_skyline(skyline([read_skyline() for _ in range(read(int))]))


main()

