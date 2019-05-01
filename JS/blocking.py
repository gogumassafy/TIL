from time import sleep
def sleep_3s():
    sleep(3)
    print('Wake up!')

print('start sleeping')
sleep_3s() # blocking
print('end of program')