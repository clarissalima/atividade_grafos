# -*- coding: utf-8 -*-
from graph import Graph

def load_inst(inst):
    f = open("./insts/inst" + str(inst) + ".txt", 'r')
    graph = ""
    initial = 0
    end = 0
    root = 0
    count = 0

    for line in f:
        if count == 0:
            graph = line[:-1]
        elif count == 1:
            initial = int(line)
        elif count == 2:
            end = int(line)
        elif count == 3:
            root = int(line)
        
        count += 1
        
    return graph, initial, end, root

def load_graph(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break

            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g

inst = int(input("Voce tem 5 instancias de teste prontas para executar selecione uma de 1 a 5:\n"))

if inst < 1 or inst > 5:
    print("Instancia nao existente\n")

graph, initial, end, root = load_inst(inst)

gr = load_graph("./graphs/" + graph)
gr.print()
print()

print("way BFS:")
print(gr.wayBfs(initial, end))
print("DFS:")
print(gr.dfs(root))