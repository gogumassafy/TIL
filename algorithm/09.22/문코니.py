1,000,000 def solution(cook_times, order, k):
    cook_times = [0] + cook_times
    answer = []
    order_dict = {}
    in_count = [0] * (len(cook_times))
    result = cook_times[:]
    count = [0] * (len(cook_times))
    for key, value in order:
        in_count[value] += 1
        if key in order_dict.keys():
            order_dict[key] += [value]
        else:
            order_dict[key] = [value]
    # print(in_count)
    # print(order_dict)
    q = []
    for i in range(1, len(cook_times)):
        if in_count[i] == 0:
            q.append(i)
    while q:
        idx = q.pop(0)
        if idx == k:
            answer = [count[idx], result[idx]]
            break
        if idx in order_dict.keys():
            for out in order_dict[idx]:
                in_count[out] -= 1
                count[out] = 1 + count[idx]
                result[out] = max(result[out], cook_times[out] + cook_times[idx])
                if in_count[out] == 0:
                    q.append(out)
    return answer