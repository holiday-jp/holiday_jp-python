 [![PyPI version](https://img.shields.io/pypi/v/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![PyPI downloads](https://img.shields.io/pypi/dm/holiday-jp.svg)](https://pypi.org/project/holiday-jp/)
 [![GitHub release](https://img.shields.io/github/release/holiday-jp/holiday_jp-python.svg)](https://github.com/holiday-jp/holiday_jp-python/releases)

# holiday_jp-python リポジトリ

## 概要

`holiday_jp-python` リポジトリは、**Python言語**向けの日本の祝日データを提供するライブラリです。このライブラリを使用することで、簡単に日本の祝日情報を取得し、カレンダーアプリケーションや日程管理ツールなどで利用することができます。based on [holiday-jp](https://github.com/holiday-jp/holiday_jp) dataset

## インストール

`pip` を使用して、簡単に `holiday_jp` ライブラリをインストールできます。

```bash
pip install holiday-jp
```

## 使用方法

```python
from holiday_jp import HolidayJp

# 特定の年の祝日を取得
holidays_2024 = HolidayJp.year_holidays(year=2024)
print([one_holiday.date_obj for one_holiday in holidays_2024])

>> [datetime.date(2024, 1, 1), datetime.date(2024, 1, 8), datetime.date(2024, 2, 11), datetime.date(2024, 2, 12), datetime.date(2024, 2, 23), datetime.date(2024, 3, 20), datetime.date(2024, 4, 29), datetime.date(2024, 5, 3), datetime.date(2024, 5, 4), datetime.date(2024, 5, 5),...

# 休日の情報を文字列として取得するためのフォーマットを指定する。
def format_holiday_as_string(holiday):
    return f"{holiday.date_obj.strftime('%Y年%m月%d日')}（{holiday.week}）「{holiday.name}」"

print([format_holiday_as_string(one_holiday) for one_holiday in holidays_2024])

>> ['2024年01月01日（月）「元日」', '2024年01月08日（月）「成人の日」', '2024年02月11日（日）「建国記念の日」', '2024年02月12日（月）「建国記念の日 振替休日」', '2024年02月23日（金）「天皇誕生日」', '2024年03月20日（水）「春分の日」', '2024年04月29日（月）「昭和の日」', '2024年05月03日（金）「憲法記念日」',...
```

## サポートされている機能

- 特定の月の祝日一覧を取得:

```python
from holiday_jp import HolidayJp

# 特定の月の祝日一覧を取得
holidays_may_2024 = HolidayJp.month_holidays(year=2024, month=5)
print([one_holiday.date_obj for one_holiday in holidays_may_2024])

>> [datetime.date(2024, 5, 3), datetime.date(2024, 5, 4), datetime.date(2024, 5, 5), datetime.date(2024, 5, 6)]
```

- 特定の日が振替休日かどうかを確認:

```python
from holiday_jp import HolidayJp

# 特定の日が振替休日かどうかを確認
is_substitute_holiday = holiday.is_substitute_holiday(date='2024-05-06')
print(is_substitute_holiday)

>> True
```

- 今日が祝日かどうかを確認:

```python
from datetime import date

# 今日が祝日かどうかを確認
today_is_holiday = holiday.is_holiday(date=date.today())
print(today_is_holiday)

>> False
```

これらの例を使用することで、`holiday_jp` ライブラリを柔軟かつ効果的に利用することができます。ライブラリのドキュメントも参照して、さらに詳細な情報を得ることができます。

## 貢献

バグ報告や新機能の提案は、GitHubのイシュートラッカーを使用してください。また、プルリクエストも歓迎しています。詳細については、CONTRIBUTING.md ファイルを参照してください。

## ライセンス

このプロジェクトは MIT License ライセンスの下で公開されています。詳細については、[LICENSE](https://github.com/holiday-jp/holiday_jp-python/blob/master/LICENSE) ファイルを参照してください。


## 代替

`holiday_jp` と [jpholiday](https://github.com/Lalcs/jpholiday) の比較


1. データの正確性とアップデート

    holiday_jp-python: 日本の祝日データは、holiday-jp から抽出され、更新が頻繁に行われています。GitHub リポジトリは、最新のデータと連携しています。 holiday_jp-python は、holiday-jp/holiday_jp リポジトリのメンテナンスおよびコミュニティによってサポートされています。

    jpholiday: jpholiday は、祝日API からデータを取得しています。ライブラリのメンテナンスとデータのアップデートは、APIの提供者に依存しています。

2. インターフェースと使用方法

    holiday_jp-python: holiday_jp ライブラリは、シンプルで直感的なAPIを提供し、特定の年や月の祝日情報を取得する際に柔軟性があります。

    jpholiday: jpholiday も使いやすいライブラリであり、jpholidayモジュールから祝日情報を取得することができます。ただし、一部の機能やオプションが異なる場合があります。

3. カスタマイズオプション

    holiday_jp-python: holiday_jp は、特定の日が振替休日かどうかや国民の休日かどうかを確認するための専用の関数を提供しており、柔軟なオプションを利用できます。

    jpholiday: jpholiday も同様の機能を提供していますが、それぞれのライブラリで提供されているオプションには若干の違いがあります。

## まとめ

どちらのライブラリも、日本の祝日情報を取得するために便利で使いやすいものであり、プロジェクトの要件や好みによって選択できます。holiday_jp-python は、holiday-jp/holiday_jp リポジトリの共通データセットをベースにしており、コミュニティによってメンテナンスされています。両方のドキュメントを参照し、使用例を確認した上で、プロジェクトに最適なものを選択することをお勧めします。



ありがとうございます。楽しんで使っていただけることを願っています！
