from collections import Counter

ips = ["1.1.1.1", "1.1.1.2", "1.1.1.1", "1.1.1.3", "1.1.1.1", "1.1.1.2","1.1.1.1"]

counts = Counter()
for ip in ips:
    counts[ip] += 1
print("第1步 counts      =", counts)

top2 = counts.most_common(3)
print("第2步 most_common =", top2)

for ip, n in top2:
    print(f"{n:6d}  {ip}")

