from datetime import datetime, timedelta
from locale import setlocale, LC_ALL

setlocale(LC_ALL, "pt_BR.utf-8")

data = datetime(2020, 2 ,21, 22, 24, 29)
print(data.strftime("%A-%B-%Y"))
print()
print(datetime.today())
print()
print(datetime.now())
