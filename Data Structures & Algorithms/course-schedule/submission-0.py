class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            courses[a].append(b)

        took_course = True
        while took_course:
            took_course = False

            for course in courses.values():
                if not len(course):
                    continue
                else:
                    # Loop backwards so deleting items doesn't break our index positions
                    for i in range(len(course) - 1, -1, -1):
                        can_take = not len(courses[course[i]])
                        if can_take:
                            del course[i]
                            took_course = True

        # Check courses.values() so we look at the lists, not the integer keys
        return all([not len(course) for course in courses.values()])