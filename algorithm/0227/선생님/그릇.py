#import sys
#sys.stdin = open("input.txt")

arr = input()
tot=10
for i in range(1, len(arr)):
    if arr[i]==arr[i-1]:
        tot+=5
    else:
        tot+=10
print(tot)