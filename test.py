import collections

test = collections.deque(maxlen=6)

for i in range(1, 10):
    test.append(i)


print(test)
