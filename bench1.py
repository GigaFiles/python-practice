import random
import time

N = 100_000
lst = list(range(N))
samples = [random.randrange(N) for _ in range(1000)]

t = time.perf_counter()
for x in samples:
    _ = x in lst
print(f"list: {(time.perf_counter() - t) * 1000:.2f} ms")
