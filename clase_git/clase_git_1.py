import datetime as dt
import random

for x in range(10):
    print(f'numero random: {random.randint(1,100)}')

fecha_hoy = dt.datetime.now().strftime('%d/%m/%Y')

print(fecha_hoy)