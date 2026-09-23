from collections import Counter

ips = []
with open("/tmp/access.log", encoding="utf-8") as f:
    for line in f:
        fields = line.split()
        print(fields)
        if fields:
            ips.append(fields[0])

print(Counter(ips).most_common(5))
for ip, n in Counter(ips).most_common(5):
    print(n, ip)
