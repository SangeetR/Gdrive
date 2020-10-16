from threading import Thread
import time


class Mult():
    def __init__(self):
        self.a= 0
        self.b= 0 

    def thread1(self):
        while True:
            self.a += 1
            time.sleep(0.5)
            print(self.a)

    def printall(self):
        while True:
            print(self.a, end = '\r')




obj = Mult()
t = Thread(target=obj.thread1)
# obj.printall()