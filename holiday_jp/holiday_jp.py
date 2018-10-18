# -*- coding: utf-8 -*-
import datetime
import zenhan


class HolidayJp(object):
  """Holiday in Japan."""

  date_obj = '' # the date object
  week = '' # the week day in jp ex: 木
  week_en = '' # the week day in en ex: Thursday
  name = '' # the name of the holiday in jp ex: 元日
  name_en = '' # the name of the holiday in en ex: New Year's Day
  is_holiday = False # if the day is a holiday day

  HOLIDAYS = ''

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

    if not self.HOLIDAYS:
      self.HOLIDAYS = self.build_dict()

    date_str = self.date_obj.strftime('%Y-%m-%d')
    if self.HOLIDAYS.get(date_str):
      # as the date is in the dict
      self.is_holiday = True
      self.week = self.HOLIDAYS[date_str]['week']
      self.week_en = self.HOLIDAYS[date_str]['week_en']
      self.name = self.HOLIDAYS[date_str]['name']
      self.name_en = self.HOLIDAYS[date_str]['name_en']

  @staticmethod
  def build_dict():
    """Init the dict."""
    holiday_dict = {}
    with open('holiday_jp/holidays_detailed.yml') as file:
      lines = file.readlines()
      for i in range(0, len(lines)):
        line = lines[i]
        if 'date' in line:
          date_str = line.replace('date: ', '').strip()
          holiday_dict[date_str] = {}
        elif 'week:' in line:
          holiday_dict[date_str]['week'] = line.replace('week: ', '').strip()
        elif 'week_en:' in line:
          holiday_dict[date_str]['week_en'] = line.replace('week_en: ', '').strip()
        elif 'name:' in line:
          holiday_dict[date_str]['name'] = line.replace('name: ', '').strip()
        elif 'name_en:' in line:
          holiday_dict[date_str]['name_en'] = line.replace('name_en: ', '').strip()
    return holiday_dict
