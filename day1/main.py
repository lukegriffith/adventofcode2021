#!/bin/env python3 

def part1():
    last = None
    larger = 0 
    with open("input.txt") as f:
        for l in f:
            current = int(l)
            if type(last) is int and current > last:
                larger = larger + 1
            last = current
    print(larger)

def part2():
    with open("input_2.txt") as f:
        input_arr = []
        for l in f:
            input_arr.append(int(l))
    arr_length = len(input_arr)
    window_groups = []
    start = 0
    for i in range(3,arr_length):
        end = i
        window_groups.append(input_arr[start:end])
        start = start + 1
    last = 0
    larger = 0
    for window in window_groups:
        current = sum(window)
        if current > last:
            larger = larger + 1
        last = current

    print(larger)

part2()
