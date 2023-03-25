from bfs import bfs
from dfs import dfs
from states import *

print("Insira o vetor de Estados [ x, x, x] de acordo com:")
print("Classe de estados possíveis")
print("Os Estados possiveis sao dados por um vetor de 3 elementos no qual:")
print("1 Elemento -> position -> Posiçao do robô (0 ou 1)")
print("2 Elemento -> statusR1 -> Status da sala 1 (Limpa ou Suja, 0 ou 1)")
print("3 Elemento -> statusR2 -> Status da sala 2 (Limpa ou Suja, 0 ou 1)\n")
state = []
for i in range(3):
    state.append(int(input()))

bfs(state)
dfs(state)