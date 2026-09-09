import math

def calculate_time_length(str1, str2):
    h1, m1 = map(int, str1.split(':'))
    h2, m2 = map(int, str2.split(':'))
    return (h2 * 60 + m2) - (h1 * 60 + m1)

def solution(fees, records):
    stayed_time_dict = {}  # 차량번호:주차시간(m)
    in_record_dict = {}  # 차량번호:입차시간
    for record in records:
        time, number, action = record.split(' ')
        if action == 'IN':
            in_record_dict[number] = time
        else:  # OUT
            stayed_time = calculate_time_length(in_record_dict[number], time)
            del in_record_dict[number]
            if number in stayed_time_dict:
                stayed_time_dict[number] += stayed_time
            else:
                stayed_time_dict[number] = stayed_time
                
    for number, time in in_record_dict.items():
        stayed_time = calculate_time_length(time, "23:59")
        if number in stayed_time_dict:
            stayed_time_dict[number] += stayed_time
        else:
            stayed_time_dict[number] = stayed_time
        
    answer = []
    for number, time in sorted(stayed_time_dict.items()):
        price = fees[1]
        addered = time - fees[0]
        if addered > 0:
            price += fees[3] * math.ceil((addered / fees[2]))
        answer.append(price)
        
    return answer