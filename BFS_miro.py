from collections import deque

# n,m 및 미로 입력
n, m = map(int,input().split())
miro = [list(map(int,list(input().strip()))) for _ in range(n)]

# 이동 방향 : 좌, 우, 하, 상
dir_x = [-1, 1, 0, 0]
dir_y = [0, 0, -1, 1]

# BFS
def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(0,4):
            move_x = x + dir_x[i]
            move_y = y + dir_y[i]

            #미로 밖으로 나가는 경우
            if move_x < 0 or move_y < 0 or move_x >= n or move_y >= m:
                continue

            #벽 or 중복된 곳은 무시
            if miro[move_x][move_y] == 0:
                continue

            if miro[move_x][move_y] == 1:
                miro[move_x][move_y] = miro[x][y] + 1
                queue.append((move_x,move_y))

    return miro[n-1][m-1]

#정답
print(BFS(n,m))
