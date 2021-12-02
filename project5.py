"""
Math 560
Project 5
Fall 2021

Partner 1: Casper Hsiao ph139
Partner 2: Leon Zhang lz198
Date: Nov 30 2021
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
Input:
- adjList: The adjacency list for the graph
- adjMat: The adjacency matrix for the graph
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    start = adjList[0]
    start.cost = 0
    # Put all the vertices into a priority queue
    # Visit the vertices in the order of their cost
    pq = PriorityQueue(adjList)

    while not pq.isEmpty():
        # Remove the vertex from the queue once we visited it
        v = pq.deleteMin()
        v.visited = True

        for neigh in v.neigh:
            # Update the cost of vertex if not visited (become part of the MST yet)
            if not neigh.visited:
                if neigh.cost > adjMat[v.rank][neigh.rank]:
                    neigh.cost = adjMat[v.rank][neigh.rank]
                    neigh.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    # Initialize by building singleton sets of each vertices
    for v in adjList:
        makeset(v)
    X = []
    for e in edgeList:
        u, v = e.vertices
        # If the minimum edge crosses a cut between two disjoint sets, add it to our MST
        if not find(u).isEqual(find(v)):
            X.append(e)
            union(u, v)

    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v
    height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    if v != v.pi:
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    ru = find(u)
    rv = find(v)
    if ru == rv:
        return
    if ru.height > rv.height:
        rv.pi = ru
    elif rv.height > ru.height:
        ru.pi = rv
    else:
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP
Input:
- adjList: The adjacency list of the graph
- start: The vertex to start the tour with

Ouput:
- tour: The sequence of vertex to visit for the tsp
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    # Initialize the visited field in the vertex as False
    for v in adjList:
        v.visited = False
    tour = []
    # We use pre-order DFS to traverse the MST tree with stack
    stack = []
    # We start by visiting the start vertex
    stack.append(start)
    while stack:
        curr = stack.pop(-1)
        # Only visit a vertex once to satisfy TSP requirement
        if not curr.visited:
            curr.visited = True
            # Append the visited vertex to tour
            tour.append(curr.rank)
            for neigh in curr.mstN:
                stack.append(neigh)
    # Append the start vertex to tour to complete the cycle
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
