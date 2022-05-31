# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    routes = []
    departures = []
    n_route = len(tickets)

    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            departures.append(i)

    for departure_i in departures:
        stack = []
        visited = [False] * n_route
        stack.append(departure_i)
        visited[departure_i] = True

        while stack:
            if len(stack) == n_route:
                tmp = []
                for index in stack:
                    tmp.append(tickets[index][0])
                tmp.append(tickets[index][1])
                routes.append(tmp)
            top = stack[-1]
            pop_flag = True
            for i, ticket in enumerate(tickets):
                if tickets[top][1] == ticket[0]:
                    if visited[i]:
                        continue
                    else:
                        stack.append(i)
                        visited[i] = True
                        pop_flag = False
                        break
            if pop_flag:
                stack.pop()
            else:
                continue
            print('routes : ', routes)

    min_destination = min(routes[0])
    min_route = routes[0]

    for route in routes:
        min_i = n_route-1
        for i, destination in enumerate(route):
            if min_destination == destination:
                if i < min_i:
                    min_i = i
                    min_route = route
    return min_route


if __name__ == '__main__':
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets3 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN", "JFK"], ["ICN", "JFK"]]
    tickets4 = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
    print(solution(tickets4))
