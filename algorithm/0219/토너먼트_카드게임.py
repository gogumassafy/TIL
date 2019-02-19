import sys
sys.stdin = open("토너먼트_카드게임.txt")

def attendee_split(start, end):

    if (end - start) == 0:
        return start
    elif (end - start) == 1:
        if attendees[start] - attendees[end] == 1 or attendees[start] - attendees[end] == -2 or attendees[start] - attendees[end] == 0:
            return start
        else:
            return end

    a = attendee_split(start, (start + end) // 2)
    b = attendee_split(((start + end) // 2) + 1, end)
    return a if attendees[a] - attendees[b] == 1 or attendees[a] - attendees[b] == -2 or attendees[a] - attendees[b] == 0 else b



T= int(input())

for tc in range(T):
    N = int(input())
    attendees = list(map(int, input().split()))
    print(f'#{tc+1} {attendee_split(0, len(attendees)-1)+1}')