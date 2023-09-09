import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os

# Ruta a la carpeta que contiene las imágenes
img_folder = os.path.join(os.path.dirname(__file__), "images")  # "images" es el nombre de la carpeta

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

# Mostrar imágenes para los nodos
for node, (x, y) in pos.items():
    if node == "Switch":
        image_path = os.path.join(img_folder, "switch.png")
        imagebox = OffsetImage(plt.imread(image_path), zoom=0.5)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        plt.gca().add_artist(ab)
        
        # Agregar etiqueta al switch
        plt.text(x, y + 0.1, node, fontsize=12, ha="center")
    elif node == "Host":
        image_path = os.path.join(img_folder, "host.png")
        imagebox = OffsetImage(plt.imread(image_path), zoom=0.5)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        plt.gca().add_artist(ab)
        
        # Agregar etiqueta y dirección IP al host (moviendo la IP más abajo)
        plt.text(x, y + 0.1, node, fontsize=12, ha="center")
        plt.text(x, y - 0.2, G.nodes[node]["ip"], fontsize=12, ha="center")

plt.axis('off')  # Desactivar ejes
plt.show()
