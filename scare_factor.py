audi, num_movies, max_scare = map(int,input().split())

scr_fct_dict = {}
for i in range(1,audi+1):
    scr_fct_dict['audi_' + str(i)] = [int(n) for n in input().split()]

choice_dict = {}
for j in range(1,num_movies+1):
    choice_dict['show_' + str(j)] = []

t = 1
for key in scr_fct_dict:
    for k in scr_fct_dict[key]:
        choice_dict['show_' + str(t)].append(k)
        t += 1
    t = 1

choice_dict['min_sf_shows'] = []
for key in choice_dict:
    choice_dict['min_sf_shows'].append(min(choice_dict[key]))
choice_dict['min_sf_shows'].pop()
choice_dict['min_sf_shows'] = sorted(choice_dict['min_sf_shows'])   
    
cumsum_sf = 0
movies = 0
for k in choice_dict['min_sf_shows']:
    if (cumsum_sf + k) <= max_scare:
        movies += 1
        cumsum_sf += k
print(movies)    
