# -*- coding: utf-8 -*-
import datetime
from .holidays import HolidayDataset


class HolidayJp(object):
  """Holiday in Japan."""

  date_obj = '' # the date object
  week = '' # the week day in jp ex: 木
  week_en = '' # the week day in en ex: Thursday
  name = '' # the name of the holiday in jp ex: 元日
  name_en = '' # the name of the holiday in en ex: New Year's Day
  is_holiday = False # if the day is a holiday day
  is_business_day = False # if the day is from [monday, friday]

  # defaul business day can be overwritten depends on context
  BUSINESS_DAY = ['月', '火', '水', '木', '金']

  HOLIDAY_DATASET = HolidayDataset.HOLIDAYS
  DATASET_FORMAT = '%Y-%m-%d'

  DATE_FORMAT = '%Y-%m-%d'

  def __init__(self, date):
    """init the date and fill the property.

      date: string with the following format yyyy-mm-dd (default, overwrite DATE_FORMAT for other format)
        or date object
    """
    self.date_obj = self._format_date(date)

    date_str = self.date_obj.strftime(self.DATE_FORMAT)
    if self.HOLIDAY_DATASET.get(date_str):
      # as the date is in the dict
      self.is_holiday = True
      self.week = self.HOLIDAY_DATASET[date_str]['week']
      self.week_en = self.HOLIDAY_DATASET[date_str]['week_en']
      self.name = self.HOLIDAY_DATASET[date_str]['name']
      self.name_en = self.HOLIDAY_DATASET[date_str]['name_en']
      if self.week in self.BUSINESS_DAY:
        self.is_business_day = True
    else:
      # Monday is 0 and Sunday is 6.
      if self.date_obj.weekday() < 5:
        self.is_business_day = True

  @classmethod
  def _format_date(cls, date):
    """Format the date to date object."""
    import unicodedata
    date_obj = None
    # if date is string support the following format otherwise must be a date or datetime object
    if isinstance(date, str):
      # normalize
      date = unicodedata.normalize('NFKC', date)
      # plus hyphen
      date = date.replace('−', '-')

      try:
        date_obj = datetime.datetime.strptime(date, cls.DATE_FORMAT).date()
      except Exception as e:
        raise e
    else:
      date_obj = date

    return date_obj

  @classmethod
  def between(cls, start, last):
    """Return a tuple of HolidayJp objects between 2 dates.

      start, last: string with the following format yyyy-mm-dd
        or date object
    """
    start = cls._format_date(start)
    last = cls._format_date(last)

    result = []

    if last < start:
      raise ValueError('last must be greater than start.')

    # include the limit in the format of the dataset
    start_date_str = start.strftime(cls.DATASET_FORMAT)
    if cls.HOLIDAY_DATASET.get(start_date_str):
      result.append(cls(start))
    # go day by day
    next_day = start + datetime.timedelta(days=1)

    while next_day <= last:
      next_day_str = next_day.strftime(cls.DATASET_FORMAT)
      if cls.HOLIDAY_DATASET.get(next_day_str):
        result.append(cls(next_day))
      next_day += datetime.timedelta(days=1)

    return result

  @classmethod
  def year_holidays(cls, year):
    """Return a list of HolidayJp for a given year."""
    return cls.between('%s-01-01' % year, '%s-12-31' % year)

  @classmethod
  def month_holidays(cls, year, month):
    """Return a list of HolidayJp for a given month year."""
    import calendar
    # get the last day of the month
    last_day = calendar.monthrange(year, month)
    return cls.between('%s-%s-01' % (year, month), '%s-%s-%s' % (year, month, last_day[1]))
