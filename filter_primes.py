
#todo  Filter Primes from a List

# ? Create a function that takes a list and returns a new list containing only prime numbers.
# * Examples

# * filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

# * filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

# * filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

# ! Notes

#     * New list must maintain the order of primes as they first appear in the original list.
#     * Check the Resources tab for help.




import math

# Helper function to check if a number is prime
def is_prime(x):
    if x < 2:
        return False  # Primes are greater than 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False  # Not a prime if divisible by any number from 2 to sqrt(x)
    return True

# Main function to filter primes from the list
def filter_primes(num):
    num2 = []
    for x in num:
        if is_prime(x):  # Only append if the number is prime
            num2.append(x)
    return num2

# Test cases
print(filter_primes([7, 9, 3, 9, 10, 11, 27]))  # ➞ [7, 3, 11]







