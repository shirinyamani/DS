class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex, edge):
        self.gdict[vertex].apped(edge)

#Question 1
    def is_route_bfs(self, start, end):
        queue = [start] #pushing the start node to queue
        visited = [start]
        path = False

        while queue:
            denode = queue.pop(0) #pop first element

            for adjnode in self.gdict[denode]:
                if adjnode not in visited:
                    if adjnode == end: #chehck the route
                        path = True
                        break
                    else:
                        visited.append(adjnode) #if not path the mark it as visited
                        queue.append(adjnode)
        return path
