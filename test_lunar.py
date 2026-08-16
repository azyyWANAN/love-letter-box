# -*- coding: utf-8 -*-
"""探测 zhdate / cnlunar 的 API，供阿昼改造主脚本用"""
import datetime

print("=== zhdate ===")
from zhdate import ZhDate

zd = ZhDate.from_datetime(datetime.datetime.now())
print("今天农历对象属性:", zd.__dict__)
print("chinese():", zd.chinese())
print("2026元宵(1-15):", ZhDate(2026, 1, 15).to_datetime())
print("2026七夕(7-7):", ZhDate(2026, 7, 7).to_datetime())
print("2026中秋(8-15):", ZhDate(2026, 8, 15).to_datetime())
print("2026烟烟阴历生日(8-27):", ZhDate(2026, 8, 27).to_datetime())
print("2026春节(1-1):", ZhDate(2026, 1, 1).to_datetime())

print("=== cnlunar ===")
try:
    import cnlunar
    d = cnlunar.Lunar(datetime.datetime.now(), godType="8char")
    print("cnlunar ok")
    print("todaySolarTerms:", d.todaySolarTerms)
    print("has thisYearSolarTermsDic:", hasattr(d, "thisYearSolarTermsDic"))
    if hasattr(d, "thisYearSolarTermsDic"):
        print("thisYearSolarTermsDic:", d.thisYearSolarTermsDic)
    # 把所有属性名打出来
    attrs = [a for a in dir(d) if not a.startswith("_")]
    print("attrs:", attrs)
except Exception as e:
    print("cnlunar失败:", repr(e))
