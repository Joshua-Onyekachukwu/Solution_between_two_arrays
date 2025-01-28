def count_numbers_between_arrays(a, b):
    # Step 1: Find the range of integers to consider
    start = max(a)  # Smallest possible integer to check
    end = min(b)    # Largest possible integer to check

    # Step 2: Initialize the count of valid integers
    count = 0

    # Step 3: Iterate through the range and check conditions
    for num in range(start, end + 1):
        # Check Condition 1: num is divisible by all elements in a
        condition1 = all(num % factor == 0 for factor in a)

        # Check Condition 2: num is a factor of all elements in b
        condition2 = all(multiple % num == 0 for multiple in b)

        # If both conditions are satisfied, increment the count
        if condition1 and condition2:
            count += 1

    return count

# Sample Input
n, m = 2, 3
a = [2, 4]
b = [16, 32, 96]

# Output the result
print(count_numbers_between_arrays(a, b))  # Expected Output: 3
