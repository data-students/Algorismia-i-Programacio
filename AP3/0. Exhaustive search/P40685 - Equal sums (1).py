from yogi import read
from collections import deque

def write_sums_rec(s: int, nums: list[int], used_nums: list[bool], idx: int, sol: list[int]) -> None:
    """..."""

    n = len(nums)
    if idx == n:
        if sum(sol) == s:
            print("{" + ",".join([str(x) for x in sol]) + "}")
    else:
        write_sums_rec(s, nums, used_nums, idx + 1, sol)
        
        sol.append(nums[idx])
        used_nums[idx] = True
        write_sums_rec(s, nums, used_nums, idx + 1, sol)
        sol.pop()
        used_nums[idx] = False

def write_sums(s: int, nums: list[int]) -> None:
    """"..."""
    n = len(nums)
    used_nums = [False] * n
    sol: list[int] = []
    write_sums_rec(s, nums, used_nums, 0, sol)

def main() -> None:
    s, n = read(int), read(int)
    nums = [read(int) for _ in range(n)]
    write_sums(s, nums)

if __name__ == "__main__":
    main()