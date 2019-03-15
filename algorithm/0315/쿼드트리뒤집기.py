def reverseTree():
    global raw
    first_char = raw[0]
    raw = raw[1:]
    if first_char != 'x':
        return first_char
    else:
        upperLeft = reverseTree()
        upperRight = reverseTree()
        lowerLeft = reverseTree()
        lowerRight = reverseTree()
    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight


T = int(input())
for tc in range(1, T+1):
    raw = input()
    print(reverseTree())
