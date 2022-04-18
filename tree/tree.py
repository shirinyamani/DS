import collections
from turtle import right


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


# Question 2
class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = BSTNode(sortedArray[mid])
    
    root.left = minimalTree(sortedArray, start, mid-1)
    root.right = minimalTree(sortedArray, mid+1, end)
    return root 

## OR

def minimalTree1(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) ==1:
        return BSTNode(sortedArray[0])

    mid = int(len(sortedArray/2))

    left = minimalTree1(sortedArray[:mid])
    right = minimalTree1(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid],left,right)


#Question 3
def depth_bfs(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    levels = {}

    while len(queue) > 0:
        node,level = queue.popleft()
        if level not in levels:
            levels[level] = LinkedList()

        #add node to level
        levels[level].add(node)

        #push to the queue
        if node.left:
            queue.append(node.left,level+1)
        if node.right:
            queue.append(node.right,level+1)
    return levels

# Question 4
def isbalancehelper(root): #check hight
    if root is None:
        return 0
    
    leftheight = isbalancehelper(root.left)
    rightheight = isbalancehelper(root.right)

    if leftheight == -1: #bigger than 1 difference
        return -1

    if rightheight == -1:
        return -1

    if abs(leftheight - rightheight) > 1:
        return -1

    return max(leftheight, rightheight) + 1

def isbalance(root):
    return isbalancehelper(root) > -1 

#Question 5
def helperBST(node, min_val=float("-inf"), max_val=float("inf")):
    if not node:
        return True
    val = node.val

    if val <= min_val or val>= max_val:
        return False

    if not helperBST(node.left, min_val,val):
        return False

    if not helperBST(node.right, val, max_val):
        return False

    return True

def is_BST(root):
    return helperBST(root)


#Question 6
def inorderSuccessor(node):
    if node is None:
        return None

    if node.right:
        curr = node.right

    while node.left:
        curr = node.left
        return curr

    ancestor = node.parent
    child = node

    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor

#Question 7
def buildorder(projects, dependencies):
    dependencyTree = {p: set() for p in projects}
    buildorder = []
    independantProjects = set(projects)
    for dependency, project in dependencies:
        dependencyTree[project].add(dependency)

    while independantProjects:
       
        for project in list(independantProjects):
            dependency = dependencyTree[project]
            if not independantProjects.intersection(dependencies):
                buildorder.append(project)
                independantProjects.remove(project)
               
    return buildorder





    

    

if __name__ == "__main__":
        projects = ["a", "b", "c", "d", "e", "f", "g"]
        dependencies = [
            ("d", "g"),
            ("a", "e"),
            ("b", "e"),
            ("c", "a"),
            ("f", "a"),
            ("b", "a"),
            ("f", "c"),
            ("f", "b"),
        ]

        print(buildorder(projects,dependencies))

