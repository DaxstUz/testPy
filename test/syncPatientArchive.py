#!/usr/bin/python 
# -*- coding: utf-8 -*-
# '''同步历史数据本人档案''' 
import psycopg2

conn = psycopg2.connect(database="eyebiz_db", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")
conninsert = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")

cur = conn.cursor()
curinsert = conninsert.cursor()

cur.execute("SELECT user_id,fullname,COALESCE(phone, '@@') as phone,COALESCE(person_no, '@@') as person_no,COALESCE(sex, 'o') as sex,COALESCE(birth_date, '1800-01-01'::TIMESTAMP) as birth_date,0 as level ,FALSE as DELETE,true as self ,COALESCE(create_time, '1800-01-01'::TIMESTAMP) as create_time FROM t_5 WHERE deleted=FALSE and user_id is not null ORDER BY create_time desc")
rows = cur.fetchall()
n=0
file_object = open('update.txt', 'w+')
for row in rows:
    user_id=str(row[0])
    name = str(row[1])
    contact = str(row[2])
    card_no = str(row[3])
    gender = str(row[4])
    birthday = str(row[5])
    create_time = str(row[9])
    name=name.replace("'",'')
#     sql="INSERT INTO t_patient_archive( user_id, name, contact,card_no, gender, birthday,level, deleted, self, create_time) VALUES ('"+user_id+"','"+name+"','"+contact+"','"+card_no+"','"+gender+"','"+birthday+"',0,false,true,'"+create_time+"')"
    sql="UPDATE t_patient_archive set contact='"+contact+"' WHERE self=true and user_id='"+user_id+"'"
    
    if contact!='@@':
        file_object.write(sql+";"+'\n')

    n=n+1
    print sql,n
#     curinsert.execute(sql)

file_object.close()  
print "Opened database successfully"   
# conninsert.commit()
# conninsert.close()