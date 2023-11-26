class Time:
    seconds: int = 0
    minutes: int = 0
    hours: int = 0

    __max_time_seconds = 24 * 60 * 60

    def __init__(self, s, m, h):
        self.secondsToTime(s + m * 60 + h * 60 * 60)

    def increase(self, seconds, minutes=0, hours=0):
        delta_seconds = self.inSeconds() + Time(seconds, minutes, hours).inSeconds()
        self.secondsToTime(delta_seconds)

    def decrease(self, seconds, minutes=0, hours=0):
        delta_seconds = self.inSeconds() - Time(seconds, minutes, hours).inSeconds()
        self.secondsToTime(delta_seconds)

    def secondsToTime(self, seconds: int):
        seconds = seconds % self.__max_time_seconds

        self.hours = seconds // (60 * 60)
        seconds -= self.hours * 60 * 60

        self.minutes = seconds // 60
        seconds -= self.minutes * 60

        self.seconds = seconds

    def secondsUntilMidnight(self):
        return self.__max_time_seconds - self.inSeconds()

    def inSeconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


# task 4
t = [Time(15, 15, 15), Time(59, 59, 23), Time(1, 0, 0)]

for i in t:
    print("Amount of minutes:", i.minutes + i.hours * 60)
    s = "Before: " + str(i)
    i.decrease(25)
    s += "\tAfter: " + str(i)
    print(s)
    print()

# task 9
t = [Time(15, 15, 15), Time(59, 59, 23), Time(1, 5, 1)]

for i in t:
    print("Amount of seconds:", i.seconds + i.minutes * 60 + i.hours * 60 * 60)
    print()
    s = "Before: " + str(i)
    i.increase(5)
    s += "\tAfter: " + str(i)
    print(s)

# task 15
t = [Time(15, 15, 15), Time(59, 59, 23), Time(1, 5, 1)]

for i in t:
    print("{} minutes until midnight".format(int(i.secondsUntilMidnight() / 60)))
    s = "Before: " + str(i)
    i.increase(0, 100)
    s += "\tAfter: " + str(i)
    print(s)
    print()
