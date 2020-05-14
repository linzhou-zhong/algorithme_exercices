graph = {}
graph['start'] = {}
graph['start']['A'] = 10

graph['A'] = {}
graph['A']['B'] = 20

graph['B'] = {}
graph['B']['C'] = 1
graph['B']['end'] = 30

graph['C'] = {}
graph['C']['A'] = 1

graph['end'] = {}
# --------------------- 
costs = {}
costs['A'] = 10
costs['B'] = float("inf")
costs['C'] = float("inf")
costs['end'] = float("inf")
# ---------------------
parents = {}
parents['A'] = 'start'
parents['B'] = ''
parents['C'] = ''
parents['end'] = ''

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra_algo():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neignbors = graph[node]
        for each_neignbor in neignbors.keys():
            new_cost = cost + neignbors[each_neignbor]
            if new_cost < costs[each_neignbor]:
                costs[each_neignbor] = new_cost
                parents[each_neignbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

dijkstra_algo()
print(costs)