def process_solution(a, k):
    sum = 0
    powerset_string = ""
    for i in range(1, k+1):
        if a[i]:
            sum += data[i]
            powerset_string += str(data[i]) + " "
            # print(data[i], end=" ")
    if sum == 10:
        print(powerset_string)

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global  MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k , input)

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
backtrack(a, 0, 10)