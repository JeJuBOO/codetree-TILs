import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(N,M)
print(board)

# 일단 작은 문제로 생각 오른쪽, 대각아래, 아래가 1이면 정사각형, 그리고 오른쪽,대각아래,아래에서 또 오른쪽,대각아래,아래가가 1이면 9
queue = deque()
max_size = 1
for i in range(N):
    for j in range(M):
        queue.append((i,j))
        size_ = 0
        while queue:
            x,y = queue.pop()
            size_ += 1
            if int(size_**(1/2)) == size_**(1/2):
                max_size = max(max_size,size_)
            if x >= N-1 or y >= M-1:
                break
            if board[x+1][y] == 1 and board[x+1][y+1] == 1 and board[x][y+1] == 1:
                queue.append((x+1,y))
                queue.append((x+1,y+1))
                queue.append((x,y+1))