# 스레드의 자원 공유, 활성화/비활성화
import threading, time

bread_plate = 0               #공유자원
cv = threading.Condition()

class Maker(threading.Thread):  #빵 생산자
    def run(self):
        global bread_plate
        for _ in range(30):  #반복하는데 변수를 사용하지 않을 때
            cv.acquire()       #공유자원 충돌 방지용
            
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                cv.wait() #스레드 비활성화
                
            bread_plate += 1
            print('빵 생산 : ', bread_plate)                
            cv.notify()  #스레드 활성화
            cv.release()
            time.sleep(0.05)

class Consumer(threading.Thread):  #빵 소비자
    def run(self):
        global bread_plate
        for _ in range(30):
            cv.acquire()
            
            while bread_plate < 1:
                print('빵이 없어서 대기')
                cv.wait() #스레드 비활성화
            bread_plate -= 1
            print('소비 빵 : ', bread_plate)                
            cv.notify()  #스레드 활성화
            cv.release()
            time.sleep(0.1)

mak = []
con = []
for i in range(5):
    mak.append(Maker())

for i in range(5):
    con.append(Consumer())
    
for th1 in mak:
    th1.start()
    
for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()
    
for th2 in con:
    th2.join()
print('-END-')
