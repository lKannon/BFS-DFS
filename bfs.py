from deque import *
from states import *


def bfs(firstState): 
    visited = [firstState]
    candidates = [firstState]
    fathers = dict()

    while(len(candidates) > 0):
        father = candidates[0]
        print("Candidatos: ", candidates)
        del candidates[0]
        print("Visited: ", father)

        if check(father):
            path = []
            node = father
            while node != firstState:
                path.append(node)
                node = fathers[state2string(node)]
            path.append(firstState)
            path.reverse()
            print("Solution", path)
            input()

        for son in expansion(father):
            if son not in visited:
                print("Inserted: ", son, father)
                visited.append(son)
                fathers[state2string(son)] = father
                candidates.append(son)
