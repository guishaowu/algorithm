import random


input = []
for i in xrange(100):
    key = random.randint(1, 10000)
    if key not in input:
        input.append(key)
input = sorted(input)


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

for i, key in enumerate(input):
    assert i == binary_search(input, key)
assert -1==binary_search(input, input[0]-1)
assert -1==binary_search(input, input[-1]+1)

