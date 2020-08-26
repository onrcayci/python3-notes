"""
Counter Example

This is an example on how to define our own iterable objects.

The most important thing is that we need to define two dunder methods:
__iter__ and __next__.

By implementing this, we can create our own terable objects.
"""
class Counter:
    
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(0, 10):
    print(x)