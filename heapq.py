import heapq

class Pq:
    def __init__(self):
        self.heap = []
        
    def enq(self, item, p):
        heapq.heappush(self.heap, (p, item))
    
    def deq(self):
        if self.heap == None:
            return None
        r