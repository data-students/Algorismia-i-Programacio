import yogi
from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Number:
    number: int
    frequency: int

def sort_list_frequency(n1: Number, n2: Number) -> int:
    if n1.frequency < n2.frequency:
        return 1
    elif n1.frequency > n2.frequency:
        return -1
    else:
        return n2.number - n1.number

def create_list_frequencies(n: int) -> list[Number]:
    
    input_list: list[int] = []
    n1 = n
    input_list1 = [yogi.read(int) for _ in range(n1)]
    n2 = yogi.read(int)
    input_list2 = [yogi.read(int) for _ in range(n2)]
    list_frequencies: list[Number] = []

    i = 0
    j = 0

    while i < len(input_list1) and j < len(input_list2):
        num1 = input_list1[i]
        num2 = input_list2[j]
        if num1 < num2:
            input_list.append(num1)
            i += 1
        else:
            input_list.append(num2)
            j += 1
    input_list.extend(input_list1[i:])
    input_list.extend(input_list2[j:])

    prev_num = -1
    for num in input_list:
        if list_frequencies == [] or num != prev_num:
            list_frequencies.append(Number(num, 1))
        else:
            list_frequencies[-1].frequency += 1
        prev_num = num  

    return list_frequencies

def main() -> None:
    n1 = yogi.scan(int)
    while n1 is not None:
        list_frequencies = create_list_frequencies(n1)
        list_frequencies.sort(key=cmp_to_key(sort_list_frequency))
        
        print (f'{list_frequencies[0].number} {list_frequencies[0].frequency}')

        n1 = yogi.scan(int)

if __name__ == "__main__":
    main()