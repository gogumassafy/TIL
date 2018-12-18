#1
numbers = [2, 3, 6, 11, 8]

yaho = ""

for i in numbers:
    yaho += (str(i) + " ")
    #print(i, end = " ")

print(yaho)
    
#2
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

oddN = []
evenN = []

for i in numbers2:
    if i % 2 != 0:
        oddN.append(i)
    else: 
        evenN.append(i)

print(oddN, "홀수입니다.")
print(evenN, "짝수입니다")