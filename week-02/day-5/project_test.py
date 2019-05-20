import re
string1 = "1,2019.01.02. 9:21:49,Access granted,203,12,A66 - 04 FÕBEJÁRAT (F-1) Door #1,5,Czender András,0,,0,,00215:09895"
string2 = "1,2019.01.02. 10:21:49,Access granted,203,12,A66 - 04 FÕBEJÁRAT (F-1) Door #1,5,Czender András,0,,0,,00215:09895"
string3 = "1,2019.01.02. 10:21:49,Access granted,203,12,A66 - 04 FÕBEJÁRAT (F-1) Door #1,5,Czender András,0,,0,,00789:06785"
string4 = "1,2019.01.03. 9:21:40,Access granted,203,12,A66 - 04 FÕBEJÁRAT (F-1) Door #1,5,Czender András,0,,0,,00215:09895"

# Matching date/time and ID by main entrance
list_test = [string1,string2,string3,string4]


date = []
time = []
door = []
id   = []

unique_id = set()

for i in range(len(list_test)):

    match_date = re.search(r'(\d+\.\d+\.\d+)', list_test[i])
    match_time = re.search(r'(\d+\:\d+\:\d+)', list_test[i])
    match_door = re.search(r'(A66 - 04)', list_test[i])
    match_id = re.search(r'(\d+:\d+$)', list_test[i])

    date.append(match_date.group(1))
    time.append(match_time.group(1))
    door.append(match_door.group(1))
    id.append(match_id.group(1))
    unique_id.add(match_id.group(1))

print(date)
print(time)
print(door)
print(id)
print(unique_id)

# Iterate each id and store it into list unique_time
unique_time = []

for i in unique_id:

    personal_date = []
    unique_date = set()

    indices = list(n for (n, e) in enumerate(id) if e == i)
    print(indices)

    for i in range(len(indices)):
        personal_date.append(date[indices[i]])
        unique_date.add(date[indices[i]])
        print(unique_date)
        print(personal_date)
    
    for i in unique_date:
        date_indices = list(n for (n, e) in enumerate(personal_date) if e == i)
        print(date_indices)

        time_compList = []

        for i in range(len(date_indices)):

            h = re.search(r'(\d+)\:\d+\:\d+',time[indices[date_indices[i]]])
            m = re.search(r'\d+\:(\d+)\:\d+',time[indices[date_indices[i]]])
            s = re.search(r'\d+\:\d+\:(\d+)',time[indices[date_indices[i]]])

            personal_h_s = int(h.group(1)) * 60 * 60
            personal_m_s = int(m.group(1)) * 60
            personal_s   = int(s.group(1))

            personal_time = personal_h_s + personal_m_s + personal_s

            time_compList.append(personal_time)

        print(time_compList)

        first_arr_pos = indices[date_indices[time_compList.index(min(time_compList))]]
        first_arr_time = time[first_arr_pos]

        unique_time.append(first_arr_time)

print(unique_time[2])





