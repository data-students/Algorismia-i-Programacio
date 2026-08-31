from yogi import read, tokens

def max_grannies_rec(g_rem: int, grannies: list[int], idx: int, visited: list[bool], 
                     curr_saved: int, waiting: int, max_saved: int) -> int:
    
    n = len(visited)
    
    # Poda: les iaies que queden per salvar no arriben a les maximes o queden mes bombers que escoles
    if curr_saved + waiting < max_saved or g_rem > n - idx:
        return max_saved

    # Cas base: ens quedem sense bombers
    if g_rem == 0:
        return curr_saved
    
    # Cas recurssiu: Fem combinacions de bombers en escoles, contabilitzant les iaies salvades
    for i in range(idx, n):
        
        # Modificar les caselles (i - 1, i, i + 1) apropiadament
        new_grannies = grannies[:]
        ant = 0
        post = 0
        
        # Casella antarior
        if i - 1 >= 0:
            if i - 2 >= 0 and visited[i - 2]:
                ant += grannies[i - 1]
                new_grannies[i - 1] = 0
            else:
                ant += grannies[i - 1] // 2
                new_grannies[i - 1] //= 2

        # Casella actual
        new_grannies[i] = 0

        # Casella posterior
        if i + 1 < n:
            post += grannies[i + 1] // 2
            new_grannies[i + 1] //= 2
        
        potential_saved = ant + grannies[i] + post

        new_waiting = waiting - sum(new_grannies[idx:i]) - potential_saved

        visited[i] = True
        find_max_saved = max_grannies_rec(g_rem - 1, new_grannies, i + 1, visited, curr_saved + potential_saved, new_waiting, max_saved)
        visited[i] = False

        if find_max_saved > max_saved:
            max_saved = find_max_saved
    
    return max_saved


def max_grannies(g: int, grannies: list[int]) -> int:
    
    n = len(grannies)
    visited = [False] * n
    waiting = sum(grannies)
    return max_grannies_rec(g, grannies, 0, visited, 0, waiting, 0)

def main() -> None:
    for g in tokens(int):
        n = read(int)
        grannies = [read(int) for _ in range(n)]

        print(max_grannies(g, grannies))

if __name__ == "__main__":
    main()