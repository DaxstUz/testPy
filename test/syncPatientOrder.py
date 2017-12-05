#!/usr/bin/python
# -*- coding: utf-8 -*-
# '''同步历史数据，问诊档案,同步预约档案'''                   
import psycopg2

conn = psycopg2.connect(database="hospital_db", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")
conninsert = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")

cur = conn.cursor()
curinsert = conninsert.cursor()

cur.execute("SELECT id,creator_uid,name,contact,card_no,COALESCE(gender, 'o') as gender,COALESCE(birthday, '1800-01-01'::TIMESTAMP) as birthday,create_time FROM t_visitor_info WHERE creator_uid is not null ORDER BY create_time desc")
rows = cur.fetchall()
for row in rows:
    id=str(row[0])
    user_id=str(row[1])
    name = str(row[2])
    contact = str(row[3])
    card_no = str(row[4])
    gender = str(row[5])
    birthday = str(row[6])
    create_time = str(row[7])
#     sql="INSERT INTO t_patient_archive( id,user_id, name, contact,card_no, gender,level, deleted, self,birthday,create_time) VALUES ('"+id+"','"+user_id+"','"+name+"','"+contact+"','"+card_no+"','"+gender+"',2,false,false,'"+birthday+"','"+create_time+"')"
    sql="UPDATE t_patient_archive set contact='"+contact+"' WHERE id='"+id+"'"
    print sql
    curinsert.execute(sql)
  
print "Opened database successfully"   
# conninsert.commit()
# conninsert.close()

