"""
Count the semiprime numbers in the given range [a..b]
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.
A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.
Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.
For example, consider an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:
(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:
def solution(N, P, Q)
that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.
For example, given an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
"""


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def is_semiprime(n):
    for d1 in range(2, int(n ** .5) + 1):
        if n % d1 == 0:
            d2 = n / d1
            return is_prime(d1) and is_prime(d2)
    return False


def getAllPrimeTillN(N):
    primes=[-1]*N
    c=2
    while c*c < N:
        ii=2*c
        while(ii<N):
            primes[ii]=c
            ii+=c
        c+=1
    return primes

def getPrimeWithInRange(N, P, Q):
    semi_prime = []
    if max(P) > max(Q) > N:
        return semi_prime
    for i in range(len(P)):
        prime = []
        for num in range(P[i], Q[i] + 1):
            isPrime = True
            for k in range(2, int(num ** 0.5) + 1):
                if (num % k) == 0:
                    isPrime = False
                    break
            if isPrime and num > 1: prime += [num]
        print("prime set", prime)
        semi_prime += [prime]
    return semi_prime

def solution1(N,P,Q):
    semi_prime = []
    if max(P) > max(Q) > N:
        return semi_prime
    for i in range(len(P)):
        arr = []
        for num in range(P[i], Q[i] + 1):
            if is_semiprime(num):
                arr+=[num]
        semi_prime+=[(len(arr),arr)]
    return [i[0] for i in semi_prime]

def solution2(N, P, Q):
    N=N+1
    primes=getAllPrimeTillN(N)
    print(primes)
    prefix=[0]*N
    for x in range(1,N):
        prefix[x]=prefix[x-1]
        first_factor=primes[x]
        second_factor=int(x/first_factor)
        if(primes[x]!=-1 and primes[first_factor]==-1 and primes[second_factor]==-1):
            prefix[x]+=1
    print(prefix)
    results=[]
    for r in range(len(P)):
        results.append(prefix[Q[r]]-prefix[P[r]-1])
    return results
#
# def solution(N, P, Q):
#     from math import sqrt
#     # Find out all the primes with Sieve of Eratosthenes
#     prime_table = [False]*2+[True]*(N-1)
#     print(prime_table)
#     prime = []
#     prime_count = 0
#     for num in range(2, int(sqrt(N))+1):
#         if prime_table[num] == True:
#             prime.append(num)
#             prime_count += 1
#             multiple = num * num
#             while multiple <= N:
#                 prime_table[multiple] = False
#                 multiple += num
#     for num in range(int(sqrt(N))+1, N+1):
#         if prime_table[num] == True:
#             prime.append(num)
#             prime_count += 1
#     # Compute the semiprimes information
#     semiprime = [0] * (N+1)
#     # Find out all the semiprimes.
#     # semiprime[i] == 1 when i is semiprime, or
#     #                 0 when i is not semiprime.
#     for index_former in range(prime_count-1):
#         for index_latter in range(index_former, prime_count):
#             if prime[index_former]*prime[index_latter] > N:
#                 # So large that no need to record them
#                 break
#             semiprime[prime[index_former]*prime[index_latter]] = 1
#     # Compute the number of semiprimes until each position.
#     # semiprime[i] == k means:
#     # in the range (0,i] there are k semiprimes.
#         for index in range(1, N+1):
#             semiprime[index] += semiprime[index-1]
#     # the number of semiprimes within the range [ P[K], Q[K] ]
#     # should be semiprime[Q[K]] - semiprime[P[K]-1]
#     question_len = len(P)
#     result = [0]*question_len
#     for index in range(question_len):
#         result[index] = semiprime[Q[index]] - semiprime[P[index]-1]
#     return result

N = 26
P = [1, 4, 16]
Q = [26, 10, 20]
# solution=getPrimeWithInRange
print("semi prime set counter", solution1(N, P, Q))
