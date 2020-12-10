import networkx as nx

if __name__ == "__main__":
    with open("day10.input") as f:
        jol = list(map(int,f.readlines()))
    jol.sort()
    
    jol = [0] + jol + [jol[-1]+3]
    diffs = [ jol[i]-jol[i-1] for i in range(1,len(jol)) ]
    print(diffs.count(1)*diffs.count(3))

    G = nx.DiGraph() # leave the adj. matrix generation to nx
    for i in range(len(jol)-1):
        [ G.add_edge(i,i+j) for j in range(1,4) if i+j<len(jol) and jol[i]+3 >= jol[i+j] ]
    
    adj = nx.to_numpy_array(G)
    prev = 0 # previous graph's "end" point (i.e. current "start" point)
    prod = 1 # product of # of possible ways (across graphs)
    for i in range(1,len(jol)):
        # if the graph only has the (x)->(x+1) edge that
        # connects two portions of the graph (i.e. the edge is a bridge)
        # => split the graphs and compute # of paths for each subgraph
        if adj[:i,i:].sum() == 1:
            new_adj = adj[prev:i+1, prev:i+1]
            G_ = nx.from_numpy_array(new_adj, create_using=nx.DiGraph)
            prod *= len(list(nx.all_simple_paths(G_, 0, len(G_)-1)))
            prev = i
    print(prod)