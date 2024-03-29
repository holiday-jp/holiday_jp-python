 [![PyPI version](https://img.shields.io/pypi/v/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![PyPI downloads](https://img.shields.io/pypi/dm/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![GitHub release](https://img.shields.io/github/release/holiday-jp/holiday_jp-python.svg)](https://github.com/holiday-jp/holiday_jp-python/releases)

# holiday_jp-python

Japanese holiday for Python 3+
using dataset from https://github.com/holiday-jp/holiday_jp

## install

> pip3 install holiday-jp

### If you want to contribute
Build on linux with python 3.x

#### Clone the project or download the source
> git clone https://github.com/holiday-jp/holiday_jp-python

#### test
> python3 -m unittest holiday_jp.test

OR

> make test

Build command:
> python3 setup.py sdist

OR

> make build

It will build the package and be available in the dist/ directory

### alternative install

download the release and install this way:
pip3 install holiday_jp-xxx.tar.gz

## Usage

```python
from holiday_jp import HolidayJp
# with string date YYYY-MM-DD
if HolidayJp('1990-01-01').is_holiday:
  print('True')

import datetime
from holiday_jp import HolidayJp
# or date object
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
