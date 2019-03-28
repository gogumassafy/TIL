
a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3
def DFS(no): #현재 no번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우
    if no>=N:
        for i in range(N) : print(b[i], end=' ')
        print()
        return
    for i in range(N): #a배열의 구슬(단 구슬 중복배제)
        if chk[i] : continue # 사용한 구슬이면 스킵
        chk[i]=1 # 구슬 사용체크
        b[no]=a[i] #구슬 기록
        DFS(no+1) # 다음 상자 시도
        chk[i] = 0 # 구슬 사용해제

# main ============================
DFS(0) # b[0]요소부터 담기 시작
