
N=int(input())
Ymin=9
Nmax=2
if N==0 :
    print('F')
else:
    for i in range(N):
        cnt, yn = input().split()
        cnt = int(cnt)
        if yn is 'Y':
            if Ymin > cnt: Ymin = cnt
        else:
            if Nmax < cnt: Nmax = cnt

    if Nmax < Ymin:
        print(Ymin)
    else:
        print('F')
