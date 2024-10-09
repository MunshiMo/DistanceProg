import sys
import pandas as pd
from pandas import read_csv
from queue import PriorityQueue
#from nodeC import Node

#df = pd.read_csv('driving.csv')

drivingDF=read_csv('driving.csv', index_col=0)


#reset datafram so that the first column can hold the state values rather than just the indexes 
#might make it easier to search with specific state names in the rows

#drivingDF = driving.set_index('STATE')

straightLineDF = read_csv('straightline.csv', index_col=0)
#straightLineDF = straightLine.set_index('STATE')




numberOfArgumentsPassedFromCommandLine = len(sys.argv)
print("Number of arguments passed (including your script name):", numberOfArgumentsPassedFromCommandLine)


firstArgument = sys.argv[0]
print("\nScript name:", sys.argv[0])

print("Munshi, Mohammed, A20468727 solution:")
startStateArg = sys.argv[1] #initial state
print("\nINITIAL state:", startStateArg)

goalStateArg = sys.argv[2] #goal state
print("\nGOAL state:",  goalStateArg)
    
#children = []   
#ch = []

    
def expandNode(node, goalState):
    try:
        ch = []
        for x in drivingDF.columns[1:] : #range(len(drivingDF)):
            if( drivingDF.loc[x,node] > 0 ):
                ch.append(x)
        f = ch[0]
        for x in ch:
            if(getHeuristic(x,goalState) < getHeuristic(f,goalState)):
                f = x
        return f          
             
    except:
        if len(ch) == 0:
            print("Failure: Node doesnt exist")
            
            
def expandNodeASTAR(node, goalState,pathCostA):
    try:
        childrenA = []
        for x in drivingDF.columns[1:] : #range(len(drivingDF)):
            if( drivingDF.loc[x,node] > 0 ):
                childrenA.append(x)
        z = childrenA[0]
        for x in childrenA:
            if((getEdgeCost(x,node) + getHeuristic(x,goalState)+ pathCostA) < ( getEdgeCost(z,node) + getHeuristic(z,goalState) + pathCostA)):
                z = x
        return z          
             
    except:
        if len(childrenA) == 0:
            print("Failure: Node doesnt exist")
    
    
        
    
def getEdgeCost(startState, endState):
    eCost = 0
        #for x in drivingDF : #range(len(drivingDF)):
    try:
        #if startState == endState:
           # return 0
        #if endState in drivingDF:
            #print(drivingDF[startState,endState])
        if (drivingDF.loc[startState,endState]) > 0:    
            eCost = drivingDF.loc[startState,endState]
       # print(eCost)
            return eCost
        else:
            print("Not a usable node edge neighbor")
            return eCost
    except:  
        if endState not in drivingDF:
            print("Not a usable Node edgge")
            return 0      
    
def getHeuristic(nextState, goalState):
    eHeur = 1
    try:
       # if nextState == goalState:
            #return 0
        for x in drivingDF:
            if x == goalState:
                t = True
                
        if t: #goalState in drivingDF :
            eHeur = straightLineDF.loc[nextState,goalState]
            #print(eHeur)
        return eHeur
        
    except:
        if goalState not in drivingDF:
            print("Not a usable Node heur")
            return 0


    
