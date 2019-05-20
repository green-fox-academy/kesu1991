import csv

with open('logs.csv') as csvfile:   
    readCSV = csv.reader(csvfile, delimiter=",")
    
    list_logs = []

    for row in readCSV:
        list_logs.append("".join(row))

###### What is the average arrival time?       
    date = []
    time = []
    id   = []

    unique_id = set()

    for i in range(len(list_logs)):

        match_date = re.search(r'([0-9]{4}\.\d+\.\d+)', list_logs[i])
        match_time = re.search(r'(\d+\:\d+\:\d+)', list_logs[i])
        match_id = re.search(r'(\d+:\d+$)', list_logs[i])

        date.append(match_date.group(1))
        time.append(match_time.group(1))
        id.append(match_id.group(1))
        unique_id.add(match_id.group(1))

    #print(date)
    #print(time)
    #print(door)
    #print(id)
    #print(unique_id)

    # Iterate each id and store it into list unique_time
    unique_time = []

    for i in unique_id:

        personal_date = []
        unique_date = set()

        indices = list(n for (n, e) in enumerate(id) if e == i)
        #print(indices)

        for i in range(len(indices)):
            personal_date.append(date[indices[i]])
            unique_date.add(date[indices[i]])
            #print(unique_date)
            #print(personal_date)
        
        for i in unique_date:
            date_indices = list(n for (n, e) in enumerate(personal_date) if e == i)
            #print(date_indices)

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

           # print(time_compList)

            first_arr_pos = indices[date_indices[time_compList.index(min(time_compList))]]
            first_arr_time = time[first_arr_pos]

            unique_time.append(first_arr_time)

    print(unique_time)
