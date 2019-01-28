def bruteForce(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            return i
    return -1

def bruteForce2(text, pattern):
    i = 0
    j = 0
    M = len(pattern)
    N = len(text)
    while j < M and i < N:
        if text[i] != pattern[j]:
            i -= j
            j -= 1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return -1

text = "This thii a book!~"
pattern = "Thii"
print(bruteForce(text, pattern))
print(bruteForce2(text, pattern))
print(text.find(pattern))
