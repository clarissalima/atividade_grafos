#O código abaixo possui como base os disponilizados no sigaaa com as devidas alterações
#que correspondem às duas questões pedidas
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print("Matriz")
        print(self.matrix)
        print("Lista")
        print(self.list)
        
        
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0
        
        while Q.empty() != True:
            p = Q.get()
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    
    def wayBfs(self, initial, end):
        dist, ant = self.bfs(initial)
        way = []
        v = -1
        i = initial
        aux = self.num_vertices
        antIndex = 0    

        while True:
            n_encontrou = True

            if ant[i] == v:
                way.append(i)
                v = i
                n_encontrou = False

                if way[len(way) - 1] == end:
                    break

            i += 1

            if i >= aux:
                i = 0

            if n_encontrou and i == v:
                ant.pop(v)
                way.pop()
                aux -= 1
                
                if aux == 0 or len(way) == 0:
                    return "Nao existe caminho"
                
                v = way[len(way) - 1]
                          
        return way
    
    def dfs(self, source):
        res = []
        stack = []
        isVisited = [False for _ in range(self.num_vertices)]
        qtdVisited = 0
        stack.append(source)

        while qtdVisited != self.num_vertices:  # Continue enquanto a pilha não estiver vazia
            if len(stack) == 0:
                break
            
            aux = stack.pop()

            if isVisited[aux]:
                continue
            
            res.append(aux)
            isVisited[aux] = True
            qtdVisited += 1

            for x in self.list[aux]:
                stack.append(x)

        return res
        
