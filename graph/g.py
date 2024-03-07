class graph:
    def __init__(self,size):
        self.graph = []
        self.vertex = []
        self.size = size

    def add_vertex(self,v):
        self.vertex.append(v)
        temp =[]
        for i in range(self.size):
            temp.append(0)
        self.graph.append(temp)

    def add_edge(self,v1,v2):
        i1 = self.vertex.index(v1)
        i2 = self.vertex.index(v2)
        self.graph[i1][i2] =1
    
    def printf(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.graph[i][j] == 1:
                    print(f"{self.vertex[i]}------>{self.vertex[j]}")


    def delete(self,v1,v2):
        i1 = self.vertex.index(v1)
        i2 = self.vertex.index(v2)
        self.graph[i1][i2] = 0


gr = graph(4)

# ADD VERTEX--
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4)

gr.add_edge(1,2)
gr.add_edge(1,3)
gr.add_edge(2,3)
gr.add_edge(2,2)

gr.printf()
gr.delete(2,2)
print("afterr deletig \n")
gr.printf()
