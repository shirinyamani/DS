import collections
from logging import root
from DS_implementation import LinkedList


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
def is_balancehelper(root): #check hight
    if root is None:
        return 0
    
    leftheight = is_balancehelper(root.left)
    rightheight = is_balancehelper(root.right)

    if leftheight == -1: #bigger than 1 difference
        return -1

    if rightheight == -1:
        return -1

    if abs(leftheight - rightheight) > 1:
        return -1

    return max(leftheight, rightheight) + 1

def is_balance(root):
    return is_balancehelper(root) > -1 

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

    if node.right: #for the parent sample to know to get to right (inorder)
        curr = node.right

    while node.left: #if get to right n the node has left n right child, we need to get to the left one

        curr = node.left
        return curr

    ancestor = node.parent # if already on right node n wanna jump to very first root!
    child = node

    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor

#Question 7
def buildorder(projects, dependencies):
    #Step1: Build dependency Tree 
    dependencyTree = {p: set() for p in projects} #build initial tree
    buildorder = []
    independentProjects = set(projects) 
    for dependency, project in dependencies:
        dependencyTree[project].add(dependency) #add projects n their dependencies

    #Step2: Check the dependant Projects!
    while independentProjects:
       
        for project in list(independentProjects):
            dependency = dependencyTree[project] #define dependency
            if not independentProjects.intersection(dependencies): 
                buildorder.append(project)
                independentProjects.remove(project)
               
    return buildorder


#Question 9
def BST_seq(root):
    if not root:
        return None
    return helper(root)

def helper(root):
    right_tree = helper(root.right) #Step1: for each of the SubTrees
    left_tree = helper(root.left)
    sequences = [] #to store the arrays
    for right in right_tree: 
        for left in left_tree:
            sequences = weave(left, right, [root.key], sequences)
    return sequences
# weave({1,2}, {3,4},{})--> weave({2}, {3,4}, {1}) --> weave({},{3,4},{1,2})--> (1,2,3,4)
def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        results = prefix.copy()
        results.extend(first)
        results.extend(second)
        results.append(results)
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()

    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()

    return results

#Question 10
def isMatch(s,t):
    if not s and not t:
        return False
    if s.val == t.val: #if the values are equal then check whether the trees are identical
        return isMatch(s.left, t.left) and isMatch(s.right, t.right)

def isSubtree(s,t):
    if s is None or t is None:
        return False

    if isMatch(s,t): #if the comparison win 
        return True
    # S is the bigger tree
    return isSubtree(s.left, t) or isSubtree(s.right, t)

#Question11
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.size = 1

    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0

    @property
    def right_size(self):
        if self.right:
            return self.right.size
        return 0

class BST:
    def __init__(self):
        self.root = root

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        cur_node = self.root
        while cur_node:
            cur_node.size +=1
            if cur_node.value >= value:
                if cur_node.left is None:
                    cur_node.left = new_node
                    new_node.parent = cur_node
                    return
                cur_node = cur_node.left

            else:
                if cur_node.right is None:
                    cur_node.right = new_node
                    new_node.parent = cur_node
                    return
                cur_node = cur_node.right

    def delete_helper(self, node, value):
        if node is None:
            return node
        
        if node.value < value:
            node.left = self.delete_helper(node.left, value)

        elif node.value > value:
            node.right = self.delete_helper(node.right, value)

        else:
            if node.left is None:
                temp, node = node.right, None
                return temp

            elif node.right is None:
                temp, node = node.left, None
                return temp

            temp = min_val_node(node.right)
            node.value = temp.value
            node.right = self.delete_helper(node.right, temp.value)

    def delete(self, value):
        self.delete_helper(self.root, value)

def min_val_node(node):
    current = node
    while current.left is not None:
        #go deep in the tree to find leftmost leaf
        current = current.left
    return current






















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

