from collections import Counter


def read_ips(path):
    """从日志文件读出所有 IP，返回一个列表。"""
    ips = []

    with open(path, encoding="utf-8") as f:
        for line in f:
            fields = line.split()
            if fields:
                ips.append(fields[0])

    return ips


def count_ips(ips):
    """统计每个 IP 出现次数，返回 Counter。"""
    return Counter(ips)


def show_top(counts, top_n=10):
    """打印 Top N 及百分比。"""
    total = sum(counts.values())

    if total == 0:
        print("没有可统计的 IP")
        return

    for ip, n in counts.most_common(top_n):
        pct = n / total * 100
        print(f"{n:6d}  {pct:5.1f}%  {ip}")


def main():
    ips = read_ips("/tmp/access.log")
    counts = count_ips(ips)
    show_top(counts, top_n=10)


if __name__ == "__main__":
    main()
