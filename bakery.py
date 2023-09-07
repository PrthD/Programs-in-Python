from math import ceil

n, m, k = map(int,input().split())
temp_i = sorted(list(map(int,input().split())))

if k == 0:
    counter = {}
    for k in temp_i:
        counter[k] = temp_i.count(k)
    time = 0
    for value in counter.values():
        time += ceil(value/m)
    print(time)
    exit()
elif m == 1:
    print(n)
    exit()

temp_range = list(range(temp_i[0],temp_i[0] + 2*k + 1))
time = 1
batch = 1
for temp in temp_i:
    if (batch < m) and temp in temp_range:
        batch += 1
        if temp == temp_i[-1]:
            print(time)
            exit()
    elif (batch == m) and temp in temp_range:
        if temp == temp_i[-1]:
            print(time)
            exit()
        time += 1
        batch = 1
        idx = temp_i.index(temp)
        temp_range = list(range(temp_i[idx+1],temp_i[idx+1] + 2*k + 1))
    elif temp not in temp_range:
        time += 1
        batch = 2
        if temp == temp_i[-1]:
            print(time)
            exit()
        idx = temp_i.index(temp)
        temp_range = list(range(temp_i[idx],temp_i[idx] + 2*k + 1))