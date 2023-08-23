class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time):
        hour, minute, second = map(int, time.split(':'))
        return 1 <= hour and 24 >= hour and 0 <= minute and 59 >= minute and 0 <= second and 60 >= second

    @staticmethod
    def from_string(time):
        hour, minute, second = time.split(':')
        t = Time(hour, minute, second)
        return t


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다')
