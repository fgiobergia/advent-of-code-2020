import networkx as nx
import re
from collections import defaultdict

def bfs(g, queue, costs):
    """
    bfs that maintains a costs dictionary updated during traversal
    g: graph
    queue: queue of nodes to visit (list of [prev_node, prev_bags_required, children_nodes ])
    costs: dictionary of "costs" (i.e. # of bags to use for each type)
    """
    if not queue:
        return
    prev, prev_factor, nodes = queue.pop()
    for node in nodes:
        w = g.edges[(prev, node)]["weight"]
        costs[node] += prev_factor * w
        queue.append((node, prev_factor * w, g.neighbors(node)))
    bfs(g, queue, costs)


if __name__ == "__main__":
    g = nx.DiGraph()

    with open("day07.input") as f:
        for line in f.readlines():
            match = re.match(r"(.+?) bags contain (.+)", line.strip())
            color, others = match.groups()
            contained = others.split(", ")
            if contained[0] == "no other bags.":
                neighbors = []
            else:
                neighbors = [ re.match(r"(\d+) (.+?) bags?\.?", string).groups() for string in contained ]
            
            g.add_weighted_edges_from([ (n, color, int(count)) for count, n in neighbors ])
    
    # "shiny gold" is counted as being reachable in 0, hence the -1
    print(len(nx.single_source_shortest_path_length(g, "shiny gold"))-1)

    g_rev = g.reverse()

    costs = defaultdict(lambda: 0)
    # run a bfs from "shiny gold". for each node, encoutered,
    # update `costs` with the prev node cost * bags required
    bfs(g_rev, [("shiny gold", 1, g_rev.neighbors("shiny gold"))], costs)
    print(sum(costs.values()))