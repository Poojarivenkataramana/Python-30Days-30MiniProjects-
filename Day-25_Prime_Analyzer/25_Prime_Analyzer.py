# ----------------------------------------------------
# Day 25: Prime Number & Factorization Analyzer
# Concepts: Mathematical Algorithms, Optimization, Lists, Factorization
# ----------------------------------------------------

import math
from collections import Counter

def is_prime(n):
    if n <= 1:
        return False, []
    if n == 2:
        return True, [1, 2]

    factors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    factors.sort()
    return len(factors) == 2, factors

def get_primes_in_range(start, end):
    if end < 2 or start > end:
        return []
    primes = []
    for num in range(max(2, start), end + 1):
        prime_status, _ = is_prime(num)
        if prime_status:
            primes.append(num)
    return primes

def prime_factors(n):
    if n <= 1:
        return {}
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return Counter(factors)

def main():
    print("=" * 50)
    print("🔢 PRIME NUMBER & FACTORIZATION ANALYZER 🔢".center(50))
    print("=" * 50)

    while True:
        print("\nSelect Mode:")
        print("1. Single Number Primality & Factor Check")
        print("2. Find All Primes in a Range [A, B]")
        print("3. Prime Factorization Decomposition")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            try:
                num = int(input("\nEnter positive integer to test: "))
                prime_status, factors = is_prime(num)
                print("\n" + "-" * 45)
                print(f"Number Tested : {num}")
                if prime_status:
                    print(f"Status        : ✅ PRIME NUMBER!")
                else:
                    print(f"Status        : ❌ COMPOSITE (Not Prime)")
                print(f"All Factors   : {factors}")
                print(f"Total Factors : {len(factors)}")
                print("-" * 45)
            except ValueError:
                print("❌ Invalid integer.")

        elif choice == "2":
            try:
                start = int(input("\nEnter Start Range: "))
                end = int(input("Enter End Range  : "))
                primes = get_primes_in_range(start, end)
                print("\n" + "-" * 45)
                print(f"Primes between {start} and {end}: ({len(primes)} found)")
                print("-" * 45)
                print(primes if primes else "No prime numbers found in range.")
                print("-" * 45)
            except ValueError:
                print("❌ Invalid integer input.")

        elif choice == "3":
            try:
                num = int(input("\nEnter integer for prime factorization: "))
                if num <= 1:
                    print("❌ Please enter an integer greater than 1.")
                    continue
                decomp = prime_factors(num)
                expr_parts = [f"{factor}^{count}" if count > 1 else f"{factor}" for factor, count in sorted(decomp.items())]
                print("\n" + "-" * 45)
                print(f"Prime Decomposition for {num}:")
                print(f"Formula: {num} = {' × '.join(expr_parts)}")
                print("-" * 45)
            except ValueError:
                print("❌ Invalid integer.")

        elif choice == "4":
            print("\nGoodbye! Keep exploring numbers! 🧮\n")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
