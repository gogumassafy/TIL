import sys
sys.stdin = open("작업순서.txt")

for t in range(10):
    v, e = map(int, input().split());gs, rs = {}, [];raw = list(map(int, input().split())); us = list(range(1, v+1))
    while raw:
        a = raw.pop(0)
        if a in gs: gs[a].append(raw.pop(0))
        else: gs[a] = [raw.pop(0)]
    while us:
        for u in us:
            for v in gs.values():
                if u in v: break
            else:
                rs.append(us.pop(us.index(u)))
                # print(f'rs {rs}')
                if u in gs: print(u, gs.pop(u))
    print(f"#{t+1}", *rs)