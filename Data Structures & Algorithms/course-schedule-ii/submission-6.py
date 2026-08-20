from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: set() for i in range(numCourses)}
        for take, to_take in prerequisites:
            courses[take].add(to_take)

        # 1. Use a dictionary as a hash map. It maintains insertion order and gives O(1) lookups!
        results = {}
        visited = set()

        def dfs(course: int) -> bool:
            # 2. If it's already in our final schedule, it's safe! Skip it.
            if course in results:
                return True
                
            if course in visited:
                return False

            can_take = True
            visited.add(course)

            for to_take in courses[course]:
                can_take = dfs(to_take)
                if not can_take:
                    break

            visited.remove(course)

            # 3. THE SAFE ZONE: The loop finished and no cycles were found.
            if can_take:
                results[course] = True  # Add to hash map to lock in the order
                courses[course].clear() # Clear prerequisites so it instantly passes future checks

            return can_take

        for course in sorted(courses.keys(), key=lambda x: len(courses[x])):
            can_take = dfs(course)
            if not can_take:
                return []

        # 4. Return just the keys from our hash map as a list!
        return list(results.keys())