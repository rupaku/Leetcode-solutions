'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
'''

# Solution::::::::::::::::::::::
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        courseDict = defaultdict(list)
        
        for relation in prerequisites:
            nextCourse=relation[0]
            prevCourse=relation[1]
            
            courseDict[prevCourse].append(nextCourse)
            
        path = [False]*numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse,courseDict,path):
                return False
        return True
    
    def isCyclic(self,currCourse,courseDict,path):
        if path[currCourse]:
            return True
        
        path[currCourse] = True
        ret= False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child,courseDict,path)
            if ret:
                break
            
        path[currCourse] = False
        return ret
            
        