
def dfs(cur, hub, dest, r_dict, visited):





    return cnt

def solution(depar, hub, dest, roads):
    answer = -1





    return answer


depar = "SEOUL"
hub = "ULSAN"
dest = "GWANGJU"
roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"],["BUSAN","ABC"]]

# depar = "ULSAN"
# hub = "SEOUL"
# dest = "BUSAN"
# roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]



print(solution(depar, hub, dest, roads))

