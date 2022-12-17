#graph wighted edges

#                --------#2
#      #2     ---         |
#         -----           |   #20 weighted edges
#   ------                |
# #5---------------------#10
#         # 6


#edges can be wighted or not weighted
#can be directional[------->,<---------] or not birectioal representation[<----> or --------]

#LL is a form of graph Tree is a form of graph but LL points to one and Tree points to 2 or 1

#node => vertices in graph
# list O(|V|+|E|) wins over matrix in space complexity O(|V|)2 2 is square here
# adding a vertex list O(1) matrix O(|V|)2 2 is square here
# adding a edge both O(1)
# removing a edge matrix O(1) list O(|E|)
# removing a vertices list O(|V|+|E|) wins over matrix in space complexity O(|V|)2 2 is square here

#lsit is better than matrix

# class Graph:
#     def __init__(self):
#         self.adj_list = {}
#
#     def print_graph(self):
#         for vertex in self.adj_list:
#             print(vertex, ':', self.adj_list[vertex])
#
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
#
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False
#
#     def remove_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             try:
#                 self.adj_list[v1].remove(v2)
#                 self.adj_list[v2].remove(v1)
#             except ValueError:
#                 pass
#             return True
#         return False
#
#     def remove_vertex(self, vertex):
#         if vertex in self.adj_list.keys():
#             for other_vertex in self.adj_list[vertex]:
#                 self.adj_list[other_vertex].remove(vertex)
#             del self.adj_list[vertex]
#             return True
#         return False
#
# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_edge('A','B')
# my_graph.add_edge('A','C')
# my_graph.add_edge('A','D')
# my_graph.add_edge('B','D')
# my_graph.add_edge('C','D')
# my_graph.print_graph()
# print('***********')
# my_graph.remove_vertex('D')
# my_graph.print_graph()




###########################################



class Grapp:
    def __init__(self):
        self.d = {}
    def insertv(self,value):
        if value not in self.d.keys():
            self.d[value] = []
        return False
    def display(self):
        for i in self.d:
            print(f'{i} : {self.d[i]}')
    def inserte(self,v1,v2):
        if v1 in self.d.keys() and v2 in self.d.keys():
            self.d[v1].append(v2)
            self.d[v2].append(v1)
        return -1
    def removev(self,v):
        if v in self.d.keys():
            for i in self.d:
                if v in self.d[i]:
                    self.d[i].remove(v)
            print('*',self.d[v])
            del self.d[v]
        return -1

    def removee(self,v):
        if v in self.d.keys():
            for i in self.d:
                if v in self.d[i]:
                    self.d[i].remove(v)
            self.d[v].clear()
        return -1
g = Grapp()
g.insertv('A')
g.insertv('B')
g.insertv('C')
g.insertv('D')
g.inserte('A','B')
g.inserte('A','C')
g.inserte('C','D')
# g.removee('D')
g.removev('D')
g.display()