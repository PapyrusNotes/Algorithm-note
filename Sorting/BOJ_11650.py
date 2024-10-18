def print_ns(ns):
    for c in ns:
        print(c[0], c[1])
    print()


N = int(input())
s = []
for _ in range(0, N):
    x, y = map(int, input().split())
    s.append((x, y))

ns = sorted(s, key=lambda x: (x[0], x[1]))
print_ns(ns)
