from yogi import read, tokens
import heapq


def neighbors(v: tuple[int], obstacles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    '''returns a list of neighbors of v that are not obstacles'''
    return set([(v[0] - 1, v[1]), (v[0] + 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] - 1)]) - obstacles


def h(v: tuple[int, int], dest: tuple[int, int]) -> int:
    '''returns the value of the heuristic of v, calculated with the manhattan norm'''
    return abs(v[0] - dest[0]) + abs(v[1] - dest[1])

     
def min_steps(ori: tuple[int, int], dest: tuple[int, int], obstacles: set[tuple[int, int]]) -> int:
    '''returns the minimum number of steps required to go from x to y avoiding the obstacles'''

    g: dict[tuple[int, int], int] = {ori: 0} # dist(ori, v)
    f: dict[tuple[int, int], int] = {ori: h(ori, dest)} #g(v) + h(v)

    #priority que sorted by f (visited squares whose neighbors are not inspected)
    open: list[tuple[int, tuple[int, int]]] = [(f[ori], ori)] 

    while open:
        # the best candidate of every iteration is the first element in open
        current = heapq.heappop(open)[1] 
        
        if current == dest: 
            return g[current]

        for neighbor in neighbors(current, obstacles):
            new_g = g[current] + 1  # previous cost + 1 step
            
            if new_g < g.get(neighbor, 10e9): # not in open or new path shorter
                f[neighbor] = new_g + h(neighbor, dest)
                g[neighbor] = new_g

                heapq.heappush(open, (f[neighbor], neighbor))

    return g[dest]


def main() -> None:
    ori = (read(int), read(int))
    dest = (read(int), read(int))
    obstacles: set[tuple[int, int]] = {(x, read(int)) for x in tokens(int)}
    print(min_steps(ori, dest, obstacles))


if __name__ == "__main__":
    main()