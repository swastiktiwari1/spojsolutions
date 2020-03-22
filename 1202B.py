def floyd_warshall(cost):
    n = len(cost)
    dist = cost[::]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
 
def insert_matrix(x, y):
    cost = [[0 for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(10):
            if (i+x)%10 == j or (i+y)%10 == j:
                cost[i][j] = 1
            else:
                cost[i][j] = 100 # Big number to show that edge does not exist
    dist = floyd_warshall(cost)
    for i in range(10):
        for j in range(10):
            if dist[i][j] >= 100:
                dist[i][j] = -1
            else:
                dist[i][j] -= 1
    return dist
 
def solve_one(x, y, transitions):
    mat = insert_matrix(x,y)
    result = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j]*transitions[i][j]<0:
                return -1
            result += mat[i][j]*transitions[i][j]
    return result
 
def solve(S):
    transitions = [[0 for i in range(10)] for j in range(10)]
    for i in range(1, len(S)):
        transitions[int(S[i-1])][int(S[i])] += 1
    
    result = [[0 for i in range(10)] for j in range(10)]
    for x in range(10):
        for y in range(10):
            result[x][y] = solve_one(x, y, transitions)
        
    return result
 
result = solve(input())
for x in range(10):
    for y in range(10):
        print(result[x][y], end=" ")
    print()