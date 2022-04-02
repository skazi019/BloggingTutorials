
from functools import lru_cache
from timeit import repeat


@lru_cache(maxsize=16)
def steps_to(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return (steps_to(stair - 3) +
                steps_to(stair - 2) +
                steps_to(stair - 1))


print(steps_to(30))
print(steps_to(15))
print(steps_to.cache_info())
