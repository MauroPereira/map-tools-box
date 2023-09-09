import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()

# Agregar nodos (router y host)
G.add_node("Router")
G.add_node("Host")

# Agregar una conexión entre el router y el host
G.add_edge("Router", "Host")

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue')
plt.show()