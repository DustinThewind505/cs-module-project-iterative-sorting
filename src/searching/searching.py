# Write an iterative implementation of Linear Search
def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        cur_item = arr[index]

        if target == cur_item:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    lo_bound = 0
    up_bound = len(arr) - 1

    while lo_bound <= up_bound:
        guess_index = (lo_bound + up_bound) // 2
        guess = arr[guess_index]

        if guess == target:
            return guess_index
        elif guess < target:
            lo_bound = guess_index + 1
        elif guess > target:
            up_bound = guess_index - 1

    return -1  # not found
