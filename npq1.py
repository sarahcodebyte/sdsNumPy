# reverse 
import numpy

def arrays(arr):
    arr1 = numpy.array(arr, dtype = float)
    arr2 = numpy.array(arr[::-1], dtype = float)
    return arr2

arr = input().strip().split(' ')
result = arrays(arr)
print(result)