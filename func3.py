from collections import Counter

def read_ips(path):
    """读出日志里每行的第1列(IP)，返回一个列表"""
    ips = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                fields = line.split()
                if fields:
                    ips.append(fields[0])
    except FileNotFoundError:
        print(f"错误: 文件 {path} 不存在")
    return ips

def read_paths(path):
    """读出日志里每行的第3列(路径)，返回一个列表"""
    paths = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                fields = line.split()
                if fields:
                    paths.append(fields[2])
    except FileNotFoundError:
        print(f"错误: 文件 {path} 不存在")
    return paths

print("=== Top IP ===")
ips = read_ips("/tmp/access.log")
for ip, n in Counter(ips).most_common(5):
    print(n, ip)

print("=== Top 路径 ===")
paths = read_paths("/tmp/access.log")
for p, n in Counter(paths).most_common(5):
    print(n, p)
