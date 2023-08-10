# 리스트에서 탐색할 경우 이중 for문 -> 시간초과.
# 딕셔너리 2개로 구성해서 풀기

import sys

N, M = map(int, sys.stdin.readline().split())

# 포켓몬 도감 만들기
pokemon_intkey_dic = {}  # key가 포켓몬번호, value가 포켓몬이름인 딕셔너리
pokemon_strkey_dic = {}  # key가 포켓몬이름, value가 포켓몬번호인 딕셔너리
for i in range(N):
    pokemon_num = i+1
    pokemon_name = sys.stdin.readline().rstrip()
    pokemon_intkey_dic[pokemon_num] = pokemon_name
    pokemon_strkey_dic[pokemon_name] = pokemon_num

# M개의 문제 풀기
for _ in range(M):
    q = sys.stdin.readline().rstrip()
    # 숫자 문제인 경우, pokemon_intkey_dic에서 찾기
    if q.isnumeric() == True:  
        q = int(q)
        ans = pokemon_intkey_dic[q]
    # 문자 문제인 경우, pokemon_strkey_dic에서 찾기
    else:  
        ans = pokemon_strkey_dic[q]
    # 답 출력
    print(ans)
