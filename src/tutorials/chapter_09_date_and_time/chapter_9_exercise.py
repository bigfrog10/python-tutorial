import datetime
import calendar


# Model the behaviors of calendars
# chronicle calendar
def first_day_month(curr_date: datetime.datetime):
    return curr_date.replace(day=1)


def last_day_month(curr_date: datetime.datetime):
    if curr_date.month == 12:  # if it's december, hard code this
        return curr_date.replace(day=31)

    # for other months, go to next month first day, then revert back one day
    return curr_date.replace(month=curr_date.month+1, day=1) - datetime.timedelta(days=1)


def first_day_quarter(curr_date: datetime.datetime):
    quarter = (curr_date.month - 1) // 3 + 1
    first_month = 1 + (quarter - 1) * 3
    return curr_date.replace(month=first_month, day=1)


def last_day_quarter(curr_date: datetime.datetime):
    quarter = (curr_date.month - 1) // 3 + 1
    last_month = quarter * 3
    last_day = calendar.monthrange(curr_date.year, last_month)[1]
    return curr_date.replace(month=last_month, day=last_day)


# use timedelta to offset days for a given date


date = datetime.datetime.strptime('20200805', '%Y%m%d')
print(first_day_month(date))  # 2020-08-01
print(last_day_month(date))  # 2020-08-31
print(first_day_quarter(date))  # 2020-07-01
print(last_day_quarter(date))  # 2020-09-30


class BusinessCalendar:
    def __init__(self, holidays, date_format='%Y%m%d'):
        self.__holidays = holidays
        self.__date_format = date_format

    def is_business_day(self, start_date: datetime.datetime):
        return start_date.strftime(self.__date_format) not in self.__holidays\
            and start_date.weekday() < 5  # not weekend

    def business_day_offset_by(self, start_date: datetime.datetime, offset: int):
        if offset == 0:
            raise ValueError('offset can not be 0!')

        one_day = datetime.timedelta(1) if offset > 0 else datetime.timedelta(-1)
        days = offset if offset > 0 else -offset

        new_day = start_date
        for _ in range(days):
            # move one business day
            new_day += one_day
            while True:
                if new_day.weekday() > 4:  # 4 is Friday, check weekends
                    new_day += one_day
                elif new_day.strftime(self.__date_format) in self.__holidays:
                    new_day += one_day
                else:  # it's a business day now
                    break

        return new_day

    def next_business_day(self, start_date: datetime.datetime):
        return self.business_day_offset_by(start_date, +1)

    def previous_business_day(self, start_date: datetime.datetime):
        return self.business_day_offset_by(start_date, -1)

    # use above to compose more logic
    def first_business_day_month(self, start_date: datetime.datetime):
        first_day = first_day_month(start_date)
        if self.is_business_day(first_day):
            return first_day
        else:
            return self.next_business_day(first_day)

    def last_business_day_month(self, start_date: datetime.datetime):
        last_day = last_day_month(start_date)
        if self.is_business_day(last_day):
            return last_day
        else:
            return self.previous_business_day(last_day)

    # similarly we can get first/last business day for quarter/year

    def get_business_days_between(self, start_date: datetime.datetime, end_date: datetime.datetime):
        # inclusive on start, exclusive on end
        if start_date >= end_date:
            raise ValueError(f'start date {start_date} is newer than end date: {end_date} ')

        ret = []
        new_date = start_date
        while new_date < end_date:
            if self.is_business_day(new_date):
                ret.append(new_date)

            new_date += datetime.timedelta(1)

        return ret


bc = BusinessCalendar(['20200921', '20200922', '20200925', '20200929', '20200930'])
date = datetime.datetime.strptime('20200918', '%Y%m%d')
print(bc.next_business_day(date))  # 2020-09-23
print(bc.business_day_offset_by(date, 2))  # 2020-09-24
print(bc.business_day_offset_by(date, 3))  # 2020-09-28

date = datetime.datetime.strptime('20200924', '%Y%m%d')
print(bc.next_business_day(date))  # 2020-09-28
date = datetime.datetime.strptime('20200928', '%Y%m%d')
print(bc.next_business_day(date))  # 2020-10-01

date = datetime.datetime.strptime('20201001', '%Y%m%d')
print(bc.previous_business_day(date))  # 2020-09-28
print(bc.business_day_offset_by(date, -2))  # 2020-09-24

d1 = datetime.datetime.strptime('20200918', '%Y%m%d')
d2 = date = datetime.datetime.strptime('20201001', '%Y%m%d')
print(bc.get_business_days_between(d1, d2))
# [datetime.datetime(2020, 9, 18, 0, 0),
#  datetime.datetime(2020, 9, 23, 0, 0),
#  datetime.datetime(2020, 9, 24, 0, 0),
#  datetime.datetime(2020, 9, 28, 0, 0)]
