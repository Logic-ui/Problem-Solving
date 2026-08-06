# Find the missing number in an array of 1 to n
def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing([1,2,4,5,6], 6))  # 3