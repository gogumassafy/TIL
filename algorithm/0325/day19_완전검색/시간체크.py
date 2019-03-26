import time
from time import strftime

start_time = time.time()

###############################
sum = 0
for i in range(10000000):
    sum += i
################################
print(time.time() - start_time, 'seconds')