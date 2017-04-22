def BreadthFirstSearch(graph, source):
    
    """
    Function BreadthFirstSearch takes arguments graph, a dictionary, and source, an integer. The function will return a dictionary which contains ancestors, descendants, distance from source, and the color of each vertex.
    """
    
    # Dictionary dataInfo will be used to store the information about each vertex. (Ancestors, descendants, distance from source, and color)
    dataInfo = {} 
    
    # List queue will be used to store the vertices currently in the queue, these vertices will all be gray.
    queue = []
    
    # Loops through the vertices in the graph, creates a key in the dictionary for each vertice, with default values.
    for vertex in graph["V"]:
        dataInfo[str(vertex)] = {"ancestor": "", "descendants": [], "distance": "", "color": "white"}
    
    # At key source (variable) in dataInfo dictionary, key ancestor is set to have no value other than "NA" (as it is the starting point), and distance to 0 (as it will always be zero as it is the source).
    dataInfo[str(source)]["ancestor"] = "NA"
    dataInfo[str(source)]["distance"] = 0

    def symmetricVertex(edge, otherVertex):
        
        """
        Function symmetricVertex takes arguments edge, a list of an edge from the graph dictionary, and otherVertex, an integer that is the other vertex in the edge with the sourceVertex. The function will return the point other than the otherVertex, and will be used to find adjacent vertices relative to the current vertex in the queue. Example: edge ([1, 2]), otherVertex (1), the function will return 2.
        """
        
        for num in edge:
            if num != otherVertex:
                return num
            

    def pathFinder(graph, sourceVertex):
        
        """
        Function pathFinder takes arguments graph, a dictionary, with the same keys for the edges and the vertices and sourceVertex, an integer. The function will loop through all of the edges in the graph and find adjacent vertices relative to the current sourceVertex. sourceVertex values will be in the queue. The function will edit dictionaries and lists, not return any value.
        """
        
        # List removeEdges will be used to store the edges that will be removed from the graph dictionary after the loop ends. Makes the code more efficient, as you don't want to loop through a million vertices every time, now do you?
        removeEdges = []
        
        # Loop through edges in the graph, will be used to find adjacent vertices.
        for edge in graph["E"]:
        
        # If the sourceVertex is in the edge and the edge is not discovered yet, then edit and change values in the main dictionary, dataInfo.
            if (sourceVertex in edge) and (dataInfo[str(symmetricVertex(edge, sourceVertex))] != "gray"):
                otherVertex = symmetricVertex(edge, sourceVertex)
        
                # Adds variable otherVertex to the descendants of the sourceVertex.
                dataInfo[str(sourceVertex)]["descendants"].append(otherVertex)
                
                # Updates key(otherVertex) to correct values. Ancestor is always the sourceVertex, the distance is always the distance of sourceVertex incremented                    by one, and the color is updated to gray as it is added to the queue.
                dataInfo[str(otherVertex)] = {"ancestor": sourceVertex, "descendants": [], "distance": (dataInfo[str(sourceVertex)]["distance"] + 1), "color": "gray"}
                
                # Edge includes two discovered edges, so it will be removed to stop redundancy. It is added to the removeEdges list.
                removeEdges.append(edge)
                
                # Appends the discovered vertex to the queue.
                queue.append(otherVertex)
        
        # After the loop ends, the edges that contain the source vertex have been exhausted, so the color is updated to black.
        dataInfo[str(sourceVertex)]["color"] = "black"    
        
        # If the sourceVertex is in the queue, it is removed, as all of the edges containing it have been exhausted.
        if sourceVertex in queue:
            queue.remove(sourceVertex)
        
        # Loop through the edges in the removeEdges list, each edge will be removed.
        for edge in removeEdges:
            graph["E"].remove(edge)
            
    # The function pathFinder is called on the graph and the source vertex, which sets up the queue.
    pathFinder(graph, source)
    
    # While the list queue contains values, the pathFinder function is called on the graph, and the queue value at index 0.
    while len(queue) != 0:
        pathFinder(graph, queue[0])
    
    # Loop below is for formatting of the data, makes it easier to read.
    for key in dataInfo:
        print "Vertex: " + key + ", Distance: " + str(dataInfo[key]["distance"]) + ", Ancestor: " + str(dataInfo[key]["ancestor"]) + ", Descendants: " + str(dataInfo[key]["descendants"]) + ", Color: " + str(dataInfo[key]["color"]) + "."    
    
    # Returns dictionary dataInfo.
    return dataInfo



BreadthFirstSearch({"E": [[1, 7], [1, 3], [3, 4], [4, 5], [4, 2], [4, 8]], "V": [1, 2, 3, 4, 5, 6, 7, 8]}, 4)
#Input is the graph dictionary with keys "E" that holds a list of edges. "V" holds a list of all of the vertices and the source vertex which is an integer.