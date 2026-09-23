from collections import Counter

counts = Counter()

with open("/tmp/access.log", encoding="utf-8") as f:
    for line in f:
        ip = line.split()[0]
        counts[ip] += 1

total = sum(counts.values())
print(counts.values())
print(total)
print("question 3------->",counts.most_common(10))

for ip, n in counts.most_common(10):
    pct = n /total * 100
    print(f"{n:6d} {pct:5.1f}%  {ip}")


import json

data = dict(counts.most_common(10))
print(json.dumps(data, ensure_ascii=False))
