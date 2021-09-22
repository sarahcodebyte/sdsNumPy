import numpy
def arrays(arr, arr1, arr2):
    arr = numpy.array(arr, dtype = int)
    arr1 = numpy.array([arr1], dtype = int)
    arr2 = numpy.array([arr2], dtype = int)

    add = numpy.add(arr1,arr2)
    sub = numpy.subtract(arr1, arr2)
    mul = numpy.multiply(arr1, arr2)
    div = numpy.floor_divide(arr1, arr2)
    mod = numpy.mod(arr1, arr2)
    power = numpy.power(arr1, arr2)
    return add,sub,mul,div,mod,power

arr = input().strip().split(' ')

arr1 = input().strip().split(' ')
arr2 = input().strip().split(' ')
add,sub,mul,div,mod,power = arrays(arr, arr1, arr2)
print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(power)