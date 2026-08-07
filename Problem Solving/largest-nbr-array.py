# Find the second largest number in an array
def second_largest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second

print(second_largest([10, 5, 20, 8, 15]))