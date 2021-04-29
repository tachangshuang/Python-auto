import pytest

import db
import time



def test_func_check():
    report = "../report/all_report.html"
    # 获取游标
    cursor = db.connect.cursor()
    # 查询数据
    sql = 'SELECT application_name, creat_time, status_id from application_program where status_id = 0'
    cursor.execute(sql)
    if cursor.rowcount > 0:
        for row in cursor.fetchall():
            if row[0] == '会员管理' and row[2] == 0:
                print('**********会员管理数据**********')
                from case.vip_info.ReadExcelInterface import test_send_mail
                test_send_mail(report)
                test_update_check()
                pytest.main(
                    ["-q", "../case/vip_info/find_vipinfo.py", "../case/vip_info/login.py", '-v', '--html=../report/all_report.html',
                     '--self'
                     '-contained-html'])
    else:
        print("**********func暂无数据**********")


def test_update_check():
    # 获取游标
    cursor = db.connect.cursor()
    # 更新数据
    sql1 = 'UPDATE application_program SET status_id = 1 ,update_time = NOW() where status_id = 0'
    cursor.execute(sql1)
    db.connect.commit()
    if cursor.rowcount > 0:
        print("**********共有", cursor.rowcount, "条数据更新成功**********")
    else:
        print("**********update暂无数据**********")
    cursor.close()



def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def time_check():
    second = sleeptime(0, 0, 5)
    while 1 == 1:
        time.sleep(second)
        test_func_check()

