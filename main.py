import datetime as dt


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return self.records

    def get_today_stats(self):
        return sum(
            [record.amount for record in self.records
                if record.date == dt.date.today()])

    def get_week_stats(self):
        last_week = dt.date.today() - dt.timedelta(weeks=1)
        return sum(
            [record.amount for record in self.records
                if last_week <= record.date <= dt.date.today()]
                )


class Record:
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = comment
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = date


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, \
                    но с общей калорийностью не более {calories} \
                    кКал'
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00

    def get_today_cash_remained(self, currency):
        count = self.limit - self.get_today_stats()

        currencies = {
            "rub": ('руб', 1),
            "usd": ('USD', self.USD_RATE),
            "eur": ('Euro', self.EURO_RATE)
        }

        name, rate = currencies[currency]

        if currency == "rub":
            total = int(abs(count / rate))
        else:
            total = round(abs(count / rate), 2)

        if count > 0:
            return f'На сегодня осталось {total} {name}'
        elif count == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {total} {name}'
