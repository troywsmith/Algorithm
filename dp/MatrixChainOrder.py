# # Recursion
# def MatrixChainOrder(p, i, j):
#     if i == j:
#         return 0

#     count = 10**10
#     for k in range(i, j):
#         currCount = MatrixChainOrder(
#             p, i, k) + MatrixChainOrder(p, k+1, j) + p[i-1]*p[k]*p[j]
#         count = min(count, currCount)

#     return count


# Dynamic Programming
def MatrixChainOrder(p, n):

    m = [[0 for x in range(n)] for x in range(n)]

    for L in range(2, n):
        for i in range(1, n-L+1):

            j = i+L-1
            m[i][j] = 10**10

            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                m[i][j] = min(m[i][j], q)

    return m[1][n-1]


# Driver program to test above function
arr = [1, 2, 3, 4]
n = len(arr)
print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, n)))
