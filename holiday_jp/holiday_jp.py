# -*- coding: utf-8 -*-
import datetime
from .holidays import HolidayDataset


class HolidayJp(object):
  """Holiday in Japan."""

  date_obj = None # the date object
  week = '' # the week day in jp ex: 木
  week_en = '' # the week day in en ex: Thursday
  name = '' # the name of the holiday in jp ex: 元日
  name_en = '' # the name of the holiday in en ex: New Year's Day
  is_holiday = False # if the day is a national holiday
  is_substitute_holiday = False # if the day is a substitute holiday
  is_business_day = False # if the day is from [monday, friday]

  # default business days Monday is 0 and Sunday is 6
  BUSINESS_DAY = [i for i in range(0, 5)]

  HOLIDAY_DATASET = HolidayDataset.HOLIDAYS
  DATASET_FORMAT = '%Y-%m-%d'

  DATE_FORMAT = '%Y-%m-%d'

  def __init__(self, date) -> None:
    """Initialize a HolidayJp instance.

    Parameters:
      date (str or datetime.date): The date to initialize the instance for.
        If a string, must be in the format defined in the DATE_FORMAT constante (default 'YYYY-MM-DD').

    Sets the following instance attributes based on the given date:
      - date_obj: The parsed date object.
      - is_holiday: Whether the date is a national holiday.
      - week: The weekday in Japanese.
      - week_en: The weekday in English.
      - name: The holiday name in Japanese (if a holiday).
      - name_en: The holiday name in English (if a holiday).
      - is_business_day: Whether the date is a business day.
      - is_substitute_holiday: Whether the date is a substitute holiday.
    """
    self.date_obj = self._format_date(date)
    if self.date_obj.weekday() in self.BUSINESS_DAY:
      self.is_business_day = True

    date_str = self.date_obj.strftime(self.DATE_FORMAT)
    if self.HOLIDAY_DATASET.get(date_str):
      # as the date is in the dict
      self.is_holiday = True
      self.week = self.HOLIDAY_DATASET[date_str]['week']
      self.week_en = self.HOLIDAY_DATASET[date_str]['week_en']
      self.name = self.HOLIDAY_DATASET[date_str]['name']
      self.name_en = self.HOLIDAY_DATASET[date_str]['name_en']
      self.is_substitute_holiday = self._check_substitute()

  @classmethod
  def _format_date(cls, date) -> datetime.date:
    """Format a date string or date object to a date object.

    Parameters:
      date (str or datetime.date): The date to format.
        If a string, must match the DATE_FORMAT class constant.

    Returns:
      datetime.date: The formatted date object.

    Raises:
      Exception: If the date string does not match the expected format.
    """
    import unicodedata
    date_obj = date

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

    return date_obj

  @classmethod
  def between(cls, start, last) -> list:
    """Returns a list of HolidayJp objects between the given start and end dates.

    The start and end dates can be strings in the format 'yyyy-mm-dd' or
    datetime.date objects.

    Iterates day-by-day from start to end date and creates a HolidayJp object
    for each date that exists in the holiday dataset.

    Parameters:
      start: The start date, either as string or datetime.date
      end: The end date, either as string or datetime.date

    Returns:
      A list of HolidayJp objects between the start and end dates inclusive.

    Raises:
      ValueError if end date is before start date.
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
  def year_holidays(cls, year) -> list:
    """Returns a list of HolidayJp objects for the given year.

    Iterates day-by-day from Jan 1 to Dec 31 of the given year, and creates a
    HolidayJp object for each date that exists in the holiday dataset.

    Parameters:
      year (int): The year to get holidays for

    Returns:
      list: A list of HolidayJp objects representing the holidays in the given year.
    """
    return cls.between('%s-01-01' % year, '%s-12-31' % year)

  @classmethod
  def month_holidays(cls, year, month) -> list:
    """Returns a list of HolidayJp objects for the given month and year.

    Iterates day-by-day from the 1st to the last day of the given month and year,
    and creates a HolidayJp object for each date that exists in the holiday dataset.

    Parameters:
      year (int): The year to get holidays for
      month (int): The month to get holidays for, 1-12

    Returns:
      list: A list of HolidayJp objects representing the holidays in the given month and year.
    """
    import calendar
    # get the last day of the month
    last_day = calendar.monthrange(year, month)
    return cls.between('%s-%s-01' % (year, month), '%s-%s-%s' % (year, month, last_day[1]))

  def _check_substitute(self) -> bool:
    """Check if the given date is a substitute holiday in Japan.

    A substitute holiday is when a national holiday falls on a Sunday,
    so the following Monday is also a holiday.

    Returns:
      bool: True if the date is a substitute holiday, False otherwise.
    """
    """Check if the day is a substitute holiday."""
    is_substitute_holiday = False

    if self.is_holiday and '振替休日' in self.name:
      is_substitute_holiday = True

    return is_substitute_holiday