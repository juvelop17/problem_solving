

def solution(companies, applicants):
    answer = []

    com_appli = {}
    com_info = {}
    for com in companies:
        name, pri, num = com.split()
        com_info[name] = [pri, num]
        com_appli[name] = []

    waiting = []
    appli_info = {}
    for appli in applicants:
        name, pri, num = appli.split()
        cnt = 0
        appli_info[name] = [pri, num, cnt]
        waiting.append(name)
    while len(waiting) > 0:
        while(len(waiting) > 0):
            appli_name = waiting.pop()
            appli_pri, appli_num, appli_cnt = appli_info[appli_name]
            com_appli[appli_pri[appli_cnt]].append(appli_name)
        
    return answer



companies =["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants =["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]

# companies =["A abc 2", "B abc 1"]
# applicants =["a AB 1", "b AB 1", "c AB 1"]


