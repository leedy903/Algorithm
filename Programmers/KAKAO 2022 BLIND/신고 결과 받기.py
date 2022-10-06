def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_dict = {}
    for id in id_list:
        report_dict[id] = set()
    
    for r in report:
        a, b = r.split()
        report_dict[b].add(a)
        
    for criminal, reporters in report_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1
    return answer