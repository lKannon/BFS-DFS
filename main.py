from deque import queue
from states import *
s = State(1, 'S', 'S')
queue.append(s)
for item in queue:
    print(vars(item))
while s.statusR1 == 'S' or s.statusR2 == 'S':
    expansion(s)