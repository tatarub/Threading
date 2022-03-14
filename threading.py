import queue
import threading

NUM_ITERS = 2


class Cube():
    def __init__(self, lat):
        self.lat = lat
        
    def volume(self):
        return self.lat ** 3
        
    def length(self):
        return self.lat * 12


def worker(cube, q, attr):
    for num in range(NUM_ITERS):
        func = getattr(cube, attr)
        val = func()
        q.put(val)


if __name__ == "__main__":
    que = queue.Queue()
    cube = Cube(2)
    t1 = threading.Thread(target=worker, args=(cube, que, "volume"))
    t2 = threading.Thread(target=worker, args=(cube, que, "length"))
    t2.start()
    t1.start()
    t2.join()
    t1.join()
    while not que.empty():
        result = que.get()
        print(result)
        
