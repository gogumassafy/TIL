a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no): # 0개에서 N개까지 고르는 조합
    if no>=N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    b[no] = a[no] # 담기
    DFS(no+1)
    b[no] = 0 # 담지 않기
    DFS(no+1)

def DFS2(no, cnt): # N개중 M개를 고르는 조합
    if no>=N:
        if cnt==2:
            for i in range(N): print(b[i], end=' ')
            print(cnt)
        return
    b[cnt] = a[no] # 담기
    DFS2(no+1, cnt+1)
    b[cnt] = 0 # 담지 않기
    DFS2(no+1, cnt)
# main ============================
#DFS(0) # a[0]요소 구슬부터 시작
DFS2(0, 0) # 0요소부터 시작, 개수는 0개부터