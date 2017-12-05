#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import psycopg2

# import demjson

def insertData():
    conninsertp = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")
    conninsertc = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")
    conninsertd = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.181", port="5432")
   
    curp=conninsertp.cursor()
    curc=conninsertc.cursor()
    curd=conninsertd.cursor()
    
    areadata=load();
    
#     print areadata["province"][0]["name"]
#     print areadata["province"][0]["id"]
    
    arrayp = areadata["province"]
    for province in arrayp:
        insertProvince="INSERT INTO t_address_province(name, code )VALUES ( '"+province["name"]+"', '"+province["id"]+"');"
#         print insertProvince
        curp.execute(insertProvince);
        arrayc=province["city"]
        for city in arrayc:
#             print city["name"]+" "+city["id"];
            insertCity="INSERT INTO t_address_city(name, code )VALUES ( '"+city["name"]+"', '"+city["id"]+"');"
#             print insertCity
            curc.execute(insertCity);
            district=city.get('district', "")
            if len(district)>0:
                arrayd=city["district"]
                for d in arrayd:
                    insertDistrict="INSERT INTO t_address_district(name, code )VALUES ( '"+d["name"]+"', '"+d["id"]+"');"
#                     print insertDistrict
                    curd.execute(insertDistrict);
            
            
#         print areadata["province"][0]["id"]
    conninsertp.commit()
    curp.close()
    conninsertp.close()
    conninsertc.commit()
    curc.close()
    conninsertc.close()
    conninsertd.commit()
    curd.close()
    conninsertd.close()
    
    print "Opened database successfully" 

def load():
    with open('areafile.json') as json_file:
        data = json.load(json_file)
#         print "open successfully"
#         data2=demjson.decode(data);
        return data
# cur=conn.cursor()
#  
# cur.execute("SELECT * from t_student;")
# # cur.execute("select id,site_name FROM t_site_info WHERE site_name is not null")
# # cur.fetchall()
# rows = cur.fetchall()
# for row in rows:
#     print "ID = ", row[0]
#     print "NAME = ", row[1], "\n"
#     
# print "Operation done successfully";
# cur.close()
# conn.close()  

insertData();

# load();