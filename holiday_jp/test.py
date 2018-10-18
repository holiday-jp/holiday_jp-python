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
    with self.assertRaises(ValueError) as context:
      HolidayJp('Banana') # but not banana

  def test_is_holiday(self):
    """Check that isHoliday is working as expected."""
    # first day of the year is holiday
    one_holiday_date = HolidayJp('1990-01-01')
    self.assertEqual(one_holiday_date.is_holiday, True)
    # today is working day as I'm in office
    not_holiday_date = HolidayJp('2018-10-18')
    self.assertEqual(not_holiday_date.is_holiday, False)

  def test_other_data_holiday(self):
    """Check that the data are correctly initialized."""
    one_holiday_date = HolidayJp('1990-01-01')
    self.assertEqual(one_holiday_date.week, '月')
    self.assertEqual(one_holiday_date.week_en, 'Monday')
    self.assertEqual(one_holiday_date.name, '元日')
    self.assertEqual(one_holiday_date.name_en, "New Year's Day")

  def test_other_data_not_holiday(self):
    """Check that for not holiday the data are empty."""
    not_holiday_date = HolidayJp('2018-10-18')
    self.assertEqual(not_holiday_date.week, '')
    self.assertEqual(not_holiday_date.week_en, '')
    self.assertEqual(not_holiday_date.name, '')
    self.assertEqual(not_holiday_date.name_en, '')
