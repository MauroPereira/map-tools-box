import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os

# Ruta a la carpeta que contiene las imágenes
img_folder = os.path.join(os.path.dirname(__file__), "images")  # "images" es el nombre de la carpeta

# Crear un grafo
G = nx.Graph()

# Preguntar cuántos hosts están conectados
num_hosts = int(input("Ingrese el número de hosts conectados: "))

# Solicitar las direcciones IP de los hosts
for i in range(1, num_hosts + 1):
    ip = input(f"Ingrese la dirección IP del Host {i}: ")
    G.add_node(f"Host {i}", ip=ip)

# Agregar el switch
G.add_node("Switch")

# Conectar el switch con los hosts
for i in range(1, num_hosts + 1):
    G.add_edge("Switch", f"Host {i}")

# Dibujar el grafo
fig, ax = plt.subplots(figsize=(8, 8))  # Ajusta el tamaño de la figura

pos = nx.spring_layout(G, seed=42)  # Usamos una semilla para que la disposición sea la misma cada vez
nx.draw(G, pos, with_labels=False, node_size=1, node_color='skyblue', ax=ax)  # Utiliza el mismo eje (ax)

# Mostrar imágenes para los nodos
for node, (x, y) in pos.items():
    if node == "Switch":
        image_path = os.path.join(img_folder, "switch.png")
        imagebox = OffsetImage(plt.imread(image_path), zoom=0.5)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        
        # Agregar etiqueta al switch
        ax.text(x, y + 0.1, node, fontsize=12, ha="center")
    elif node.startswith("Host"):
        image_path = os.path.join(img_folder, "host.png")
        imagebox = OffsetImage(plt.imread(image_path), zoom=0.5)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        
        # Agregar etiqueta y dirección IP al host (moviendo la IP más abajo)
        ax.text(x, y + 0.1, node, fontsize=12, ha="center")
        ax.text(x, y - 0.2, G.nodes[node]["ip"], fontsize=12, ha="center")

plt.axis('off')  # Desactivar ejes
plt.show()
