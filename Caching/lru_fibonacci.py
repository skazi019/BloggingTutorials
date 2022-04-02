from functools import lru_cache


@lru_cache(maxsize=16)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print([fibonacci(n) for n in range(16)])
print(fibonacci.cache_info())
