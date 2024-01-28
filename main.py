'''
from datetime import datetime
def get_days_from_today(date):
    try:
        date_1 = datetime.strptime(date, "%Y-%m-%d")
        date_2 = datetime.now()
        difference = date_2.toordinal() - date_1.toordinal()
        print(difference)
    except ValueError:
        print("Дату записано в неправильному форматі")


date = input("Введіть дату у форматі YYYY-MM-DD: ")  
get_days_from_today(date)
'''


import random

def get_numbers_ticket(min, max, quantity):
    for num in [min, max, quantity]:
        if not (1<= num <= 1000):
            return []
        random_numbers = random.sample(range(min, max+1), quantity)
        return sorted(random_numbers)
        
            
lottery_numbers = get_numbers_ticket(1, 70, 6)
print(lottery_numbers)