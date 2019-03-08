import numpy as np
from ant_colony import AntColony


#  формирование графа
graph = []
first_row = list(map(float, input().split()))
n = len(first_row)
graph.append(first_row)
for i in range(n - 1):
    row = list(map(float, input().split()))
    graph.append(row)

graph = np.array(graph)
for i in range(n):
    graph[i][i] = np.inf
	
# запуск муравьиного алгоритма
ant_colony = AntColony(graph, 25, 100, 0.5, alpha=1, beta=1)
shortest_path = ant_colony.main_func()

print(int(shortest_path[1]))  #  вывод длины наименьшего пути, найденного муравьями (shortest_path[0] - путь, shortest_path[1] - его длина)
