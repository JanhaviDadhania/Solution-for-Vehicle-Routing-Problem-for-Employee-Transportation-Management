from math import inf
from collections import defaultdict
from pprint import pprint
from copy import deepcopy, copy

"""
	assuming the pickup points to be sorted
"""
'''

'''
def add_to_cur_mst(distances, source, sink, current_mst, point, max_allowed_dist, max_number, minimise_distance=False):
	"""
		Takes input as mst in adjacency list representation, and point to be added
		returns the new formed mst, or raises error if given point can not be added
	"""
	current_mst = deepcopy(current_mst)
	cur_mst_distance = 0

	# calculate the distance that vehicle travels going via current mst
	for index, node in enumerate(current_mst[source]):
		if node is source:
			continue
		cur_mst_distance += distances[node][current_mst[source][index - 1]]

	# calculate the new total distance that the vechicle has to travel if current point is added in the mst
	new_total_dist = [inf, inf, inf]
	# our mst is a straight line graph, for each pair of vertices, try inserting the new point by removing the edge between them
	for index, node in enumerate(current_mst[source]):
		if node is source:
			continue

		cur_distance = (
			cur_mst_distance
			- distances[node][current_mst[source][index - 1]]
			+ distances[node][point]
			+ distances[point][current_mst[source][index - 1]]
		)

		# new_total_dist = min(new_total_dist, cur_distance)
		if new_total_dist[0] > cur_distance:
			new_total_dist = [cur_distance, node, current_mst[source][index - 1]]

		if new_total_dist[0] > max_allowed_dist:
			# print(f'for point {point} max distance reached {new_total_dist}')
			raise Exception("Exceeded max allowed distance")

		elif len(current_mst[source]) == max_number:
			raise Exception('Max capacity reached')

		#
		if minimise_distance:
			if distances[source][point] + distances[point][sink] < distances[new_total_dist[-1]] + distances[new_total_dist[1]]:
				raise Exception('Create separate cluster to minimize distance')

		index = current_mst[source].index(new_total_dist[-1])
		current_mst[source].insert(index+1, point)
		#print(f' before returning : using point {point}, mst is : {current_mst}')
		#print(cur_mst_distance)
		#print(current_mst)

		return current_mst


def clusters(distances, source, sink, pickup_points, max_allowed_dist, max_number):
	"""
		Takes input as list of points sorted by their x-coordinates, and position of source, sink
		returns list of Trees of clusters.
		source : starting point of vehicle
		sink : end point of vehicle
	"""
	clusters = []
	# adjacency list representation of tree of current cluster being formed
	# current_mst = {source: [sink]}
	current_mst = defaultdict(list)
	current_mst[source] = [source, sink]

	# for next closest point to the cluster, try adding it to mst
	for point in pickup_points:
		if point is source or point is sink:
			continue

		# current_mst = add_to_cur_mst(distances, source, sink, current_mst, point, max_allowed_dist)

		try:
			current_mst = add_to_cur_mst(distances, source, sink, current_mst, point, max_number, max_allowed_dist)
			# if it exceeds the max threshold of distance that vehicle can travel, form a new cluster and add point to it
		except Exception as e:
			# pprint(f'Error {e} raised on point {point}. appending {current_mst}')
			clusters.append(current_mst)
			current_mst = defaultdict(list)
			current_mst[source] = [source, sink]
			current_mst = add_to_cur_mst(distances, source, sink, current_mst, point, max_number, max_allowed_dist)


	clusters.append(current_mst)

	return clusters
