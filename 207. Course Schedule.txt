class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        listofedges = [x for x in range(numCourses)]
        lnoIncoming = listofedges[:]
        for x in prerequisites:
            a,b = x
            if a in lnoIncoming: lnoIncoming.remove(a)
        def noIncoming(node, prerequisites):
            for x in prerequisites:
                if node == x[0]:
                    return False
            return True
        for x in lnoIncoming:
            l = []
            for y in prerequisites:
                a,b = y
                if b == x:
                    l.append(y)
            for z in l:
                prerequisites.remove(z)
                if noIncoming(z[0], prerequisites):
                    lnoIncoming.append(z[0])
        if prerequisites:
            return False
        return True