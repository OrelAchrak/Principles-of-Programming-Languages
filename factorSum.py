def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorSum(num):
    if num <= 1:
        return None  # Invalid input, as the number should be greater than 1

    prime_factors = []
    for i in range(2, num + 1):
        while num % i == 0 and is_prime(i):
            prime_factors.append(i)
            num //= i
    return sum(set(prime_factors))

# Example usage:
number = int(input("Enter an integer greater than 1: "))
result = factorSum(number)

if result is not None:
    print(f"The sum of prime factors of {number} is: {result}")
else:
    print("Invalid input. Please enter an integer greater than 1.")
