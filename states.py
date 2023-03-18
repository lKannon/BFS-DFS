#Classe de estados possíveis 
#position -> Posiçao do robô
#statusR1 -> Status da sala 1 (Limpa ou Suja, 0 ou 1)
#statusR2 -> Status da sala 2 (Limpa ou Suja, 0 ou 1)
#s -> estado inicial




class State:
    def __init__(self, position, statusR1, statusR2):
        self.position = position
        self.statusR1 = statusR1
        self.statusR2 = statusR2
        self.left = None
        self.right = None
        self.clean = None

def left(s):
    sLeft = State(s.position, s.statusR1, s.statusR2)
    sLeft.position = 1
    return sLeft

def right(s):
    sRight = State(s.position, s.statusR1, s.statusR2)
    sRight.position = 2
    return sRight

def clean(s):
    sClean = State(s.position, s.statusR1, s.statusR2)
    if s.position == 1:
        sClean.statusR1 = 'N'
    else:
        sClean.statusR2 = 'N'

    return sClean

def expansion(s):
    s.left = left(s)
    s.right = right(s)
    s.clean = clean(s)

