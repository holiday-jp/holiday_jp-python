[![Build Status](https://travis-ci.org/LUXEYS/holiday_jp-python.svg?branch=master)](https://travis-ci.org/LUXEYS/holiday_jp-python)
 [![PyPI version](https://img.shields.io/pypi/v/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![PyPI downloads](https://img.shields.io/pypi/dm/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![GitHub release](https://img.shields.io/github/release/LUXEYS/holiday_jp-python.svg)](https://github.com/LUXEYS/holiday_jp-python/releases)


# holiday_jp-python

Japanese holiday for Python

## install

> pip install holiday-jp


### dependencies
> pip3 install -r requirements.txt

using dataset from https://github.com/holiday-jp/holiday_jp

### test
> python3 -m unittest holiday_jp.test

### for dev
Build on linux with python 3.6

Build command:
> python setup.py sdist

OR

Run ./build.sh
build the package that will be available in the dist/ directory

### alternative install

download the release and install this way:
pip3 install holiday_jp-xxx.tar.gz

## Usage

```
from holiday_jp import HolidayJp
if HolidayJp('1990-01-01').is_holiday:
  print('True')

work with date
import datetime
from holiday_jp import HolidayJp

if HolidayJp(datetime.date.today()).is_holiday:
  print('False')
else:
  print('True')

# Between return holidays between 2 dates in text
holidays = HolidayJp.between('2009-01-01', '2009-01-31')
new_year_day = holidays[0]
self.assertEqual(datetime.date(year=2009, month=1, day=1), new_year_day.date_obj)
self.assertEqual('元日', new_year_day.name)

# Or date object
holidays = HolidayJp.between(datetime.date(year=2008, month=12, day=23), datetime.date(year=2009, month=1, day=12))
```

For more usage check the unit test holiday_jp/test.py
