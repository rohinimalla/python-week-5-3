# Prime number using iteration
def prime_iterative(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Prime number using recursion
def prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime_recursive(n, i + 1)
n = int(input("Enter a number: "))

if prime_iterative(n):
    print("Prime number (using iteration)")
else:
    print("Not a prime number (using iteration)")

if prime_recursive(n):
    print("Prime number (using recursion)")
else:
    print("Not a prime number (using recursion)")
