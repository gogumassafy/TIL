def recursioncomb(total, num, string):
    global count

    if total == 10:
        print(string)
        return

    if total > 10 or num == len(a):
        return

    count += 1
    recursioncomb(total + a[num], num + 1, string + str(a[num]) + ' ')
    recursioncomb(total, num + 1, string)


# def powerset(n, k, sum):
#     if n == k:
#         return
#         print(A)
#     else:
#         A[k] = 1
#         powerset(n, k + 1, sum + data[k)
#         A[k] = 0
#         powerset(n, k + 1, sum)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [0 for _ in range(10)]
count = 0
recursioncomb(0, 0, '')
print(count)
# powerset(len(a), 0)
