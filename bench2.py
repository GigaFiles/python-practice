import random
import time

N = 100_000
lst = list(range(N))
st = set(lst)
samples = [random.randrange(N) for _ in range(1000)]

t = time.perf_counter()
for x in samples:
    _ = x in st
print(f"set:  {(time.perf_counter() - t) * 1000:.2f} ms")

