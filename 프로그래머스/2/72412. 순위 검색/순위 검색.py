# number 이상의 값이 최초로 나오는 인덱스 반환
def lower_bound(number_list, number):
    left = 0
    right = len(number_list)
    while left < right:
        mid = (left + right) // 2
        if number_list[mid] < number: 
            left = mid + 1
        else: # mid >= number
            right = mid
    return right
    

def solution(info, query):
    answer = []
    
    # 경우의 수와 해당 지원자들의 점수 리스트 를 해시로 연결
    list1 = ['cpp', 'java', 'python', '-']
    list2 = ['backend', 'frontend', '-']
    list3 = ['junior', 'senior', '-']
    list4 = ['chicken', 'pizza', '-']
    info_dict = {}
    for s1 in list1:
        for s2 in list2:
            for s3 in list3:
                for s4 in list4:
                    s = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4
                    info_dict[s] = []
        
    # info문에 해당하는 조건의 value값에 점수 넣기
    for info_item in info:
        for key in info_dict.keys():
            flag = True
            a_list = list(key.split())  # info_dict의 key
            b_list = list(info_item.split()) # 현재 info item
            for i in range(4):
                if a_list[i] != '-' and a_list[i] != b_list[i]:
                    flag = False
                    break
            if flag:
                info_dict[key].append(int(b_list[4]))
            
    # value값에 있는 점수들 정렬
    for value in info_dict.values():
        value.sort()
        
    # 각 쿼리마다 딕셔너리에서 해당 조건을 찾고 답 구하기
    for query_item in query:
        # 쿼리에서 'and' 제거하고 숫자 부분을 분리
        query_item = query_item.replace(' and', '')
        number = int(list(query_item.split())[-1])
        order = query_item.replace(' '+ str(number), '')
        # number 이상의 값이 처음 나타나는 부분 찾기
        score_list = info_dict[order]
        answer.append(len(score_list) - lower_bound(score_list, number))
    return answer