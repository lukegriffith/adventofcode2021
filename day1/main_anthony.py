def num_larger(f: str, window: int=1):
    with open(f) as file:
        arr = list(map(int, file.readlines()))
        return len([sum(arr[i:i+window]) for i in range(len(arr[0:-window])) if sum(arr[i+1:i+window+1]) > sum(arr[i:i+window])])

print(num_larger("input.txt")) # part 1
print(num_larger("input_2.txt", 3)) # part 2j
