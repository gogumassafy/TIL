import sys
sys.stdin = open("contact.txt")

def BFS(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        v = queue.pop(0)
        if v in node_dict:
            for i in node_dict[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[v] + 1
    print(f'#{tc + 1} {len(visited) - 1 - visited[::-1].index(max(visited))}')


for tc in range(10):
    N, start = map(int, input().split())
    # 1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
    input_list = list(map(int, input().split()))
    node_dict = {}
    visited = [0] * 101
    queue = []
    for i in range(0, N, 2):
        if input_list[i] not in node_dict:
            node_dict[input_list[i]] = []
            node_dict[input_list[i]] += [input_list[i+1]]
            continue
        node_dict[input_list[i]] += [input_list[i + 1]]

    BFS(start)