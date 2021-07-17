import time


class trafficlight:
    __color = "gray"

    def running(self):
        while True:
            print("red")
            time.sleep(7)
            print("yellow")
            time.sleep(2)
            print("green")
            time.sleep(5)
            print("yellow")
            time.sleep(2)
tl = trafficlight()
tl.running()