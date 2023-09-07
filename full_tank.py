from turtle import distance


length,capacity,number_gas_st,time_refuel = list(map(int,input().split()))
gas_stations = list(map(int,input().split()))

dist_travelled = 0
time_taken = 0
if capacity >= length:
    print(length)
else:
    while dist_travelled+capacity < length:
        if (capacity+dist_travelled) in gas_stations:
            dist_travelled += capacity
            time_taken += capacity + time_refuel
        else:
            for p in range(len(gas_stations)):
                if gas_stations[p] > (capacity+dist_travelled):
                    time_taken += (gas_stations[p-1]-dist_travelled) + time_refuel
                    dist_travelled = gas_stations[p-1]
                elif (p == len(gas_stations)-1) and (dist_travelled+capacity < length):
                    time_taken +=  (gas_stations[p]-dist_travelled) + time_refuel
                    dist_travelled = gas_stations[p]
    time_taken = time_taken - (dist_travelled-length)
    print(time_taken)
