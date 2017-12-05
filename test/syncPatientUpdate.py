#!/usr/bin/python
# -*- coding: utf-8 -*-
# '''同步历史数据，问诊档案'''
import psycopg2
import json
import time
import datetime
from warnings import catch_warnings
#json string

conninsert = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")

curinsert = conninsert.cursor()

curinsert.execute("SELECT archive_info,user_id FROM t_user_archive tua where tua.deleted=false  GROUP BY archive_info,user_id")
rows = curinsert.fetchall()
for row in rows:
    user_id = str(row[1])
    s = json.loads(json.dumps(row[0]))
    age=long(s["age"])/1000
    name=str(s["name"].encode("utf-8"))
    name=s["name"]
    sex=s["sex"]
#     print "age",age,"name",name,"sex",sex
    timet=""
    if age>0:
        timet = datetime.datetime.fromtimestamp(age)
    else:
        timet = datetime.datetime.fromtimestamp(0L)
#     print timet
    name=name.replace("'",'')
#     timet=timet.replace("'",'')
#     try:
    rowinfo=row[0]
    rowinfo.pop('name')
#     print rowinfo
#     rowinfo=rowinfo.replace("'",'')
    
#     insertsql="INSERT INTO t_patient_archive(user_id, name, gender,birthday,archive_info, level, deleted, self, create_time) VALUES ('"+user_id+"', '"+name+"', '"+sex+"','"+str(timet)+"', '"+json.dumps(row[0])+"'::jsonb, 0, false, false, now()) "
    insertsql="INSERT INTO t_patient_archive(user_id, name, gender,birthday,archive_info, level, deleted, self, create_time) VALUES ('"+user_id+"', '"+name+"', '"+sex+"','"+str(timet)+"', '"+json.dumps(rowinfo)+"'::jsonb, 0, false, false, now()) "
    print insertsql
    curinsert.execute(insertsql)
#     except Exception:
#         print insertsql
#     else:
#         print "执行成功"
        
    
print "Opened database successfully"   
conninsert.commit()
conninsert.close()