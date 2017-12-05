# -*- coding: UTF-8 -*-
# 文件名：测试hello
'''
Created on 2017年9月1日

@author: Administrator
'''

import urllib  
import urllib2
import json
import psycopg2
import time

def getData():
    conn = psycopg2.connect(database="hospital_db", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.189", port="5432")
    querysql="select * from t_site_info where tags && ARRAY['order'::varchar,'view'::varchar] and (longitude is null or latitude is null)  limit 20 offset 0"
    cur=conn.cursor()
 
    cur.execute(querysql)
    rows = cur.fetchall()
    
    n=0
    for row in rows:
        id=str(row[0])
        site_name=str(row[1])
        city=getAddress(site_name)
        insersql=""
        if city==None:
            print site_name,'获取详细地址失败'
            insersql="UPDATE t_site_info SET  longitude='0', latitude='0' WHERE id='"+id+"';"
        else:
            locationlist=getLocation(city.encode("utf-8"))
            insersql="UPDATE t_site_info SET  longitude='"+locationlist[0]+"', latitude='"+locationlist[1]+"' WHERE id='"+id+"';"
            print insersql,n
            
        cur.execute(insersql)
        n=n+1
            
    print "Operation done successfully";
    conn.commit()
    cur.close()
    conn.close()
    
    time.sleep(2)
    
    return

def getAddress(sitename):
    targeturl="http://ditu.amap.com/service/poiTipslite?&words="+urllib.quote(sitename)
    req = urllib2.Request(targeturl)
    res_data = urllib2.urlopen(req)
    res = res_data.read()

    s = json.loads(res)
    
    if s["data"]=="Not found.":
        return 
    else:
        jsontip=s["data"]["tip_list"][0]["tip"]
        district=jsontip.get('district', "")
        address=jsontip.get('address', "")
    
    return district+address
  
def getLocation(address):
    url = "http://restapi.amap.com/v3/geocode/geo?key=aa4a48297242d22d2b3fd6eddfe62217&s=rsv3&address='"+urllib.quote(address)+"'"
    req = urllib2.Request(url)
    
    res_data = urllib2.urlopen(req)
    res = res_data.read()

    s = json.loads(res)
    
    location=s["geocodes"][0]["location"]
    locationlist=location.split(',')
    return locationlist
    
def countSite():
    hasSite=True
    while hasSite:
        conn = psycopg2.connect(database="hospital_db", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="10.0.13.189", port="5432")
        querysql="select * from t_site_info where tags && ARRAY['order'::varchar,'view'::varchar] and (longitude is null or latitude is null)  limit 1"
        cur=conn.cursor()
 
        cur.execute(querysql)
        rows = cur.fetchall()
        if len(rows)>0:
            cur.close()
            conn.close()
            time.sleep(2)
            try:
                getData()
            except Exception:
                time.sleep(5)
                print "连接出异常了"
                getData()
            else:
                print "执行成功"
                time.sleep(3)
        else:
            break
       


print countSite()

