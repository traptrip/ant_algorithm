import numpy as np


class AntColony(object):

    def __init__(self, graph, ants, iterations, decay, alpha=1, beta=1):
        """
        :param graph: двумерный массив numpy.array элементы главной диагонали равны 0
        :param ants: кол-во муравьев в одной итерации (колонии)
        :param iterations: кол-во итераций (колоний)
        :param decay: коэффицент испарения феромона
        :param alpha: const, при α = 0 выбор ближайшего города наиболее вероятен
        :param beta: const, при β = 0 выбор происходит только на основании феромона
        """
        self.graph = graph
        self.ants = ants
        self.iterations = iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = np.ones(graph.shape) / len(graph)
        self.cities = range(len(graph))

    def main_func(self):
        true_shortest_path = ("path", np.inf)  # true_shortest_path[0] - путь, true_shortest_path[1] - длина пути
        for i in range(self.iterations):
            all_paths = self.gen_all_paths()
            self.gen_pheromone(all_paths)
            shortest_path = min(all_paths, key=lambda x: x[1])  # кратчайший путь пройденный i-ой колонией
            if shortest_path[1] < true_shortest_path[1]:
                true_shortest_path = shortest_path
        return true_shortest_path

    def gen_pheromone(self, all_paths):  # генерирует феромон
        sorted_paths = sorted(all_paths, key=lambda x: x[1])  # сортирует по длине пути
        for path, dist in sorted_paths:
            for edge in path:
                self.pheromone[edge] = (1 - self.decay) * self.pheromone[edge] + 1 / self.graph[edge]

    def gen_all_paths(self):  # заносит в массив все пути и их длины, пройденные муравьями
        all_paths = []
        for j in range(self.ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_length(path)))
        return all_paths

    def gen_path_length(self, path):  # генерация длины пути муравья
        dist = 0
        for edge in path:
            dist += self.graph[edge]
        return dist

    def gen_path(self, start):  # генерация пути муравья
        path = []
        tabu_list = set()  # множество индексов уже пройденных городов
        tabu_list.add(start)
        prev_city = start
        for i in range(len(self.graph) - 1):
            new_city = self.find_city(self.pheromone[prev_city], self.graph[prev_city], tabu_list)
            path.append((prev_city, new_city))
            prev_city = new_city
            tabu_list.add(new_city)
        path.append((prev_city, start))
        return path

    def find_city(self, pheromone, length, tabu_list):  # выбор следующего города
        pheromone = np.copy(pheromone)
        pheromone[list(tabu_list)] = 0  # обнуляем значение феромона в уже пройденных городах

        p = (pheromone ** self.alpha) * ((1 / length) ** self.beta)
        possibility = p / p.sum()  # подсчет вероятностей перхода в соседние города

        new_city = np.random.choice(self.cities, 1, p=possibility)[0]  # индекс выбранного города
        return new_city
