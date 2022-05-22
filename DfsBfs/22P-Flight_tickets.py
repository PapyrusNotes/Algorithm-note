# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    answer = []
    departure = []

    for ticket in tickets:
        if ticket[0] == 'ICN':
            departure.append(ticket)


    return answer


if __name__ == '__main__':

    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(tickets1))
