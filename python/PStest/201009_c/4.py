
def dfs(cur, hub, dest, r_dict, visited):
    if cur == dest:
        if visited[hub]:
            return 1
        return 0
    if visited[cur]:
        return 0

    cnt = 0
    next_list = r_dict.get(cur,[])
    for next in next_list:
        visited[cur] = True
        cnt += dfs(next,hub,dest,r_dict,visited)
        visited[cur] = False

    return cnt

def solution(depar, hub, dest, roads):
    answer = -1
    visited = {}

    r_dict = {}
    for road_list in roads:
        start = road_list[0]
        end = road_list[1]
        visited[start] = False
        visited[end] = False
        if start not in r_dict:
            r_dict[start] = []
        r_dict[start].append(end)
    print(r_dict)
    print(visited)

    answer = dfs(depar,hub,dest,r_dict,visited)
    print(answer)



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

