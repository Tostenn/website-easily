from datetime import datetime
from time import localtime

temps = localtime()


data_actuel = datetime(temps.tm_year,temps.tm_mon,temps.tm_mday,temps.tm_hour,temps.tm_min,temps.tm_sec)

date_sortir = datetime(2023,3,10,0,0,0)


print(f'il reste {date_sortir - data_actuel} avant la sortir officiel du script')
