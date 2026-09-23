from collections import Counter

def read_ips(path):
    """读出日志里每行的第一个字段(IP)，返回一个列表"""
    ips = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            fields = line.split()
            if fields:
                ips.append(fields[0])
    return ips

ips = read_ips("/tmp/access.log")

for ip, n in Counter(ips).most_common(5):
    print(n, ip)
