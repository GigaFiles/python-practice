from collections import Counter

ips = []
with open("/tmp/access.log", encoding="utf-8") as f:
    for line in f:
        fields = line.split()
        if fields:
            ips.append(fields[0])

print("=== 1. ips 长这样 ===")
print(ips)

counts = Counter(ips)
print("\n=== 2. counts 长这样 ===")
print(counts)

pairs = counts.most_common(5)
print("\n=== 3. most_common(5) 长这样 ===")
print(pairs)

print("\n=== 4. 循环把每个元组拆开 ===")
for ip, n in pairs:
    print(f"ip={ip}   n={n}")

print("\n=== 5. 正式输出 ===")
for ip, n in pairs:
    print(n, ip)
