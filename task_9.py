bulls_n, families_k = map(int, input().split())
bulls_free = bulls_n % families_k
print(bulls_free)
