# iterator - zwraca kolejne elementy
class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Count(low=1, high=8)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))  # StopIteration

for number in counter:
    print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
print("------")
for number in counter:
    print(number)
