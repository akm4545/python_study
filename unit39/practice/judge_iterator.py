class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < stop: 
            next_time = '{0:02d}:{1:02d}:{2:02d}'.format(self.current // 60 // 60 % 24, self.current // 60 % 60, self.current % 60 % 60)
            self.current += 1
            return next_time
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < self.stop - self.start:
            index_time = self.start + index
            return '{0:02d}:{1:02d}:{2:02d}'.format(index_time // 60 // 60 % 24, index_time // 60 % 60, index_time % 60 % 60)
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
