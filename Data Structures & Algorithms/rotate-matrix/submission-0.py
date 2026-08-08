class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r

                topLeft = matrix[t][l+i]

                # bottom left to top left
                matrix[t][l+i] = matrix[b-i][l]

                # bottom right to bottom left
                matrix[b-i][l] = matrix[b][r-i]

                # top right to bottom right
                matrix[b][r-i] = matrix[t+i][r]

                # top left to top right
                matrix[t+i][r] = topLeft

            r -= 1
            l += 1