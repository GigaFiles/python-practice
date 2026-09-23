from collections import Counter

def read_ips(path):
    """读出日志里每行的第一个字段(IP)，返回一个列表"""
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

ips = read_ips("/tmp/不存在.log")

for ip, n in Counter(ips).most_common(5):
    print(n, ip)
