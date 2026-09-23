from collections import Counter
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        cost = (time.perf_counter() - t) * 1000
        print(f"[timer] {func.__name__} 耗时 {cost:.2f} ms")
        return result
    return wrapper


@timer
def read_ips(path):
    """从日志文件读出所有 IP，返回一个列表"""
    ips = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            fields = line.split()
            if fields:
                ips.append(fields[0])
    return ips


@timer
def read_paths(path):
    """从日志文件读出所有路径"""
    paths = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            fields = line.split()
            if len(fields) > 2:
                paths.append(fields[2])
    return paths


def count_items(items):
    """统计每个元素出现次数，返回 Counter"""
    return Counter(items)


def show_top(counts, top_n=10):
    """打印 Top N 及百分比"""
    total = sum(counts.values())
    if total == 0:
        print("没有可统计的数据")
        return
    for name, n in counts.most_common(top_n):
        pct = n / total * 100
        print(f"{n:6d}  {pct:5.1f}%  {name}")


def check_alert(counts, threshold):
    """找出超过阈值的项，返回 [(名字, 次数), ...]"""
    return [(name, n) for name, n in counts.items() if n > threshold]


def send_alert(alerts):
    """发送告警（先用打印代替，后面换真 webhook）"""
    for name, n in alerts:
        print(f"!! 告警: {name} 出现 {n} 次，超过阈值")


def main():
    ips = read_ips("/tmp/access.log")
    counts = count_items(ips)
    print("=== Top IP ===")
    show_top(counts, top_n=10)

    paths = read_paths("/tmp/access.log")
    path_counts = count_items(paths)
    print("=== Top 路径 ===")
    show_top(path_counts, top_n=10)

    alerts = check_alert(counts, threshold=30)
    if alerts:
        send_alert(alerts)


if __name__ == "__main__":
    main()
