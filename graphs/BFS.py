#===============================================================================
# implementation for Breadth First Search in graphs
#===============================================================================
from numpy.core.multiarray import empty

#===============================================================================
# Performs a breadth-first search on a graph
# @param {array} graph - Graph, represented as adjacency lists.
# @param {number} source - The index of the source vertex.
# @returns {array} Array of objects describing each vertex, like
# ({distance: _, predecessor: _ })
#===============================================================================
import Queue

def doBFS(graph, source):
    bfsInfo = [];
    for i in range(len(graph)):
        tempDict = ({"distance": None, "predecessor": None});
        bfsInfo.append(tempDict)
    bfsInfo[source]["distance"] = 0
    queue = Queue.Queue()
    queue.put(source)
    
    #===========================================================================
    # Traverse the graph
    # 
    # As long as the queue is not empty:
    # Repeatedly dequeue a vertex u from the queue.
    #   
    # For each neighbor v of u that has not been visited:
    # Set distance to 1 greater than u's distance
    # Set predecessor to u
    # Enqueue v
    #===========================================================================
    
    while(not queue.empty()):
        u = queue.get()
        for i in range(len(graph[u])):
            v = graph[u][i]
            if(bfsInfo[v]["distance"] == None):
                bfsInfo[v]["distance"] = bfsInfo[u]["distance"] + 1
                bfsInfo[v]["predecessor"] = u
                queue.put(v)
        
    
    return bfsInfo
    
    
def main():
    adjList = [[1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
    ];
    bfsInfo = doBFS(adjList, 3);
    for i in range(len(adjList)):
         print "vertex %d: distance =  %s , predecessor = %s" % (i, bfsInfo[i].get("distance"), bfsInfo[i].get("predecessor"))

if __name__ == '__main__':
    main()
