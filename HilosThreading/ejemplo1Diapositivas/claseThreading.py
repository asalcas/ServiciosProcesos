import random
import threading
import time

class MiThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(random.randint(1,4))
        print ("Soy el hilo: ", self.num)

        