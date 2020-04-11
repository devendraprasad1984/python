import threading
import time

def worker():
    print(threading.currentThread().getName()+" thread starting")
    time.sleep(2)
    print(threading.currentThread().getName()+" thread exiting")

def worker_1():
    print(threading.currentThread().getName()+" thread starting")
    time.sleep(4)
    print(threading.currentThread().getName()+" thread exiting")

#start threads
t1=threading.Thread(name='worker',target=worker)
t2=threading.Thread(name='worker_1',target=worker_1)
#df=threading.Thread(target=worker)

t1.start()
t2.start()
#df.start()
