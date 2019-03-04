S, X = input().split()

X = int(X)

for i in range(1, len(S)):
    if int(S[0:i]) + int(S[i:].lstrip('0')) == X:
        print('{}+{}={}'.format(S[0:i], S[i:].lstrip('0'), X))
        break
else:
    print('NONE')