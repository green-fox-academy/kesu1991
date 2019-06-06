def Average(lst): 
    return sum(lst) / len(lst) 


demand_list = []

def avg_demands(demand_level):
    demand_list.append(demand_level)
    return Average(demand_list)


def pricing_function(days_left, tickets_left, demand_level):

    global price
    avg_ticket = tickets_left / days_left
    avg_demand = avg_demands(demand_level)
        
    # Last Day
    if days_left == 1 and avg_demand > demand_level and tickets_left > 30:
        remain = 20 - avg_ticket
        price = demand_level - avg_ticket + remain
    elif days_left == 1 and avg_demand > demand_level and tickets_left < 10:
        remain = 10 - avg_ticket
        price = demand_level - avg_ticket + remain
   
    # Days longer than 15
    if days_left >= 15 and avg_demand > demand_level:
        price = demand_level - avg_ticket + 4
    elif days_left >= 15 and avg_demand < demand_level:
        price = demand_level - avg_ticket + 3

    # Days between 3 to 7
    if days_left >= 3 and days_left >= 7 and avg_demand > demand_level:
        price = demand_level - avg_ticket + 5
    elif days_left >= 3 and days_left >= 7 and avg_demand < demand_level:
        price = demand_level - avg_ticket + 2

    # Days between 2 to 3
    if days_left >= 2 and days_left >= 3 and avg_demand > demand_level:
        price = demand_level - avg_ticket + 6
    elif days_left >= 3 and days_left >= 7 and avg_demand < demand_level:
        price = demand_level - avg_ticket + 1 

    return price

    


















    


