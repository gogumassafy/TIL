ary = [5,2,7,1,3,8,9,3,5,2]

def recselectionsort(ary, s, e):
	mini = s

	if s == e:  return

	for j in range(s+1, e, 1):
		if ary[j] < ary[mini]:
			mini = j

	ary[s], ary[mini] = ary[mini], ary[s]

	recselectionsort(ary, s + 1, e);

def selectionsort(ary):
	for i in range(len(ary)):
		mini = i;
		for j in range(i + 1, len(ary), 1):
			if ary[j] < ary[mini]:
				mini = j
		ary[i], ary[mini] = ary[mini], ary[i]


#selectionsort(ary)
recselectionsort(ary, 0, 10)
print(ary)