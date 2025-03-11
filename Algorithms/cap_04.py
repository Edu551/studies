print('Hello world!')

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + recursive_sum(arr[1:])

def count(arr):
    if len(arr) == 0:
        return 0
    return 1 + count(arr[:-1])

def higher_value(arr):
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] > higher_value(arr[1:]):
        return arr[0]
    else:
        return higher_value(arr[1:])
        
def recursive_binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
       return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return recursive_binary_search(arr, target, left, mid-1)
    else:
        return recursive_binary_search(arr, target, mid+1, right)



# print(sum([1, 2, 3, 4, 5]))
# print(recursive_sum([1, 2, 3, 4, 5]))
# print(count([1, 2, 3, 4, 5]))
# print(higher_value([1, 2, 5, 4, 1]))
print(recursive_binary_search([1, 2, 3, 4, 5], 4))
print(recursive_binary_search([1, 2, 3, 4, 5], 6))