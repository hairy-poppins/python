import os
import tkinter as tk
import customtkinter as ctk

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import simpledialog, messagebox
import sys


fig, ax = plt.subplots(figsize=(5, 4))

G = nx.MultiGraph()

def add_vertice():
    G.add_node(len(G.nodes) + 1)
    draw_graph()

def draw_graph():
    ax.clear()
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', edgecolors='black', node_size=700)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=12)
 
 # Count parallel edges
    edge_count = {}
    for u, v, key in G.edges(keys=True): #loop through  
        edge_count.setdefault((u, v), 0)
        edge_count[(u, v)] += 1

    parallel_edge_index = {}

    # Draw edges individually with different curves
    for u, v, key in G.edges(keys=True):
        n = edge_count[(u, v)]
        if n == 1:
            rad = 0.0  # straight edge if single
        else:
            parallel_edge_index.setdefault((u, v), 0)
            idx = parallel_edge_index[(u, v)]
            rad = 0.2 * ((idx // 2 + 1) * (-1) ** idx)  # alternating +/- curvature
            parallel_edge_index[(u, v)] += 1

        nx.draw_networkx_edges(
            G, pos, edgelist=[(u, v)], ax=ax,
            arrows=True, arrowstyle='-',
            connectionstyle=f"arc3,rad={rad}"
        )
    

    canvas.draw()

def add_edge():
    if len(G.nodes) < 2:
        messagebox.showerror("Error", "Not enough vertices to create an edge.")
        return
    u = simpledialog.askinteger("", "First Vertice:")
    v = simpledialog.askinteger("", "Second Vertice:")
    if u not in G.nodes or v not in G.nodes:
        messagebox.showerror("Error", "One or both vertices do not exist.")
        return
    
    
    G.add_edge(u, v)
    draw_graph()

def check_euler_path():
    odd_degree_nodes = 0
    for node in G.nodes:
        if G.degree(node) % 2 != 0:
            odd_degree_nodes += 1

    if odd_degree_nodes == 0:
        messagebox.showinfo("Result", "The graph has an Eulerian Circuit.")
    elif odd_degree_nodes == 2:
        messagebox.showinfo("Result", "The graph has an Eulerian Path.")
    else:
        messagebox.showinfo("Result", "The graph does not have an Eulerian Path or Circuit.")

def konigsberg():
    G.clear()
    edges = [(1, 3), (1, 3), (1, 4), (2, 3), (2, 3), (2, 4), (3, 4)]
    G.add_edges_from(edges)
    draw_graph()


def show_info():
    info = "This is a program to find Eulerian paths and circuits in a graph.\n\n" \
        "Eulerian Path: A path that visits every edge exactly once.\n" \
        "Eulerian Circuit: A circuit that visits every edge exactly once and returns to the starting vertex.\n\n"  \
        "Konigsberg Graph: A famous problem that started graph theory involving seven bridges connecting four landmasses. Learn More:\n\n" \
        "Learn More?\n"
    if messagebox.askyesno("Info", info):
        webbrowser.open("https://www.scientificamerican.com/article/how-the-seven-bridges-of-koenigsberg-spawned-new-math/")
    

m = ctk.CTk()
ctk.set_appearance_mode("dark")
m.title('Euler Path Finder')

m.geometry('600x700')

w = ctk.CTkLabel(m, text="Euler Path Finder", font=("Helvetica", 24)).pack()

frame = ctk.CTkFrame(m)
frame.pack(pady=20)


btnV = ctk.CTkButton(frame, text='Add Vertice', width=25, command=add_vertice).pack(side= ctk.LEFT, padx=10)
btnE = ctk.CTkButton(frame, text='Add Edge', width=25, command=add_edge).pack(side= ctk.LEFT, padx=10)
btnCheck = ctk.CTkButton(frame, text='Check Euler Path', width=25, command=check_euler_path).pack(side= ctk.LEFT, padx=10)

# btnDraw = tk.Button(m, text='Draw Graph', width=25, command=draw_graph).pack()
btnKonigsberg = ctk.CTkButton(frame, text='Konigsberg Graph', width=25, command=konigsberg).pack(side= ctk.LEFT, padx=10)


ax.set_axis_off()

#G = nx.Graph()
canvas = FigureCanvasTkAgg(fig, master=m)
canvas.get_tk_widget().pack()

frame2 = ctk.CTkFrame(m)
frame2.pack(pady=20)

btnReset = ctk.CTkButton(frame2,text='Reset', font=("Helvetica", 20),width=80,command=lambda: [G.clear(), draw_graph()]).pack(side= ctk.LEFT, padx=20)
btnInfo = ctk.CTkButton(frame2,text='Info', font=("Helvetica", 20),width=80,command=show_info).pack(side= ctk.LEFT, padx=20)


m.mainloop()
plt.close()
sys.exit()
