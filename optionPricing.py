import numpy as np
sZero = 100
u = 0.1
d = -0.1
r = 0.05
n = 6
k = 95
stockPrices = np.zeros((n,n))
callPrices = np.zeros((n,n))
stockPrices[0,0] = sZero
earlyExcersize = []
#first find the prices of the asset
#this is keeping track of time

#row echellon
def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])


for i in range(1,n):
    stockPrices[i,0] = stockPrices[i-1,0] * (1 + u)
    for j in range(1, i + 1):
        stockPrices[i,j] = stockPrices[i-1,j-1] * (1 + d)
# print(stockPrices)
#options
#first calculate expiration prices
for i in range(0,n):
    callPrices[n - 1,i] = max(stockPrices[n-1,i] - k, 0)
#go backwards
A = [0] * n
A[0] = 1 + r
A[1] = 1 + r
for i in range(2,len(A)):
    A[i] = A[0] * (1+r)^i

pStar = (r - d) / (u - d)
for i in range(n - 2, -1, -1):
    tempArr = []
    for j in range(i + 1):
        callPrices[i,j] = ((callPrices[i + 1, j]/(1 + r) * pStar) + (callPrices[i + 1, j + 1]/(1 + r) * (1- pStar)))
        if callPrices[i,j] < max(stockPrices[i,j] - k,0):
            earlyExcersize.append([i,j])
        
        tempArr.append()

 
# print(callPrices)

print("Part A Answer: ", callPrices[0,0])
print(stockPrices)
if len(earlyExcersize) == 0:
    print("Part C Answer: There are no early executions")
else:
    print("Part C Answer: Early excersizes at")
    for i in earlyExcersize:
        print(i[0],i[1])
