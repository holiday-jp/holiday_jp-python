# -*- coding: utf-8 -*-
import datetime
import zenhan
from .holidays import HolidayDataset


class HolidayJp(object):
  """Holiday in Japan."""

  date_obj = '' # the date object
  week = '' # the week day in jp ex: 木
  week_en = '' # the week day in en ex: Thursday
  name = '' # the name of the holiday in jp ex: 元日
  name_en = '' # the name of the holiday in en ex: New Year's Day
  is_holiday = False # if the day is a holiday day

  def __init__(self, date):
    """init the date and fill the property."""
    # if date is string support the following format otherwise must be a date or datetime object
    if isinstance(date, str):
      # normalize
      date = zenhan.z2h(date)
      try:
        self.date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
      except Exception as e:
        raise e
    else:
      self.date_obj = date

    date_str = self.date_obj.strftime('%Y-%m-%d')
    if HolidayDataset.HOLIDAYS.get(date_str):
      # as the date is in the dict
      self.is_holiday = True
      self.week = HolidayDataset.HOLIDAYS[date_str]['week']
      self.week_en = HolidayDataset.HOLIDAYS[date_str]['week_en']
      self.name = HolidayDataset.HOLIDAYS[date_str]['name']
      self.name_en = HolidayDataset.HOLIDAYS[date_str]['name_en']
