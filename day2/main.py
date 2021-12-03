#!/bin/env python3 
aim, horizontal, depth = 0, 0, 0
dirs = [d.split() for d in open("input.txt").read().splitlines()]
dir_map = {"up": lambda i, a: a - i, "down": lambda i, a: a + i}
for d, i in dirs:
    if d == "forward":
        horizontal = horizontal + int(i)
        depth = depth + (aim * int(i))
    else:
        aim = dir_map[d](int(i), aim)
print(horizontal * depth)
