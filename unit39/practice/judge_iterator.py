class TimeIterator:
    def __init__(self, start, stop, index):
        self.start = start
        self.stop = stop
        self.index = index
        self.current = 0

    def __iter__(self):
        return self

    def __next__():
        if index < self.stop - self.start:
            f
        else:
            raise IndexError

    def __getimte__():
        if index < self.stop - self.start:
            
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
