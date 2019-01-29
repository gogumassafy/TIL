import sys
sys.stdin = open("문자열_비교_input.text")

test = int(input())

for tc in range(test):
    pattern = input()
    text = input()

    for i in range(len(text)):
        for j in range(len(pattern)):
            if i+j >= len(text) or text[i+j] != pattern[j]:
                break
        else:
            print(f'#{tc+1} 1')
            break
    else:
        print(f'#{tc + 1} 0')

