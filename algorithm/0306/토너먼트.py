def attendee_split(start, end):
    if (end - start) <= 1:
        return battle(start, end)

    a = attendee_split(start, (start + end) // 2)
    b = attendee_split(((start + end) // 2) + 1, end)
    return battle(a, b)


def battle(left, right):
    if attendees[left] - attendees[right] == 1 or attendees[left] - attendees[right] == -2 or attendees[left] - attendees[right] == 0:
        return left
    else:
        return right


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    attendees = list(map(int, input().split()))
    print('#{} {}'.format(tc, attendee_split(0, len(attendees)-1)+1))