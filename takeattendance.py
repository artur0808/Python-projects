import MySQLdb
from MySQLdb import escape_string as thwart
#from .dbconnect import connection
import os
import time 
import calendar
import datetime
from datetime import date
import gc

conn = MySQLdb.connect(host="localhost", user = "root", passwd = "root", db = "SBAS")
c = conn.cursor()

status 	= "absent"
e_id	= 2
my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]


date 	= time.strftime('%Y-%m-%d')
time 	= time.strftime('%H:%M:%S')
month   = datetime.datetime.now().strftime("%m") 
year    = datetime.datetime.now().strftime("%y") 

prop_hour = time[:2]
prop_min1 = 0
mid_one	  = time[3:4]
mid_two   = time[4:5]
 

my_list = [0,1,2,3,4,5,6,7,8,9]

if prop_hour == '09' and prop_min1 == mid_one and mid_two in my_list:
	print ("on timee")
	status = "on time"
	c.execute("INSERT INTO attendance (date,month,year,weekday,time,status,emp_id) VALUES (%s,%s, %s, %s, %s, %s, %s)", (thwart(date), thwart(month), thwart(year), thwart(weekday), thwart(time), thwart(status),int(emp_id)))
else:
	print ("late")
	status = "late" 
	c.execute("INSERT INTO attendance (date,month,year,weekday,time,status,emp_id) VALUES (%s,%s, %s, %s, %s, %s, %s)", (thwart(date), thwart(month), thwart(year), thwart(weekday), thwart(time), thwart(status),int(emp_id)))
#c.execute("INSERT INTO attendance (date,time,status,e_id,weekday) VALUES (%s,%s, %s, %s, %s)", (thwart(date), thwart(time), thwart(status), int(e_id), thwart(weekday)))


conn.commit()

c.close()
conn.close()
gc.collect()   # garbage cleaner






