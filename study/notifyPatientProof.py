#coding:utf8
__author__ = 'sunyz@ieyecloud.com'
import psycopg2  #sudo yum install python-psycopg2
import datetime
from sendmail import MyEmail

now = datetime.datetime.now()
#last_time =((now-datetime.timedelta(minutes=6)).strftime("%Y-%m-%d %H:%M:00"))
last_time = (now-datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:00")
print 'last_time', last_time
print 'now', now


# 数据库连接参数
conn = psycopg2.connect(database="eye_app", user="ieye-appserver", password="eyebiz_pg_i0da7y", host="rds0y318279u98i0da7y.pg.rds.aliyuncs.com", port="3433")
cur = conn.cursor()

sql="SELECT proof_image,phone,account_ali FROM t_order_reward  where create_time >='"+ last_time + "'"
print sql
cur.execute(sql)
result = cur.fetchall()

conn.commit()
cur.close()
conn.close()

print 'result: ', result
#print archive_dict
#exit(0)

if len(result):
    content = '新增预约完善资料：\n\n'
    for order in result:
        proof_image='凭证'
        pcontact='电话'
        account_ali='支付宝账号'
        
        content += proof_image + '  ' +pcontact + '  ' +account_ali+'  '+str(order[0])+'  '+str(order[1])+'  '+str(order[2])
        content += '\n' 
    my = MyEmail()
#     my.user = "wuxy@ieyecloud.com"
#     my.passwd = "Passw0rd"
#     my.to_list = ["liufeng@ieyecloud.com","wuxy@ieyecloud.com","liuzheng@ieyecloud.com","lijiaojiao@ieyecloud.com","yangchangshun@ieyecloud.com","zhangjifeng@ieyecloud.com","wangye@ieyecloud.com","chaiyuxiao@ieyecloud.com","jiangguoguo@ieyecloud.com"]
#     my.to_list = ["sunyz@ieyecloud.com"]
        #cc 收不到邮件
        #my.cc_list = ["wuxy@ieyecloud.com"]
    my.sub = '医院预约完善资料[' + last_time + ' -- ' + now.strftime("%Y-%m-%d %H:%M:%S") + ']'
    my.content = content
    my.send()

else:
    content = '没有新的预约完善资料'
    print content

