# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        cur_uns_index = i
        cur_uns_value = arr[cur_uns_index]

        for al_sor_index in range(cur_uns_index - 1, -1, -1):

            cur_sor_value = arr[al_sor_index]

            if cur_uns_value < cur_sor_value:
                arr[al_sor_index], arr[al_sor_index + 1] = arr[al_sor_index + 1], arr[
                    al_sor_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    while True:
        swaps_this_round = 0

        for i in range(len(arr)):
            cur_item = arr[i]

            for j in range(i + 1, len(arr)):
                item_to_the_right = arr[j]
                if cur_item > item_to_the_right:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps_this_round += 1

        if swaps_this_round == 0:
            return arr


'''
STRETCH: implement the Count Sort function below
Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).
Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 
What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr