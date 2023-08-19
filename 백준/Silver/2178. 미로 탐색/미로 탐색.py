# 최소 거리 문제: BFS. 큐 활용하기

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze_list = []  # 미로 정보를 저장하는 리스트
for _ in range(N):
    maze_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dq = deque()
dq.append((0, 0))  # 출발점 좌표

def explore(y, x):
    # 이동 가능한지 확인하고 큐에 추가
    # 하
    if y != N-1:
        if maze_list[y+1][x] == 1:
            maze_list[y+1][x] = maze_list[y][x] + 1  # 탐색을 마친 칸은 값을 이동횟수로 변경. 재방문을 막음
            dq.append((y+1, x))
    # 우
    if x != M-1: 
        if maze_list[y][x+1] == 1:
            maze_list[y][x+1] = maze_list[y][x] + 1
            dq.append((y, x+1))
    # 상
    if y != 0:
        if maze_list[y-1][x] == 1:
            maze_list[y-1][x] = maze_list[y][x] + 1
            dq.append((y-1, x))
    # 좌
    if x != 0:
        if maze_list[y][x-1] == 1:
            maze_list[y][x-1] = maze_list[y][x] + 1
            dq.append((y, x-1))
    
while True:
    now = dq.popleft()
    if now[0] == N-1 and now[1] == M-1:  # 도착점에 도달함
        print(maze_list[now[0]][now[1]])
        break
    explore(now[0], now[1])
