import sys
sys.stdin = open("이진탐색_input.text")

test_num = int(input())

for tc in range(test_num):
    P, A, B = map(int, input().split())
    ra, la = P, 1
    rb, lb = P, 1
    winner = "0"

    while ra > la and rb > lb:
        ca = int((la+ra)/2)
        cb = int((lb+rb)/2)

        if ca == A and cb != B:
            winner = "A"
            break
        elif ca != A and cb == B:
            winner = "B"
            break
        elif ca == A and cb == B:
            winner = "0"
            break

        if ca > A:
            ra = ca
        elif ca < A:
            la = ca

        if cb > B:
            rb = cb
        elif cb < B:
            lb = cb

    print(f"#{tc + 1} {winner}")
