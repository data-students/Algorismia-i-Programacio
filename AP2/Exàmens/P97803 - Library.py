import sys

def give(stacks: list[list[str]], stack: int) -> None:

    if 0 <= stack < len(stacks) and stacks[stack]:
        stacks[stack].pop()

def insert(stacks: list[list[str]], stack: int, title: str) -> None:

    if 0 <= stack < len(stacks):
        stacks[stack].append(title)

def print_stacks(stacks: list[list[str]]) -> None:

    for i in range(len(stacks)):
        print(f"Stack {i + 1}:", end="")
        for title in stacks[i]:
            print("", title, end="")
        print()

def main():
    n = int(sys.stdin.readline())

    stacks = [sys.stdin.readline().split() for _ in range(n)]

    sys.stdin.readline()
    
    for line in sys.stdin:
        instruction = line.split()
        if instruction[0] == "LOAN":
            stack = int(instruction[1])
            give(stacks, stack - 1)

        elif instruction[0] == "RETURN":
            title = instruction[1]
            stack = int(instruction[2])
            insert(stacks, stack - 1, title)

        else:
            assert False
    
    print_stacks(stacks)

if __name__ == "__main__":
    main()