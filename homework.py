import datetime as dt

class Calculator():
    def __init__ (self, limit):
        self.limit = limit
        self.records = []
        
    def add_record(self, record):
        self.records.append(record)
        return self.records
    
    def get_today_stats(self):
        return sum([record.amount for record in self.records if record.date == dt.date.today()])
      
    def get_week_stats(self):
        last_week = dt.date.today() - dt.timedelta(weeks=1)
        return sum([record.amount for record in self.records if last_week <= record.date <= dt.date.today()])
        

class Record:
    def __init__ (self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = comment
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
        else:
            self.date = date
        
class CaloriesCalculator(Calculator):

    def get_calories_remained(self):    
        if self.get_today_stats() < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал'
        return 'Хватит есть!'
            
class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00 
    
    def get_today_cash_remained(self, currency):
        count = self.limit - self.get_today_stats()
        
        cash_dict = {
        "rub" : ('руб', 1),
        "usd" : ('USD', self.USD_RATE),
        "eur" : ('Euro', self.EURO_RATE)
        }

        total = abs(count / cash_dict[currency][1])

        if count > 0:
            return f'На сегодня осталось {int(total) if currency == "rub" else round(total, 2)} {cash_dict[currency][0]}'
        elif count == 0:
            return 'Денег нет, держись'      
        else:
            return f'Денег нет, держись: твой долг - {int(total) if currency == "rub" else round(total, 2)} {cash_dict[currency][0]}'







