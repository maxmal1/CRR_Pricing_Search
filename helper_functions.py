from datetime import datetime, date


def day_to_year(options_date):
    #options_date format:
    # July 7, 2023
    current_date = date.today()
    #current_date format:
    # 2023-07-06
    
    year_split = options_date.split(", ")
    month_split = year_split[0].split(" ")
    
    d2 = date(int(year_split[1]),month_dict[month_split[0]], int(month_split[1]))
    
    delta = d2 - current_date
    
    
    
    
    
    
    return delta.days

month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12
}