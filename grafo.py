import networkx as nx
import matplotlib.pyplot as plt

# Creamos los vértices
vertices = ["Álgebra Lineal", "Física", "Matemática I", "Matemática II", "Ingeniería"]

# Creamos los arcos con los semestres como pesos
arcos = [("Física", "Matemática I", {"semestre": 2}),
         ("Matemática I", "Matemática II", {"semestre": 3}),
         ("Álgebra Lineal", "Ingeniería", {"semestre": 2}),
         ("Matemática II", "Ingeniería", {"semestre": 4})]

# Creamos el grafo dirigido
grafo = nx.DiGraph()
grafo.add_nodes_from(vertices)
grafo.add_edges_from(arcos)

# Dibujamos el grafo
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20, edge_color="gray", width=2)
edge_labels = nx.get_edge_attributes(grafo, "semestre")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_color='red')

# Imprimimos las dependencias de cada clase por semestre
for semestre in range(1, 5):
    clases_semestre = [clase for clase in vertices if all(grafo.get_edge_data(predecesor, clase)["semestre"] <= semestre for predecesor in grafo.predecessors(clase))]
    
    if clases_semestre:
        print(f"Semestre {semestre}: {', '.join(clases_semestre)}")

# Mostramos el grafo
plt.show()
