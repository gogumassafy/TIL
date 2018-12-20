"""
파이썬 dictionary 활용 기초
"""

# dict = {
#     "대전": 23,
#     "서울": 30,
#     "구미": 20,
# }

# dict.values()

# print(type(dict.values()))

# list = [1, 231,"1231342"]
# print(len(list))

# 1. 평균을 구하세요.
# score = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }



# sum_num = 0
# for i in score:
#     sum_num += score[i]
# average = sum_num / len(score)
# print(average_num)
# print(int(average_num))

# sum_num = 0
# for i in score.values():
#     sum_num += i
# average_num = sum_num / len(score)
# print(average_num)
# print(int(average_num))

# print(sum(score.values()) / len(score))

# 2. 반 평균을 구하시오

# scores = {
#     "철수": {
#         "국어": 80,
#         "영어": 90,
#         "수학": 100
#     }, 
#     "영희": {
#         "국어": 70,
#         "영어": 60,
#         "수학": 50
#     }   
# }

# each_total = 0
# for name in scores:
#     each_total += sum(scores[name].values()) / len(scores[name])
# print(each_total / len(scores))

# each_total = 0
# for name in scores:
#     each_total += scores[name]["국어"]
#     each_total += scores[name]["영어"]
#     each_total += scores[name]["수학"]
# print(each_total / (len(scores) * len(scores[name])))

# each_total = 0
# for name in scores:
#     for each_score in scores[name].values():
#         each_total += each_score
# print(each_total / (len(scores) * len(scores[name])))

# counting_num = 0
# each_total = 0
# for name in scores:
#     for each_score in scores[name].values():
#         each_total += each_score
#         counting_num += 1
# print(each_total / counting_num)

# 3. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
#개념 설명
#for문에서 key와 value 가져오기
# score = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# for key, value in score.items():
#     print(key, value)

# cities = {
#     "서울": [-6, -10, 5],
#     "대전": [-3, -5, 2],
#     "광주": [0, -2, 9],
#     "부산": [2, -2, 9]
# }

# max_city = ""
# min_city = ""
# max_num = -float("inf")
# min_num = float("inf")
# for name, temp in cities.items():
#     if max(temp) > max_num:
#         max_num = max(temp)
#         max_city = name
#     if  min_num > min(temp):
#         min_num = min(temp)
#         min_city = name
# print("최고로 더웠던 도시 " + max_city + ", 추웠던 도시 " + min_city)

import random
num_list = list(range(1,46))

print(random.num_list, 6))