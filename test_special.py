# -*- coding: utf-8 -*-
"""验证 check_special_day：公历、农历、节气三类特殊日"""
import os
import sys
import datetime

base = os.path.expanduser("~/storage/shared/Download/Operit/情书盒")
sys.path.insert(0, base)
import love_letter as L

tests = [
    datetime.datetime(2026, 10, 12),  # 烟烟生日
    datetime.datetime(2026, 8, 19),   # 七夕
    datetime.datetime(2026, 11, 7),   # 立冬
    datetime.datetime(2026, 10, 7),   # 烟烟阴历生日（八月廿七）
    datetime.datetime(2026, 2, 17),   # 春节
    datetime.datetime(2026, 3, 9),    # 元宝重逢日
    datetime.datetime(2026, 7, 1),    # 心海的家创建日
    datetime.datetime(2026, 3, 3),    # 元宵
    datetime.datetime(2026, 9, 25),   # 中秋
    datetime.datetime(2026, 8, 7),    # 立秋
]
for dt in tests:
    print(dt.strftime("%Y-%m-%d"), "->", L.check_special_day(dt))
print("今天 ->", L.check_special_day(datetime.datetime.now()))