.. holiday_jp-python documentation master file, created by
   sphinx-quickstart on Mon Apr 27 22:13:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to holiday_jp-python's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


$project
========

$project is simple and easy to use, based on a curated list of official holiday.

Basic usage:

    from holiday_jp import HolidayJp
    # with string date format YYYY-MM-DD
    if HolidayJp('1990-01-01').is_holiday:
        print('True')

Features
--------

- Support strings date format or date object.
- Return holidays between 2 dates.
- Get holiday by month and by year.
- More to come :-)

Installation
------------

Install $project by running:

    pip3 install holiday-jp

Contribute
----------

- Issue Tracker: github.com/LUXEYS/$project/issues
- Source Code: github.com/LUXEYS/$project

Support
-------

If you have issues, please let us know.
Open an issue: https://github.com/LUXEYS/holiday_jp-python/issues/new
日本語でも大丈夫です。

License
-------

The project is licensed under the MIT license.
