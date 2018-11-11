class Solution(object):
    def dfs(self, rooms, node, traverse):
        traverse.append(node)
        for x in rooms[node]:
            if x not in traverse and x != node:
                self.dfs(rooms, x, traverse)
            
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        traverse = []
        self.dfs(rooms, 0, traverse)
        return len(traverse) == len(rooms)