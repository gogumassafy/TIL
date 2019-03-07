N, X = input().split()
X = int(X)
for i in range(1, len(N)-1):
    for j in range(i+1, len(N)):
        print('{} {} {}'.format(N[:i], N[i:j], N[j:]))