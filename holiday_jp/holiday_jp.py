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

  def __init__(self, date):
    """init the date and fill the property.

      date: string with the following format yyyy-mm-dd
        or date object
    """
    self.date_obj = HolidayJp._format_date(date)

    date_str = self.date_obj.strftime('%Y-%m-%d')
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

  def _format_date(date):
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
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
      except Exception as e:
        raise e
    else:
      date_obj = date

    return date_obj

  def between(start, last):
    """Return a tuple of HolidayJp objects between 2 dates.

      start, last: string with the following format yyyy-mm-dd
        or date object
    """
    from dateutil import relativedelta

    start = HolidayJp._format_date(start)
    last = HolidayJp._format_date(last)

    result = []

    if last < start:
      raise ValueError('last must be greater than start.')

    # include the limit
    start_date_str = start.strftime('%Y-%m-%d')
    if HolidayJp.HOLIDAY_DATASET.get(start_date_str):
      result.append(HolidayJp(start))
    # go day by day
    next_day = start + relativedelta.relativedelta(days=1)

    while next_day <= last:
      next_day_str = next_day.strftime('%Y-%m-%d')
      if HolidayJp.HOLIDAY_DATASET.get(next_day_str):
        result.append(HolidayJp(next_day))
      next_day += relativedelta.relativedelta(days=1)

    return result
