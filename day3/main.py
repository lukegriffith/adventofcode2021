from numpy import transpose
reverse_map = { 0: 1, 1: 0 }
gamma = [round(sum(i) / len(i)) for i in transpose([ list(map(int,list(f.rstrip()))) for f in open("input.txt") ])]
epsilon = [reverse_map[i] for i in gamma] 
print( int("".join(map(str,gamma)),2) * int("".join(map(str,epsilon)),2))
