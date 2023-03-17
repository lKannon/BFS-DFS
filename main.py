#Classe de estados possíveis 
#position -> Posiçao do robô
#statusR1 -> Status da sala 1 (Limpa ou Suja, 0 ou 1)
#statusR2 -> Status da sala 2 (Limpa ou Suja, 0 ou 1)

class State:
    def _init_(self, position, statusR1, statusR2):
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
    sclean = State(s.position, s.statusR1, s.statusR2)
    if s.position == 1:
        sclean.statusR1 = 'N'
    else:
        sclean.statusR2 = 'N'

    return sclean

def expansion(s):
    s.left = left(s)
    s.right = right(s)
    s.clean = clean(s)

s = State(1, 'S', 'S')
expansion(s)