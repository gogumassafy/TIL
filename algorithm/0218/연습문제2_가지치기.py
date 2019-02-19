def process_solution(a, k, sum_powerset):
    if sum_powerset != 10: return
    for i in range(1, k+1):
        if a[i]:
            print(data[i], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum_powerset):
    if sum_powerset > 10: return

    global  MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum_powerset)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            if a[k]:
                backtrack(a, k , input, sum_powerset + data[k])
            else:
                backtrack(a, k, input, sum_powerset)
MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
backtrack(a, 0, 10, 0)