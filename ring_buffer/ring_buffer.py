class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # add item in storage
    # increase current
    # as long as current < capacity
        # else replace oldest item

    if len(self.storage) < self.capacity and self.storage[self.current] == None:
        self.storage.append(item)
    else:
        self.storage[self.current] = item
    
    self.current = (self.current + 1) % self.capacity
    # print(self.current)

  def get(self):
    # return whole list in storage if not None
    result = []
    for item in self.storage:
        if item != None:
            result.append(item)

    return result