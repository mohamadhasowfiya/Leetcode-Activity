class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph={i:[]for i in range (numCourses)}
        indegree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue=deque()
        for i in range (numCourses):
            if indegree[i]==0:
                queue.append(i)
        count =0
        while queue:
            node=queue.popleft()
            count+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return count == numCourses
