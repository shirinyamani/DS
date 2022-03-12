# Tree  🌳🌲🌵🌴

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

    - **Search:** The methodology is pretty simple! ya start by the root, compare the target value with the root value, if the target value is less than the root value, then we go to the left node, if the target value is greater than the root value, then we go to the right node.
    - **Delete:** 
        - If the node we wanna delete is a leaf node, then we can just delete straightaway!
        - If the node we wanna delete has only one child, then we can just delete it and replace it with the child.
        - If the node we wanna delete has 2 children, then we need to find the deepest node in the left subtree and swap the value with the node we wanna delete.**(i.e. Succesor; the smallest node in the right subtree)**
        - If the node we wanna delete has 2 children, then we need to find the deepest node in the right subtree and swap the value with the node we wanna delete.

# AVL Tree
- **AVL Tree** is a type of **Binary Search Tree** that is balanced.
- Why we need it ? look at the img below;

<img src="./img/avl.png">

So, how can we balance the tree? We can get rid of the unbalanced nodes by doing some **rotations**!
But how do we know which tree needs to be rotated? We can use the **height** of the tree!
The idea is pretty simple; if the difference between the height of left subtree and the right subtree is greater than 1, then we need to rotate the tree.
## Balanced AVL
<img src="./img/balanceavl.png">

## Dis-balanced AVL
<img src="./img/disavl.png">

We can solve such a problem by doing some **Rotations**!

## Insertion in AVL

First we need to figure whether we need to rotate the tree or not.

- **Case1:** Rotation is not required:
When the tree is balanced, then we dont need to rotate the tree(i.e. difference height subtrees equal to 1). So we treat it same as BST; 
    - 1.Compare w/ the root to go right/left!
    - 2.Insert at the first empty spot! 

- **Case2:** Rotation is required: 
When the tree is unbalanced, then Rotation is required!
<img src="./img/rotateavl.png">

- **Left left condition:**
    - 1. Rotate right
    - 2. Update the height of the tree
- **Right right condition:**
    - 1. Rotate left
    - 2. Update the height of the tree
- **Left right condition:**
    - 1. Rotate left the child of the root then rotate right the root
    - 2. Update the height of the tree
- **Right left condition:**
    - 1. Rotate right
    - 2. Update the height of the tree

### What does left left condition mean?
So imagine in the following img, we wanna insert a node with value of 10. 
- We start by comparing from the root node, if the value of the root node is greater than 10, then we go to the left subtree, if the value of the root node is less than 10, then we go to the right subtree.
- Once we find the right place to insert the node, then we insert it!
- Now we start with the node we just inserted, all the way up to the root node, we need to check if the height of the subtrees are balanced or not. To find the node that is causing the unbalance. then we need to find the condition (node 30 in our case)
<img src="./img/disnode.png">
    - If the height of the subtrees are balanced, then we dont need to rotate the tree.
    - If the height of the subtrees are not balanced, then we need to rotate the tree. 
Once we find the unbalanced node, then we go and check which subtree is causing the unbalance.)
    - If the left subtree is causing the unbalance, then we need to rotate the tree to the right. (20-10 our case)
        - **right rotation:** 
            - Root node comes down then the left subtree comes up.
            <img src="./img/rightrot.png">
    - If the right subtree is causing the unbalance, then we need to rotate the tree to the left.

## Summary of Left Left Condition Rotation:
- Find the unbalanced node, then find the condition
- Find the condition of the unbalanced node 
- Find the grand child of this unbalanced node + the path to its grand child node
- Once found,then how to know which child to select?
    - the one that has more height!
- Once found, then Rotate Right!

<img src="./img/rotavlbefore.png" width=300>
<img src="./img/rotavlafter.png" width=300>
<img src="./img/fullrot.png" >

## Left Right Condition
- Find the disbalanced node
- Find the Condition, How? next bullet! 😁
- Find the grand child of the node + the path to the grand child node!
- Once found, then first, rotate the left child of the disballenced node to left(i.e. move the right child of the parent to parent place)
<img src="./img/lrrot.png">

## Right Right Condition
- Find the disbalanced node( move upward and compare the difference in height)
- Find the Condition, **How?** next bullet! 😁
- Find the grand child of the node + the path to the grand child node!
- Once found,rotate to left!

<img src="./img/rrrot.png">

## Right Left Condition

<img src="./img/1.png" width=250><img src="./img/2.png" width=250><img src="./img/3.png" width=280><img src="./img/4.png" width=280>