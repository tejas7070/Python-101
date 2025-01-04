
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def max_in_array(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

arr = [10, 43, 22, 50]
max = max_in_array(arr)
print(f"The maximum value in the array is: {max}")
print(f"The factorial of the maximum value is: {factorial(max)}")