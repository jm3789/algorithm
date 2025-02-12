def solution(name, yearning, photo):
    answer = []
    yearning_dict = {}
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
    for name_list in photo:
        number = 0
        for name_item in name_list:
            if name_item in name:
                number += yearning_dict[name_item]
        answer.append(number)
    return answer