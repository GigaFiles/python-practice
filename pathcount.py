from collections import Counter

counts = Counter()

with open("/tmp/access.log", encoding="utf-8") as f:
    for line in f:
        path = line.split()[2]
        counts[path] += 1

for path, n in counts.most_common(10):
    print(f"{n:6d}  {path}")

