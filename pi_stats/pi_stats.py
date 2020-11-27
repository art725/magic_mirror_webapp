from gpiozero import CPUTemperature
from time import sleep
from datetime import datetime as dt
import mariadb

# used to record cpu temperature of the pi
# this will be presented on the magic mirror
# for monitoring

now = dt.now()
cpu_temp_degc = CPUTemperature().temperature
cpu_temp_degf = cpu_temp_degc*9/5+32

date_time = now.strftime("%m/%d/%Y %H:%M:%S")

conn = mariadb.connect(
    user="paul",
    password="lubu",
    host="localhost",
    database="familydb"
)


while True:
    cur = conn.cursor()

    add_detail = ("INSERT INTO pi_stats "
                    "(date_time, cpu_temp_degf) "
                    "VALUES (%s, %s)")

    detail_data = (date_time, cpu_temp_degf)

    cur.execute(add_detail, detail_data)
    conn.commit()
    cur.close()

    sleep(60)