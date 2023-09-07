from bisect import bisect

applicants = int(input())
net_worth = sorted([int(input()) for i in range(applicants)])

N = 1
for i in range(applicants):
    count = len(net_worth) - bisect(net_worth, i)
    if count >= N and (i < (applicants-1)):
        N += 1
    elif count >= N and (i == (applicants-1)):
        print(N)
    else:
        print(N-1)
        break