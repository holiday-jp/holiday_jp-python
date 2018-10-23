# holiday_jp-python

Japanese holiday for Python

# dependencies
> pip3 install zenhan

using dataset from https://github.com/holiday-jp/holiday_jp

# test
> python3 -m unittest holiday_jp.test

# for dev
Build on linux with python 3.6

Build command:
> python setup.py sdist

OR

Run ./build.sh
build the package that will be available in the dist/ directory

# install

download the release and install this way:
pip3 install holiday_jp-xxx.tar.gz

# Usage

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
```

check the unit test holiday_jp/test.py
