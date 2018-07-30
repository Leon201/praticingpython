from heapq import heapify, heappop, heappush


class priority_queue():
    def __init__(self):
        self.queue = list()
        heapify(self.queue)
        self.index = dict()

    def push(self, priority, label):
        if label in self.index:
            self.queue = [(w, l)
                          for w, l in self.queue if l != label]
            heapify(self.queue)
        heappush(self.queue, (priority, label))
        self.index[label] = priority

    def pop(self):
        if self.queue:
            return heappop(self.queue)

    def __contains__(self, item):
        return item in self.index

    def __len__(self):
        return len(self.queue)

