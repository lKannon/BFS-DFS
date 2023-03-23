from deque import *
from states import *



def dfs(firstState):                #Entrada para primeiro estado
    
    visited = [firstState]          #Lista para estados visitados
    candidates = [firstState]       #Lista para estados candidados a estados finais
    fathers = dict()                #Dicionario com pais dos nós
    
    while(len(candidates) > 0):                 #Enquando a lista de candidatos não termina
        father = candidates[0]                  #Lista de pais recebe primeiro candidato
        print("Candidatos: ", candidates)       #Imprime lista de candidatos
        del candidates[0]                       #Elimina o primeiro candidato da lista
        print("Visited: ", father)              #Printa o elemento Pai como visitado
        
        if check(father):                       #Check se o Pai é o estado final
            path = []                           #Criação e acumulo do caminho
            node = father                       #Armazenar o estado Pai em Nodo
            while node != firstState:           
                path.append(node)
                node = fathers[state2string(node)]
            path.append(firstState)
            path.reverse()
            print("O caminho foi: ", path)
            print('Quantidade de estados percorridos até o estado final: ')
            print(len(path))
            break

        for son in expansion(father):               #Cria filhos
            if son not in visited:                  #Checa se os filhos criados ja nao foram visitados
                print("Inserted: ", son, father)    #Printa os filhos criados
                visited.insert(0,(son))
                fathers[state2string(son)] = father
                candidates.insert(0,(son))
                #input("Stop")
                #for i in queue:
                    #print(i)
