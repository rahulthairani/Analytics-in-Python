import networkx as nx
from operator import itemgetter
G = nx.Graph()
nodes = ['Newport Pkwy', 'Lafayette Park', 'JCBS Depot', 'Fairmount Ave',
         'Liberty Light Rail', 'Jackson Square', 'City Hall', 'Sip Ave']
edges = [('Newport Pkwy', 'Lafayette Park', {'count': 74}),
         ('Newport Pkwy', 'JCBS Depot', {'count': 50}),
         ('Newport Pkwy', 'Liberty Light Rail', {'count': 11}),
         ('Lafayette Park', 'Fairmount Ave', {'count': 97}),
         ('Lafayette Park', 'Sip Ave', {'count': 87}),
         ('JCBS Depot', 'Sip Ave', {'count': 69}),
         ('JCBS Depot', 'City Hall', {'count': 6}),
         ('JCBS Depot', 'Fairmount Ave', {'count': 71}),
         ('JCBS Depot', 'Liberty Light Rail', {'count': 4}),
         ('Fairmount Ave', 'Liberty Light Rail', {'count': 2}),
         ('Liberty Light Rail', 'Jackson Square', {'count': 59}),
         ('Liberty Light Rail', 'City Hall', {'count': 52}),
         ('Jackson Square', 'City Hall', {'count': 38})]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
edges_count = G.edges(nbunch='Newport Pkwy', data=True)
rtr_list = list()
for i in edges_count:
    name = i[1]
    count = i[2]['count']
    tpl = (name, count)
    rtr_list.append(tpl)
final_list = sorted(rtr_list, key=itemgetter(1), reverse=True)
r_list = list()
r_list.append(final_list[0][0])
r_list.append(final_list[0][1])
print(r_list)
