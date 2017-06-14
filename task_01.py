#python2

import heapq
import sys
import itertools

class Vertex():
    
    def __init__(self, id, dist = float('inf')):
        self.id = id
        self.dist = dist
        self.parent = None
        #self.status = 'Not Removed'
        #self.vertex = (self.dist, [self.id, self.parent])

    @property
    def vertex(self):
        return [self.dist, self.id, self.parent]

    @property
    def dist(self):
        return dist

    @dist.setter
    def dist(self, value):
        self.dist = value

    #@id.setter
    #def id(self, value):
    #    self.id = value

    #@parent.setter
    #def parent(self, value):
    #    self.parent = value

    def __str__(self):
        return str(self.id) + "  " +  str(self.dist)

class Edge():

    def __init__(self, info):
        self.start = info[0]
        self.end = info[1]
        self.weight = info[2]

    def __str__(self):
        return str(self.start) + str(self.end) + str(self.weight)

        
#test = Vertex(10)
#print test.vertex

var = sys.stdin.readline()
var = map(int, var.strip('').split(' '))

ver_num = var[0]
edge_num = var[1]
heap = []
vertex_dict = {}
graph = {ver: set() for ver in range(1, ver_num + 1)}
counter = itertools.count()
removed = 'Removed'

#for ver in range(1, ver_num + 1):
#    vertex = Vertex(ver)
#    heapq.heappush(heap, vertex.vertex)
#    vertices_list.append(vertex)

for i in range(edge_num):
    edge = sys.stdin.readline()
    edge = list(map(int, edge.strip('').split(' ')))
    edge = Edge(edge)
    graph[edge.start].add(edge)

def dijkstra(graph, s):
    print "dijkstra algorithm starts here"
    for ver in range(1, ver_num + 1):
        vertex = Vertex(ver)
        if ver == s:
            vertex.dist = 0
            print "vertex - {}".format(vertex)
        heapq.heappush(heap, vertex.vertex)
        print "heap ", ver, heap 
        vertices_list.append(vertex)
    #while heap:
    u = heapq.heappop(heap)   
    print "u - {}".format(u)
    print "heap - {}".format(heap)
    print "graph", graph
    id = u[1][0]
    print "id ", id 
    for edge in graph[id]:
        end = edge.end
        weight = edge.weight
        print 'end', end
        print 'weight', weight
        beg_vertex = vertices_list[id]
        end_vertex = vertices_list[end]
        print end_vertex.dist
        print beg_vertex.dist
        print weight
        if end_vertex.dist > beg_vertex.dist + weight:
            end_vertex.dist = beg_vertex.dist + weight
            print 'end_vertex ', end_vertex
            
    print heap

#dijkstra(graph, 1)

def add_vertex(vertex, vertex_id, new_dist):
    print 'we would like to add vertex - with id -{}, dist - {} '.format(vertex_id, new_dist)
    #node = vertex.id   
    #dist = vertex.dist
    if vertex_id in vertex_dict:
        print 'if statement before remove', vertex 
        remove_vertex(vertex)
    count = next(counter)
    new_vertex = Vertex(vertex_id, new_dist) 
    new_entry = [new_vertex.dist, new_vertex]
    print 'new entry', new_entry
    vertex_dict[new_vertex.id] = new_entry
    heapq.heappush(heap, new_entry)
    print 'heap after add_vertex', heap

def remove_vertex(vertex):
    entry = vertex_dict.pop(vertex.id)
    entry[1].id = removed
    

def pop_vertex():
    while heap:
        vertex = heapq.heappop(heap)[1]
        if vertex.id is not removed:
            del vertex_dict[vertex.id]
            return vertex
    return KeyError('pop from empty heap')

def dict_print(dct):
    for i in dct:
        print dct[i]

def dijkstra2(graph, s):
    fixer = 0
    for ver in range(1, ver_num + 1):
        vertex = Vertex(ver)
        if ver == s:
            vertex.dist = 0
        add_vertex(vertex, ver, vertex.dist)
    vertex_dict_2 = dict(vertex_dict)
    dict_print(vertex_dict_2)

    while heap and fixer <= 10:
        fixer += 1
        u = pop_vertex()
        print 'pulling vertex from the heap', u
        print 
        for edge in graph[u.id]:
            print 'edge that coming out of u', edge
            if edge.end in vertex_dict:
                print 'if {} in vertex_dict - yes'.format(edge.end)
                working_vertex = vertex_dict[edge.end][1]
                print 'then working vertex is ', working_vertex
                if working_vertex.dist > u.dist + edge.weight:
                    working_vertex.dist = u.dist + edge.weight
                    working_vertex.parent = u.id
                    print 'new working_vertex', working_vertex
                    add_vertex(working_vertex, working_vertex.id, working_vertex.dist)
        for h  in heap:
            print h[0], "  ", h[1]

dijkstra2(graph, 1)

for h in heap:
    print h
    
#print vertex_dict

#print graph

print vertex_dict_2
