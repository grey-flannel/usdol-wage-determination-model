from enum import StrEnum


# These names were taken from the Python holidays package for consistency
class Holiday(StrEnum):
    new_years_day = 'New Year\'s Day'
    mlk_day = 'Martin Luther King Jr. Day'
    memorial_day = 'Memorial Day'
    independence_day = 'Independence Day'
    labor_day = 'Labor Day'
    veterans_day = 'Veterans Day'
    thanksgiving_day = 'Thanksgiving Day'
    day_after_thanksgiving = 'Day After Thanksgiving'
    christmas_day = 'Christmas Day'
