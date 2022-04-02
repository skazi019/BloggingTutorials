import timeit
import time

a = list(range(1, 100_000_000))
b = tuple(range(1, 100_000_000))

for _ in a:
    pass


def time_function(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        print(f"Time taken to execute {func.__name__}: {time.perf_counter() - start}")

    return inner


# @time_function
def iterate_list(a):
    for _ in a:
        pass


iterate = time_function(iterate_list)
iterate(a)
iterate(b)
