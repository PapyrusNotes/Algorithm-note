# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    route = []
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
                temp = list(stack)
                route.append(temp)
            print('route : ', route)
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
            print('route : ', route)


if __name__ == '__main__':
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(tickets1))
