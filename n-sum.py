n,m = map(int,input().split(' '))

n_list = [1]*n
iterator = 0
for i in n_list:
    n_list[iterator] = iterator + 1
    iterator += 1

if m <= n:
    print(1)
    print(m)
else:
    sum = n
    k_int = [n]
    n_list.reverse()
    for k in range(1,n):
        sum += n_list[k]
        k_int.append(n_list[k])
        if sum == m:
            print(len(k_int))
            k_int.reverse()
            print(*k_int,sep=' ')
        elif sum > m:
            sum -= n_list[k]
            k_int.pop()  