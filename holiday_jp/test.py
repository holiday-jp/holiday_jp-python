# -*- coding: utf-8 -*-
import datetime
from unittest import TestCase
from holiday_jp import HolidayJp


class HolidayJpTest(TestCase):
  """Test the holiday class."""

  def test_init(self):
    """Check that the calss init correctly."""
    HolidayJp('1990-01-01') # support string
    HolidayJp(datetime.date(year=1990, month=1, day=1)) # date
    with self.assertRaises(ValueError):
      HolidayJp('Banana') # but not banana

  def test_is_holiday(self):
    """Check that is_holiday is working as expected."""
    # first day of the year is holiday and business day so don't come to office
    one_holiday_date = HolidayJp('1990-01-01')
    self.assertEqual(one_holiday_date.is_holiday, True)
    # today is working day as I'm in office
    not_holiday_date = HolidayJp('2018-10-18')
    self.assertEqual(not_holiday_date.is_holiday, False)
    self.assertEqual(not_holiday_date.is_business_day, True)
    # but 20 is weekend not holiday but don't come to office
    not_business_date = HolidayJp('2018-10-20')
    self.assertEqual(not_business_date.is_holiday, False)
    self.assertEqual(not_business_date.is_business_day, False)

  def test_other_data_holiday(self):
    """Check that the data are correctly initialized."""
    one_holiday_date = HolidayJp('1990-01-01')
    self.assertEqual(one_holiday_date.week, '月')
    self.assertEqual(one_holiday_date.week_en, 'Monday')
    self.assertEqual(one_holiday_date.name, '元日')
    self.assertEqual(one_holiday_date.name_en, "New Year's Day")
    self.assertEqual(one_holiday_date.is_business_day, True)

  def test_other_data_not_holiday(self):
    """Check that for not holiday the data are empty."""
    not_holiday_date = HolidayJp('2018-10-18')
    self.assertEqual(not_holiday_date.week, '')
    self.assertEqual(not_holiday_date.week_en, '')
    self.assertEqual(not_holiday_date.name, '')
    self.assertEqual(not_holiday_date.name_en, '')

  def test_custom_holiday(self):
    """Check that I can overwrite and add custom holiday."""
    # default is not holiday
    not_holiday_date = HolidayJp('2018-10-01')
    self.assertEqual(not_holiday_date.is_holiday, False)

    from holiday_jp.holidays import HolidayDataset
    my_holiday = HolidayDataset.HOLIDAYS

    my_holiday.update({'2018-10-01': {
      'week': '月',
      'week_en': 'Monday',
      'name': '誕生日',
      'name_en': 'Birthday',
    }})

    class MyHolidayJp(HolidayJp):
      # overwrite the holiday dataset
      HOLIDAY_DATASET = my_holiday

    new_holiday_date = MyHolidayJp('2018-10-01')
    self.assertEqual(new_holiday_date.is_holiday, True)

  def test_between(self):
    """Check that I can retrieved holiday date between 2 dates."""
    # add a full width date to test the normalization
    holidays = HolidayJp.between('２００９−０１−０１', '2009-01-31')
    new_year_day = holidays[0]
    self.assertEqual(datetime.date(year=2009, month=1, day=1), new_year_day.date_obj)
    self.assertEqual('元日', new_year_day.name)
    self.assertEqual("New Year's Day", new_year_day.name_en)
    self.assertEqual('木', new_year_day.week)

    self.assertEqual(datetime.date(year=2009, month=1, day=12), holidays[1].date_obj)
    self.assertEqual('成人の日', holidays[1].name)

    holidays = HolidayJp.between(datetime.date(year=2008, month=12, day=23), datetime.date(year=2009, month=1, day=12))

    self.assertEqual(datetime.date(year=2008, month=12, day=23), holidays[0].date_obj)
    self.assertEqual(datetime.date(year=2009, month=1, day=1), holidays[1].date_obj)
    self.assertEqual(datetime.date(year=2009, month=1, day=12), holidays[2].date_obj)
