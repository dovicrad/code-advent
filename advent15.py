caveMatrix = [
    [1,1,6,3,7,5,1,7,4,2],
    [1,3,8,1,3,7,3,6,7,2],
    [2,1,3,6,5,1,1,3,2,8],
    [3,6,9,4,9,3,1,5,6,9],
    [7,4,6,3,4,1,7,1,1,1],
    [1,3,1,9,1,2,8,1,3,7],
    [1,3,5,9,9,1,2,4,2,1],
    [3,1,2,5,4,2,1,6,3,9],
    [1,2,9,3,1,3,8,5,2,1],
    [2,3,1,1,9,4,4,5,8,1]
]

class Vertex:
    def __init__(self,value,x,y):
        self.x = x
        self.y = y
        self.value = value
        self.minDistance = float('inf')
        self.previousVertex = None

class Dijkstra:
    def __init__(self):
        self.vertexMatrix = []

    def createGraph(self, matrix):
        for row in range(0,len(matrix)):
            self.vertexMatrix.append([])
            for chiton in range(0,len(matrix[row])):
                self.vertexMatrix[row].append(Vertex(matrix[row][chiton],chiton,row))
                
    def getNextVertex(self, vertex):
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        for dir in directions:
            newX = vertex.x + dir[0]
            newY = vertex.y + dir[1]
            if newX >= 0 and newY >=0 and newX < len(self.vertexMatrix[0]) and newY < len(self.vertexMatrix):
                newVertex = self.vertexMatrix[newY][newX]
                if newVertex.minDistance > vertex.minDistance+newVertex.value:
                    return newVertex
        return None

    def getPath(self):
        start = self.vertexMatrix[0][0]
        start.minDistance = 0
        complete = False
        while not complete:
            new = self.getNextVertex(start)
            if(new == None):
                complete = True
            else:
                self.makeStep(start, new)

        finished = False
        last = self.vertexMatrix[len(self.vertexMatrix[0])-1][len(self.vertexMatrix)-1]
        print("res:"+str(last.minDistance))
        resultPath = []
        while not finished:
            resultPath.append(last)
            last = last.previousVertex
            if last == None:
                finished = True

        for row in range(len(self.vertexMatrix)):
            for col in self.vertexMatrix[row]:
                if col in resultPath:
                    print(col.value, end="")
                else:
                    print(" ",end="")
            print()
        

    def makeStep(self, prev, current):
        current.minDistance = prev.minDistance + current.value
        current.previousVertex = prev
        complete = False
        while not complete:
            new = self.getNextVertex(current)
            if(new == None):
                complete = True
            else:
                self.makeStep(current, new)
        
dijkstra = Dijkstra()
dijkstra.createGraph(caveMatrix)
dijkstra.getPath()