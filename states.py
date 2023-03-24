#Classe de estados possíveis
#Os Estados possiveis sao dados por um vetor de 3 elementos no qual:
#1 Elemento -> position -> Posiçao do robô
#2 Elemento -> statusR1 -> Status da sala 1 (Limpa ou Suja, 0 ou 1)
#3 Elemento -> statusR2 -> Status da sala 2 (Limpa ou Suja, 0 ou 1)
#state -> estado inicial state = [0,1,1] // Posição 0 e as duas salas sujas



#Movimentos possíveis

def expansion(state):
    
    queue = []
    #Mover a esquerda

    stateL = [0, state[1], state[2]]
    queue.append(stateL)

    #limpar a sala atual

    if state[0] == 0:
        stateC = [0, 0, state[2]]
        queue.append(stateC)
    else:
        stateC = [1, state[1], 0]
        queue.append(stateC)

    #Mover a direita

    stateR = [1, state[1], state[2]]
    queue.append(stateR)
    
    return queue

def check(state):
    if state[1] == 0 and state[2] == 0:
        return True
    else:
        return False
    
def state2string(state):
    return ''.join([str(v) for v in state])

