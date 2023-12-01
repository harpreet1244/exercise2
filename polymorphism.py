from collections import Counter
my = [1,1,1,2,2,2,2,2,4,4,4,4,]
print(Counter(my))

import datetime

mytime = datetime.time(2,30)
print(mytime)

today = datetime.date.today()
print(today)

print(today.ctime())

from datetime import datetime

mydate = datetime(2021,7,25,14,36,11)
print(mydate)

from datetime import date

d1 = date(2021,11,3)
d2 = date(2022,12,3)
result = d2-d1
print(result)
print(type(result))


