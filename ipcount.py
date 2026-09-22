from collections import Counter

counts = Counter()

with open("/tmp/access.log", encoding="utf-8") as f:
    for line in f:
        ip = line.split()[0]
        counts[ip] += 1

for ip, n in counts.most_common(10):
    print(f"{n:6d}  {ip}")

