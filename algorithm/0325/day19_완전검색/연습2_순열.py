# arr = [6,6,7,7,6,7]
arr = [1,2,4,7,8,3]
#arr = [0,5,4,0,6,0]
#arr = [1,0,1,1,2,3]
def babyGin():
    global flag
    check = 0
    
    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]: check += 1
    
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check += 1
    
    if check == 2:
        flag = 1
        return

def perm(n, k):
    if k == n:
        babyGin()
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


flag = 0
perm(6, 0)

if flag :
    print("BabyGin")
else:
    print("Not babyGin")
