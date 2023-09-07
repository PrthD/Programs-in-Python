num_enem,num_class = map(int,input().split(' '))
enem_atck_range = list(map(int,input().split(' ')))
clss_atck_range = list(map(int,input().split(' ')))

max_enem_atck = max(enem_atck_range)
min_enem_atck = min(enem_atck_range)
max_clss_atck = max(clss_atck_range)
clss_atck_range.sort()

if max_clss_atck <= min_enem_atck:
    print('-1')
else:
    for class_attack in clss_atck_range:
        if class_attack > max_enem_atck:
            print(class_attack)
            break