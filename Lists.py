#6/49 year 2017
import collections

t1  = [8,12,16,23,25,41]
t2   = [17,23,28,33,35,47]
t3 = [11,14,16,42,47,48]
t4 = [13,18,22,31,44,49]
all     = t1 + t2+t3+t4

counter = collections.Counter(all)
print(counter.most_common())
