"""Given an integer input array heights representing the heights of vertical lines, write a function that returns
the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in
an array of integers and return an integer."""


def most(arr):
    start, end = 0,len(arr) - 1
    currentmax = 0
    while start < end:
        length = end - start
        width = min(arr[start], arr[end])
        area = length * width
        currentmax = max(currentmax, area)
        if start < end:
            start += 1
        else:
            end -= 1
    return currentmax


on = most([2, 4, 2, 5, 6, 2, 3])
print(on)
