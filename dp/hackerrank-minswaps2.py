#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    count = 0
    hash_map = {}
    for j in range(len(arr)):
        value = arr[j]
        hash_map[value] = j
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            index = hash_map[i + 1]
            arr[i], arr[index] = arr[index], arr[i]
            hash_map[arr[i]] = i
            hash_map[arr[index]] = index
            count +=1
            
            
    return count
                    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()