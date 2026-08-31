from yogi import tokens, read

UNDEF = -1

def num_par_rec(x: int, y: int, n: int, dp: list[list[int]]) -> int:

    if dp[x][y] == UNDEF:
        par = sum(num_par_rec(i, j, n, dp) *num_par_rec(x - i - 1, y - j, n, dp)
                  for i in range(x) for j in range(y + 1))

        cor = sum(num_par_rec(i, j, n, dp)*num_par_rec(x - i, y - j - 1, n, dp)
            for i in range(x + 1) for j in range(y))

        dp[x][y] = (par + cor) % n

    return dp[x][y]
    
def num_par(x: int, y: int, n: int) -> int:
    dp = [[UNDEF] * (y + 1) for _ in range(x + 1)] # dp[x][y] indica el numero de parentizaciones que puedes hacer con x ()'s e y {}'s
    dp[0][0] = 1 # cas base
    return num_par_rec(x, y, n, dp)

def main() -> None:
    for x in tokens(int):
        y = read(int)
        n = read(int)
        print(num_par(x, y, n))
    

if __name__ == "__main__":
    main()