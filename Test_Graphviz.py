import graphviz as gv

g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.edge('A', 'B')

print(g1.source)

g1.render(filename='img/g1')

