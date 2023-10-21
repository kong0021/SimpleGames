def largest_prime(k: int) -> int:
    """
    Finding the largest prime using Sieve of Eratosthenes approach
    Time Complexity = O(n*log(log(n)))
    """
    #Initialize set for O(1) membership test (not in)
    non_prime = set()
    #List for prime numbers
    prime = []
    for i in range(2, k + 1):
        #Because we use set, not in is O(1)
        if i not in non_prime and i != k:
            prime.append(i)
            for j in range(i, k + 1, i):
                non_prime.add(j)
    #Return the largest prime
    # e.g.
    # i = 2, non_prime = [4,6,8,10], prime = [2]. Because 2 not in non_prime so we append
    # i = 3, non_prime = [4,6,8,9,10], prime = [2,3] Because 3 not in non_prime so we append
    # i = 4, non_prime = [4,6,8,9,10], prime = [2,3]  Because 4 already in non_prime so we do not append
    return prime[-1]

# print(largest_prime(3))
