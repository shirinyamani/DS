# Tree  🌱 

- ## Binary Tree

    <img src= "./img/bt.png" >

    - Each node has at most 2 children, could be one but no more than 2
    - Binary Search Tree used for it!

    **Type of BT**

    - **Full BT** ---> each node has either Zero or 2 children!
    <img src= "./img/full.png" >

    - **Perfect BT** ----> each node has 2 children + same level
    <img src= "./img/perfect.png" >

    - **Complete BT** ----> all level has filled except the last level!
    <img src= "./img/complete.png" >

    - **Balanced BT** ----> all leafs are at the same distance from root
    <img src= "./img/balanced.png" >

    ## Operations on Tree
    - Insert a node
    - Delete a Node 
    - Search for a value
    - Traverse all nodes
    - Deletion of a tree

    ## Traversal within a Tree
    
    - **DFS**
        - InOrder
        - PreOrder
        - PostOrder
    - **BFS**
        - LevelOrder
    
## Pre-order Traversal

<img src="./img/preorder.png">

**Root Node ----> Left SubTree ----> Right Subtree**

- the last node that we visit is almost always is the right ending leaf node.

## In-order Traversal

<img src="./img/inorder.png">

**Left SubTree ----> Root Node ----> Right Subtree**

- the last node that we visit is almost always is the right ending leaf node.

## Post-order Traversal

<img src="./img/postorder.png">

**Left SubTree ----> Right SubTree ----> Root Node**

- the last node that we visit is almost always is the root node.

## Level-order Traversal

- **Level-order Traversal Usage**
    - Search for a Value
    - Insert a Node
    - Delete a Node

<img src="./img/levelorder.png">

**Level1 ----> level2 ----> ...**

- In each level, we start from the leftmost node and end at the rightmost node.
- **Search:** When we wanna search for a node in a tree, we usually use **level-order traversal** cuz it uses Queue not like the others that uses Stack! 

- **Insert:** When ya wanna insert a node, we usually use **level-order traversal**. So now the question is **HOW** to find a place to add the node? The answer is pretty simple! the place will be the very first empty option we see! In other words, we go in each level, check whether its node has 2 children, if yes, then it is not possible to add the node there, then we go to the next node check whether it has one child, if yes, then it is not possible to add the node there, then we go to the next node and so on.

<img src= "./img/insert.png">

- **Delete:** We usually use **Level-Order Traversal** We have 2 Scenarios:
    - 1. The node.value we wanna delete does not exist in the tree! --> return false
    - 2. The node we wanna delete exists in the tree! If yes, then we need to do some stuff:
            - Find the deepest node in the tree.
            - Swap the value of the node we wanna delete with the deepest node.
            - Delete the deepest node.
            - You ask **why? why not deleting the node itself?** This is bc in a tree, the next nodes rely on the prev node! So we cant really delete it as if we do so, then in breaks the connections! So we need to swap the value of the node we wanna delete with the deepest node, and then delete the deepest node.


## Binary Search Tree
- left nodes are less than the root + right node!
    - **Delete:** 
        - If the node we wanna delete is a leaf node, then we can just delete it.
        - If the node we wanna delete has only one child, then we can just delete it and replace it with the child.
        - If the node we wanna delete has 2 children, then we need to find the deepest node in the left subtree and swap the value with the node we wanna delete.**(i.e. Succesor; the smallest node in the right subtree)**
        - If the node we wanna delete has 2 children, then we need to find the deepest node in the right subtree and swap the value with the node we wanna delete.