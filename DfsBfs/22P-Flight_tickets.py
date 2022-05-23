# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    stack = []
    route = ['ICN']
    visited = [False]*len(tickets)
    candidates = []

    for ticket in tickets:
        if ticket[0] == 'ICN':
            candidates.append(ticket)

    departure = candidates[0]

    for i in range(0, len(candidates) - 1):
        if candidates[i][1] < candidates[i + 1][1]:
            departure = i

    stack.append(departure)
    route.append(tickets[departure][1])
    visited[departure] = True

    while stack:
        top = stack[-1]
        arrival = tickets[top][1]

        for i, ticket in enumerate(tickets):
            if visited[i]:
                continue
            elif arrival == ticket[0]:
                stack.append(i)
                visited[i] = True
                break




    return answer


if __name__ == '__main__':
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(tickets1))
