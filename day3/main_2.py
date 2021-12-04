from numpy import transpose
from decimal import Decimal, ROUND_HALF_UP
bits = [list(map(int,list(f.rstrip()))) for f in open("input.txt")]
bit_length = len(bits[0])

def findCriteria(array, common):
    for i in range(bit_length):
        if len(array) <= 1:
            break
        t = transpose(array)
        criteria = Decimal(sum(t[i]) / len(t[i])).quantize(0, ROUND_HALF_UP)
        if common:
            array = [ b for b in array if b[i] == criteria]
        else:
            array = [ b for b in array if b[i] != criteria] 
    if len(array) != 1:
        raise Exception("Error in algorithm")
    return int("".join(map(str,array[0])),2)

print(findCriteria(bits, True) *
    findCriteria(bits, False))
