#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
# jdbc:postgresql://rds0y318279u98i0da7y.pg.rds.aliyuncs.com:3433/eye_app?charSet=UTF-8
# conn = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="rds0y318279u98i0da7y.pg.rds.aliyuncs.com", port="3433")
  
print "Opened database successfully"  

cur=conn.cursor()
 
cur.execute("SELECT * from t_student;")
# cur.execute("select id,site_name FROM t_site_info WHERE site_name is not null")
# cur.fetchall()
rows = cur.fetchall()
for row in rows:
    print "ID = ", row[0]
    print "NAME = ", row[1], "\n"
    
print "Operation done successfully";
cur.close()
conn.close()  