import pymysql

# 连接测试数据库
connect = pymysql.Connect(
    host='192.168.15.104',
    port=3306,
    user='crm_rtmap',
    passwd='rtmap-911',
    db='test',
    charset='utf8'
)