def GBFSSearch(startState, goalState):
        
    frontier = PriorityQueue() #prioritize with lowest heuristic
    pathCost = 0
    solutionPath = []
    reached = []
    expandedCount = 0
 
    dummyDict = {}
    statPathCount = 0
    reached.append(startState)
    # reached[startState] = getHeuristic(startState,goalState) #the inital state is technically already reached so its first
    #print(reached)
    solutionPath.append(startState)    
    statPathCount += 1
    frontier.put((0,startState)) #first node to go in is the initial start node
     
    while  not frontier.empty():
        getNode = frontier.get()
        temp = getNode[1]
        dummyDict[temp] = 0
        #child = []
        child = expandNode(temp,goalState)
        expandedCount += 1 #+= len(childrenG)
        
        #for child in childrenG:
        if temp == goalState:
            print("Goal has been reached")
            print("GBFS:\n")
            print("Solution path: " , solutionPath )
            print("Number of states on path: " , statPathCount )
            print("No. expanded nodes: " , expandedCount )
            print("pathCost: " , pathCost)
            print(reached)
            print('\n')
            return temp, pathCost, solutionPath,expandedCount            
            
            
        
        tmpC = child
      
        if len(dummyDict)>1:
            dummyDict[tmpC] = getHeuristic(tmpC,goalState)
        cHeur = getHeuristic(child,goalState)    
        if tmpC not in reached or (cHeur < dummyDict[tmpC]): #getHeuristic(reached[holder],goalState)): 
                #reached[tmpC] = getHeuristic(child,goalState)
            num = getHeuristic(tmpC,goalState)
            dummyDict[tmpC] = num
            reached.append(tmpC)
            frontier.put((getHeuristic(child,goalState),child))
            pathCost += getEdgeCost(temp, tmpC)
            solutionPath.append(tmpC)
            statPathCount += 1
            temp = child
           
    return None
                    
        

    
def AstarSearch(start, goal): #cost of next state distance to goal state + heuristic
        
    frontierA = PriorityQueue() #prioritize with lowest heuristic
    pathCostA = 0
    solutionPathA = []
    reachedA = []
    expandedCountA = 0

    dummyDictA = {}
    statPathCountA = 0
    reachedA.append(start)
    # reached[startState] = getHeuristic(startState,goalState) #the inital state is technically already reached so its first
    #print(reached)
    solutionPathA.append(start)    
    statPathCountA += 1
    frontierA.put((0,start)) #first node to go in is the initial start node
    dummyDictA[start] = 0 
    
    
    
    while  not frontierA.empty():
        getNodeA = frontierA.get()
        tempA = getNodeA[1]
        
        
        #child = []
        
        expandedCountA += 1 #+= len(childrenG)
        
        #for child in childrenG:
        if tempA == goal:
            print("Goal has been reached")
            print("ASTAR:\n")
            print("Solution path: " , solutionPathA)
            print("Number of states on path: " , statPathCountA )
            print("No. expanded nodes: " , expandedCountA )
            print("pathCost: " , pathCostA)
            print(reachedA)
            print('\n')
            return tempA, pathCostA, solutionPathA,expandedCountA            
            
            
        childC = expandNodeASTAR(tempA,goal,pathCostA)
        tmpCA = childC
    
       
        #if len(dummyDictA)>1:
           # dummyDictA[tmpCA] = getHeuristic(tmpCA,goal) + getEdgeCost(tmpCA,tempA) + pathCostA
                   
        cHeurA = getHeuristic(childC,goal) + getEdgeCost(childC,tempA) + pathCostA   
        if tmpCA not in reachedA or (cHeurA < dummyDictA[tmpCA]): #getHeuristic(reached[holder],goalState)): 
                #reached[tmpC] = getHeuristic(child,goalState)
            dummyDictA[tmpCA] = getHeuristic(tmpCA,goal) + getEdgeCost(tmpCA, tempA) + pathCostA

            reachedA.append(tmpCA)
            frontierA.put((getHeuristic(childC,goal),childC))
            pathCostA += getEdgeCost(tempA, childC)
            solutionPathA.append(tmpCA)
            statPathCountA += 1
            tempA = childC
           
    return None
    
    

    
#expandNode('OR')
#getEdgeCost('IL', 'IA')

#getHeuristic('WA','IL')
#GBFSSearch('OR','NY')
#expandNodeASTAR('CA','OR')
#expandNodeASTAR('OR','NY')
#expandNodeASTAR('WA','NY')


#AstarSearch('OR','NY')

#Node('IL', None, driving,straightLine, 'GBFS')


# Run both GBFS and A* searches
print("\nRunning Greedy Best-First Search (GBFS)...")
GBFSSearch(startStateArg, goalStateArg)

print("\nRunning A* Search...")
AstarSearch(startStateArg, goalStateArg)