class Solution(object):
    def matrixBlockSum(self, mat, k):
        
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

    
        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
            
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                R1, C1 = r1 + 1, c1 + 1
                R2, C2 = r2 + 1, c2 + 1

                answer[i][j] = (
                    prefix[R2][C2]
                    - prefix[R1 - 1][C2]
                    - prefix[R2][C1 - 1]
                    + prefix[R1 - 1][C1 - 1]
                )

        return answer
        