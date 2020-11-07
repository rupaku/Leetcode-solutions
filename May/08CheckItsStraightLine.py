'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
'''
# Solution::::::::::::::::::::::
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope=self.get_slope(coordinates[0],coordinates[1])
        for i in range(2,len(coordinates)):
            m=self.get_slope(coordinates[i],coordinates[0])
            if m != slope:
                return False
        return True
        
    def get_slope(self,p1:List[int],p2:List[int]):
        if p1[0] == p2[0]:
            return 100000
        return (p2[1]-p1[1])/(p2[0]-p1[0])
        