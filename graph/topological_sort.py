from queue import Queue
from graph import *

def topological_sort(graph):
	queue = Queue()
	indegreeMap = {}

	for i in range(graph.numVertices):
		idegreeMap[i] = graph.get_indegree(i)

		#Queue nodes with inDegree of 0

		if indegreeMap[i] == 0:
			queue.put(i)

	sortedList = []

	while not queue.empty():

		vertex = queue.get()
		sortedList.append(vertex)

		for v in graph.get_adjacent_vertices(vertex):
			indegreeMap[v] = indegreeMap[v] - 1

			if indegreeMap[v] == 0:
				queue.put(v)

	if len(sortedList) != graph.numVertices:
		raise ValueError("This graph as cycle!")

	print(sortedList)