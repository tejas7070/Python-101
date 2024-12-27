

def product(arr):
    n = len(arr)
    prod = [1] * n  # Initialize the product array with 1

    # Iterate over the array
    for i in range(n):
        for j in range(n):
            if i != j:  # Skip the current index
                prod[i] *= arr[j]

    return prod

# Example usage
arr = [10, 23, 2, 5, 6]
print(product(arr))  # Output: [1380, 600, 6900, 2760, 2300]