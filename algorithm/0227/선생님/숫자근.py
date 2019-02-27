import sys
sys.stdin=open("input.txt")


N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

def root_calc(num):#숫자근 만들어주는 함수
    while True:
        temp = list(map(int, str(num)))
        tot=sum(temp)
        if tot<10 : return tot
        num = tot
    '''
    while True:
        tot=0
        while num:
            tot+=num%10
            num/=10
        if tot<10: return tot
        num=tot
    '''
root_max=0
sol =0
for i in range(N):
    root = root_calc(arr[i]) #숫자근 만들어주는 함수
    #가장 큰 숫자근이면 해당 정수를 솔루션으로
    if root_max<root :
        root_max = root
        sol = arr[i]
    #가장 큰 숫자근과 같다면 더 작은 정수를 솔루션으로
    if root_max == root:
        if sol > arr[i]:
            sol=arr[i]

print(sol)
