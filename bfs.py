from deque import *
from states import *


def bfs(firstState):                #Entrada para primeiro estado
    visited = [firstState]          #Lista para estados visitados
    candidates = [firstState]       #Lista para estados candidados a estados finais
    fathers = dict()                #Dicionario com pais dos nós

    while(len(candidates) > 0):                 #Enquando a lista de candidatos não termina
        father = candidates[0]                  #Lista de pais recebe primeiro candidato
        print("Candidatos: ", candidates)       #Imprime lista de candidatos
        del candidates[0]                       #Elimina o primeiro candidato da lista
        print("Visited: ", father)              #Printa o elemento Pai como visitado

        if check(father):                       #Check se o Pai é o estado final
            path = []                           #Criação do caminho
            node = father                       #Armazenar o estado Pai em Nodo
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
