# Ant_algorithm

Как работает алгоритм:
Муравьи проходят все города, начиная из стартого и заканчивая в нём же.
На своем пути они откладывают феромон, при том, чем короче весь путь, тем больше феромона муравьи отложат на нём.
Муравей выбирает путь, основываясь на длине до ближайшего города и уровне феромона на пути.

1) Определяем константы: кол-во муравьев, кол-во колоний (итераций), коэффицент испарения феромона, альфа, бета.

2) Генерируем матрицу значений феромона т.о., что значение феромона между i-м и j-м городами было равно единице деленой на кол-во всех городов.

3) Муравей определяет в какой город пойти, пользуясь данными формулами:

		value = (pheromone ** alpha) * ((1.0 / length) ** beta)
	
value считается для всех соседних городов, за исключением тех, которые муравей уже посетил
высчитывается вероятность перехода в следующий город:

		probability = value / sum_of_all_values

Следуя данным правилам, муравей обходит все города.

4) После того как муравей обошёл все города, значение феромона на его пути пересчитывается согласно следующему правилу:
	
		new_pheromone = (1 - decay) * old_pheromone + 1 / distanse_between_two_cities, 
	
где decay - коэффицент испарения, old_pheromone - старое значение феромона, distanse_between_two_cities - расстояние м/у рассматриваемыми городами.

5) Затем просто из всех путей, пройденных всеми муравьями, выбираем самый короткий.

6) Повторяем 3), 4), 5) n раз. Кол-во итераций указывалось в пункте 1)
	
	
	
	

