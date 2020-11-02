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
            
        