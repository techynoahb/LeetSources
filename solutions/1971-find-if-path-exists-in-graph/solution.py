from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list) # 1. create adj list, u maps to v, v maps t u
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source]) #create a deque starting from the start vertex
        visited = {source}  #create a visited set starting with the start vertex since we are already there

        while q: #while the q is occupied
            node = q.popleft() #set node equal to the queue'd item
            if node == destination: # if node is our target vertex then return true
                return True
            for neighbor in graph[node]: # for all nodes neighboring vertex's
                if neighbor not in visited: # if nodes neighbor isnt in the visited vertex, add it and append it to the q
                    visited.add(neighbor)
                    q.append(neighbor)

        return False # at the end, return false assuming node doesnt = destination through the loop
