for ts in range(int(input())):
    n,m,k = map(int, input().split())
    farm = [[0 for i in range(m)] for j in range(n)]
    for iter_on_plants in range(k):
        r,c = map(int, input().split())
        farm[r-1][c-1] = 1
    fence_len = 0
    for row in range(n):
        for col in range(m):
            no_of_adj_cells = 0
            if(farm[row][col]):
                # top
                if (row - 1 >=0 and farm[row-1][col]):
                    no_of_adj_cells = no_of_adj_cells + 1
                # bottom
                if (row + 1 <=n-1 and farm[row+1][col]):
                    no_of_adj_cells = no_of_adj_cells + 1
                # left
                if (col - 1 >=0 and farm[row][col-1]):
                    no_of_adj_cells = no_of_adj_cells + 1
                # right
                if (col + 1 <=m-1 and farm[row][col+1]):
                    no_of_adj_cells = no_of_adj_cells + 1
                fence_len = fence_len + (4 - no_of_adj_cells)
    print(fence_len)