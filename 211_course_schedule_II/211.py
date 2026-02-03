class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        viewed = set()
        safe = set()
        output = []

        def _dfs(crs):
            if crs in viewed:
                return False
            if crs in safe:
                return True
            viewed.add(crs)
            for pre in pre_map[crs]:
                if not _dfs(pre):
                    return False
            viewed.remove(crs)
            safe.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if not _dfs(crs):
                return []
        return output