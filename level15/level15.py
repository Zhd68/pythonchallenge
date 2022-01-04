#print(1006 / 4)
#print(1016 / 4) #first year
#print(1026 / 4)
#print(1036 / 4) #second year
#print(1996 / 4) #last year

leap_years = list(range(1016, 1997, 20))
from datetime import date
leap_year_26_jan_is_mon = [year for year in leap_years if date(year, 1, 26).weekday() == 0]
print(leap_year_26_jan_is_mon)

#Mozart was born on January 27, 1756
#answer mozart

#this is an alternative option from the vastness of Google
import datetime, calendar
for year in range(1006,1996,10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)