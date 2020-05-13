#thread를 이용해 날짜 및 시간 출력
import time

now = time.localtime()
print('현재는 {}년 {}월 {}일'.format(now.tm_year, now.tm_mon, now.tm_mday))
print('{}시 {}분 {}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
print('오늘은 {}요일, 올해 {}번째 날'.format(now.tm_wday, now.tm_yday)) #월0 화1 수2 목3 금4 토5 일6

import threading

def cal_show():
    now = time.localtime()
    print('현재는 {}.{}.{}  {}:{}:{} '.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    
def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 34: break
        cal_show()
        time.sleep(1)
        
th = threading.Thread(target=myRun)
th.start()

th.join()
print('프로그램 종료')