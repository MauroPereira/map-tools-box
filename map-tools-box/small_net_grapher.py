import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Crear un grafo
G = nx.Graph()

# Agregar nodos (switch y host)
G.add_node("Switch")
G.add_node("Host", ip="192.168.1.2")

# Agregar una conexión entre el switch y el host
G.add_edge("Switch", "Host")

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)  # Usamos una semilla para que la disposición sea la misma cada vez
nx.draw(G, pos, with_labels=False, node_size=1, node_color='skyblue')

# Cargar imágenes de switch y host
switch_img = plt.imread("switch.png")
host_img = plt.imread("host.png")

# Mostrar imágenes para los nodos
for node, (x, y) in pos.items():
    if node == "Switch":
        imagebox = OffsetImage(switch_img, zoom=0.05)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        plt.gca().add_artist(ab)
        
        # Agregar etiqueta al switch
        plt.text(x, y + 0.1, node, fontsize=12, ha="center")
    elif node == "Host":
        imagebox = OffsetImage(host_img, zoom=0.05)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        plt.gca().add_artist(ab)
        
        # Agregar etiqueta y dirección IP al host
        plt.text(x, y + 0.1, node, fontsize=12, ha="center")
        plt.text(x, y - 0.1, G.nodes[node]["ip"], fontsize=12, ha="center")

plt.axis('off')  # Desactivar ejes
plt.show()
