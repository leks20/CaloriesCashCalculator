import datetime as dt

class Calculator():
    def __init__ (self, limit):
        self.limit = limit
        self.records = []
        
    def add_record(self, record):
        self.record = record
        self.records.append(record)
        return self.records
    
    def get_today_stats(self):
        total_day = 0
        for i in self.records:
            if i.date == dt.date.today():
                total_day += i.amount
        return total_day
    
    def get_week_stats(self):
        total_week = 0
        last_week = dt.date.today() - dt.timedelta(weeks=1)
        for i in self.records:
            if last_week <= i.date <= dt.date.today():
                total_week += i.amount
        return total_week

class Record:
    def __init__ (self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = comment
        if (type(date)==str):
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
        else:
            self.date = date
        
class CaloriesCalculator(Calculator):

    def get_calories_remained(self):    
        if self.get_today_stats() < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал'
        else:
            return 'Хватит есть!'
            
class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    def get_today_cash_remained(self, currency):
        self.currency = currency
        count = self.limit - self.get_today_stats()
        if count == 0:
            return 'Денег нет, держись'      
        else:
            if self.currency == "rub":
                if count > 0:
                    return f'На сегодня осталось {count} руб'
                else:
                    return f'Денег нет, держись: твой долг - {abs(count)} руб'
            elif self.currency == "usd":
                if count > 0:
                    return f'На сегодня осталось {round(count / self.USD_RATE, 2)} USD'
                else:
                    return f'Денег нет, держись: твой долг - {round(abs(count) / self.USD_RATE, 2)} USD'
            else:
                if count > 0:
                    return f'На сегодня осталось {round(count / self.EURO_RATE, 2)} Euro'
                else:
                    return f'Денег нет, держись: твой долг - {round(abs(count) / self.EURO_RATE, 2)} Euro'







