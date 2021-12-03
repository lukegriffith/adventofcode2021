from numpy import transpose
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
bits_oxygen = [list(map(int,list(f.rstrip()))) for f in open("input.txt")]
bits_scrubber = bits_oxygen.copy()
bit_length = len(bits_oxygen[0])

def findCriteria(array, round_behaviour, bit_map):
    for i in range(bit_length):
        if len(array) <= 1:
            break
        t = transpose(array)
        criteria = Decimal(sum(t[i]) / len(t[i])).quantize(0, round_behaviour)
        array = [ b for b in array if b[i] == criteria ]
    if len(array) != 1:
        raise Exception("Error in algorithm", round_behaviour)
    bits = [bit_map[b] for b in array[0]]
    return int("".join(map(str,bits)),2)

print(findCriteria(bits_oxygen, ROUND_HALF_UP, {1:1, 0:0}) * 
    findCriteria(bits_scrubber, ROUND_HALF_DOWN, {1:0, 0:1}))
