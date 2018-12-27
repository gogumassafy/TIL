#python 과거
#'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

#pyformat
#'{} {}'.format('one', 'two')

name = '성원'
e_name = 'SEONGWON'
#print("내 이름은 {1}입니다.  My name is {0}".format(name, e_name))

#f-string python 3.6

print(f"안녕하세요. {name}입니다. My name is {e_name}")

#로또
import random
lotto = []
selected = []

lotto = list(range(1,46))
selected = random.sample(lotto, 6)

print("오늘의 행운의 번호는 {0}입니다".format(sorted(selected)))
print(f"오늘의 행운의 번호는 {sorted(selected)}입니다.")

#기타 다른 방법
print("안녕하세요." + name + "입니다.")