import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()

# Agregar nodos (switch y host)
G.add_node("Switch")
G.add_node("Host", ip="192.168.1.2")

# Agregar una conexión entre el switch y el host
G.add_edge("Switch", "Host")

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=False, node_size=5000, node_color='skyblue')

# Mostrar las etiquetas separadas del nombre y la IP para el host
for node, (x, y) in pos.items():
    if node == "Host":
        plt.text(x, y + 0.1, node, fontsize=12, ha="center")
        plt.text(x, y - 0.1, G.nodes[node]["ip"], fontsize=12, ha="center")
    else:
        plt.text(x, y, node, fontsize=12, ha="center")

plt.show()