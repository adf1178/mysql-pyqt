# 定义基本的功能
import hashlib
def GetUserCount(cursor):
    cursor.execute("select User_id from users")
    result = cursor.fetchall()
    re = [x[0] for x in result]
    return max(re)
def md5(str):
    m = hashlib.md5()
    bytes(str,encoding='utf-8')
    m.update(str.encode(encoding='utf-8'))
    return m.hexdigest()
def UseridToUsername(cursor,userid):
    '''
    通过user_id 找用户名
    :param cursor:
    :param userid:
    :return 用户名:
    '''
    sql = "select User_name from users where User_id = %s"
    cursor.execute(sql,userid)
    result = cursor.fetchall()
    return result[0][0]
def UserReg(cursor,db,Userinfo):
    '''
    用户登录
    :param cursor:
    :param db:
    :param Userinfo  [User_id,User_name,passwordHash]:
    :return 成功返回1，失败返回0:
    '''
    User_id = Userinfo[0]
    User_name = Userinfo[1]
    passwordHash = Userinfo[2]
    cursor.execute("select * from users where User_name = %s",User_name)
    result = cursor.fetchall()
    if result!=():
        return -1
    sql_user = "insert into Users (User_id,User_name,Register_date) values (%s,%s,CURDATE())"
    sql_pass = "insert into Login(User_id,Password_hash) values (%s,%s)"
    try:
        cursor.execute(sql_user,[User_id,User_name])
        cursor.execute(sql_pass,[User_id,passwordHash])
        db.commit()
        return 1
    except:
        return 0
def UserLogin(cursor,Userinfo):
    '''
    用户注册
    :param cursor:
    :param Userinfo [User_name,passwordHash]:
    :return 成功返回User_id，失败返回0,错误则返回-1:
    '''
    User_name = Userinfo[0]
    passwordHash = Userinfo[1]
    sql = "select User_id from Users natural join Login where Users.User_name = %s and Login.Password_hash = %s"
    print(sql%(User_name,passwordHash))
    try:
        cursor.execute(sql,[User_name,passwordHash])

        result = cursor.fetchall()
        if result==():
            return 0
        else:
            return result[0]
    except:
        return -1


def insertPatient(cursor,patientinfotuple,db):
    '''

    :param cursor:
    :param infotuple 患者信息的元组，按照一定顺序:
    :param db:
    :return 如果插入成功则返回1， 失败返回0:
    '''
    sql = "insert into Patient(Patient_id, Pname, Province_id,  Id_number, Birthday) values (%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql,patientinfotuple)
        db.commit()
        return 1
    except:
        return 0
def deleteDangerousCar(cursor,trafficInfoList,db):
    '''
    删除某一危险车次
    :param cursor:
    :param trafficInfoList 按照date,Tnumber的顺序:
    :param db:
    :return 删除失败返回0，成功返回1:
    '''
    sql = "delete from traffic where Traffic_date = %s and Tnumber = %s"
    try:
        cursor.execute(sql,trafficInfoList)
        db.commit()
        return 1
    except:
        return 0
def insertdangerousCar(cursor, trafficInfoList, db):
        '''

        :param cursor:
        :param infotuple 危险车次信息的元组，按照一定顺序:
        :param db:
        :return 如果插入成功则返回1， 失败返回0:
        '''
        sql = "insert into Traffic(Traffic_id,Traffic_date,Tnumber) values (%s,%s,%s)"
        try:
            cursor.execute(sql, trafficInfoList)
            db.commit()
            return 1
        except:
            return 0
def QueryIntimeData(cursor,ProvinceId):
    sql = "select Total_number,xianyou,zhiyu,yisi,siwang from intime_data where Province_id=%s"
    cursor.execute(sql,ProvinceId)
    result = cursor.fetchall()
    return result
def UpdateIntimeData(cursor,db):
    '''
    刷新实时数据
    :param cursor:
    :param db:
    :return:
    '''
    sql1 = "update Intime_data as A2 set A2.Total_number = (select count(*) as total from Patient as A1 where A2.Province_id = A1.Province_id)"
    sql2 = "update Intime_data as A2 set A2.zhiyu = (select count(*) as total from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A1.Patient_id=A3.Patient_id and A3.Pstatus=1)"
    sql3 = "update Intime_data as A2 set A2.yisi = (select count(*) as total from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A1.Patient_id=A3.Patient_id and A3.Pstatus=2)"
    sql4 = "update Intime_data as A2 set A2.xianyou = (select count(*) as total from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A1.Patient_id=A3.Patient_id and A3.Pstatus=3)"
    sql5 = "update Intime_data as A2 set A2.siwang = (select count(*) as total from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A1.Patient_id=A3.Patient_id and A3.Pstatus=4)"
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    db.commit()
def ProivinceName_to_Id(cursor,provincename):
    '''

    :param cursor:
    :param provincename 省份名字:
    :return 省份的id:
    '''
    sql = "select Province_id from province where Province_name=%s"
    cursor.execute(sql,provincename)
    result = cursor.fetchall()
    return result[0][0]
def ProivinceId_to_name(cursor,provinceId):
    '''

    :param cursor:
    :param provincename 省份名字:
    :return 省份的id:
    '''
    sql = "select Province_name from province where Province_id=%s"
    cursor.execute(sql,provinceId)
    result = cursor.fetchall()
    return result[0][0]
def GetUserSub(cursor,Userid):
    '''

    :param cursor:
    :param Userid 用户id:
    :return 用户订阅省份元组，如果没有订阅则返回0:
    '''
    sql = "select Province_id from Subscribe where User_id = %s"
    cursor.execute(sql,Userid)
    result = cursor.fetchall()
    return result
def UserSubs(cursor,provinceId,userid,db):
    sql = "insert into subscribe(User_id,Province_id) Values (%s,%s)"
    cursor.execute(sql,[userid,provinceId])
    db.commit()
def GetPatientNumber(choice,cursor):
    '''

    :param choice 0代表全国，大于0代表某个省份:
    :param cursor ，数据库游标:
    :return 用户查询省份病人的结果:
    '''
    if choice==0:
        sql = "select Pstatus,count(*) from patient_status group by Pstatus"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    else:
        re = {}
        for province_id in choice:
            province_id = str(province_id)
            sql = "select Province_id,Pstatus,count(*) from patient_status natural join patient  where province_id=%s group by Pstatus"
            cursor.execute(sql,province_id)
            result = cursor.fetchall()
            re.update({province_id:result})
        return re
def GetDangerNumber(cursor):
    sql = "select count(*) from traffic"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]
def ModifyDangerCar(cursor,before,after,db):
    '''
    根据信息修改危险车次的值
    :param cursor:
    :param before 【原来的日期，原来的车次】:
    :param after   【改后的日期，改后的车次】:
    :param db:
    :return 成功返回1，失败返回0:
    '''
    sql = "update traffic as A2 set A2.Traffic_date = %s, A2.Tnumber = %s where A2.Traffic_date = %s and A2.Tnumber = %s"
    try:
        cursor.execute(sql,[after[0],after[1],before[0],before[1]])
        db.commit()
        return 1
    except:
        return 0
def GetDangerCar(cursor):
    sql = "select * from traffic"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def QueryDangerousCar(cursor,date,carnumber):
    '''

    :param cursor:
    :param date 车次日期:
    :param carnumber 车次:
    :return 如果不危险则返回0，如果危险则返回这个危险车的traffic_id:
    '''
    sql = "select Traffic_id from traffic where Traffic_date = %s and Tnumber = %s"
    cursor.execute(sql,[date,carnumber])
    result = cursor.fetchall()
    if result==():
        return 0
    else:
        return result[0]
def QueryByDateAndProvince(cursor,dates,Provinceid):
    '''
    通过时间和省份来查询历史记录
    :param cursor:
    :param date 时间区间[开始时间，结束时间]:
    :param Provinceid 省份id:
    :return 查询返回结果:
    '''
    sql = "select Pdate,Patient_number,zhiyu,xianyou,yisi,siwang from history_data where Pdate>=%s and Pdate <=%s and Province_id = %s"
    cursor.execute(sql,[dates[0],dates[1],Provinceid])
    result = cursor.fetchall()
    return result
def InsertOrUpdateHistory(cursor,db):
    '''
    更新历史数据，如果数据库中没有当前的数据那么就插入，如果有就更新
    :param cursor:
    :param db:
    :return:
    '''
    sql = "select * from history_data where Pdate = curdate()"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    if tmp==():   # 插入
        for i in range(1,35):
            sql1 = "insert into history_data values(%s,curdate(),(select count(*) as total from Patient as A1 where A1.Province_id = 1)," \
               "(select count(*) from Patient natural join Patient_status where Province_id = %s and Pstatus = 1)," \
               "(select count(*) from Patient natural join Patient_status where Province_id = %s and Pstatus = 2)," \
               "(select count(*) from Patient natural join Patient_status where Province_id = %s and Pstatus = 3)," \
               "(select count(*) from Patient natural join Patient_status where Province_id = %s and Pstatus = 4))"
            cursor.execute(sql1,[i,i,i,i,i])
            db.commit()

    else:   #更新
        sql2 = "update history_data as A2 set A2.Total_number = (select count(*) from Patient as A1 where A2.Province_id = A1.Province_id)"
        sql3 = "update history_data as A2 set A2.zhiyu = (select count(*) from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A3.Pstatus=1) where A2.Pdate = curdate()"
        sql4 = "update history_data as A2 set A2.yisi = (select count(*) from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A3.Pstatus=2) where A2.Pdate = curdate()"
        sql5 = "update history_data as A2 set A2.xianyou = (select count(*) from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A3.Pstatus=3) where A2.Pdate = curdate()"
        sql6 = "update history_data as A2 set A2.siwang = (select count(*) from Patient as A1 natural join patient_status as A3 where A2.Province_id = A1.Province_id and A3.Pstatus=4) where A2.Pdate = curdate()"
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
        cursor.execute(sql6)
        db.commit()

def GetAllAuth(cursor):
    '''
    获得当前全部授权情况
    :param cursor:
    :return:
    '''
    sql = "select * from authority"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
def GetAuthorityNumber(cursor):
    '''
    确定下一个授权id
    :param cursor:
    :return:
    '''
    sql = "select Auth_id from authority"
    cursor.execute(sql)
    result = cursor.fetchall()
    re = [x[0] for x in result]
    return max(re)
def NewUserAuth(cursor,userid,db):
    auth_id = GetAuthorityNumber(cursor)+1
    sql = "insert into authority(User_id,Province_auth,Auth_type,Auth_id) values (%s,%s,%s,%s)"
    cursor.execute(sql,[userid,0,1,auth_id])
    db.commit()
def GetUserAuthLevel(cursor,userid):
    sql = "select Auth_type from authority where User_id = %s"
    cursor.execute(sql,userid)
    result = cursor.fetchall()
    re = [x[0] for x in result]
    Max_auth = max(re)
    return Max_auth
def GiveAuth(cursor,db,userid,provinceid):
    auth_id = GetAuthorityNumber(cursor) + 1
    sql = "insert into authority(User_id,Province_auth,Auth_type,Auth_id) values (%s,%s,%s,%s)"
    try:

        cursor.execute(sql,[userid,provinceid,2,auth_id])
        db.commit()
        return 1
    except:
        return 0
def RecallAuth(cursor,db,userid,provinceid):
    sql = "delete from authority where User_id = %s and Province_auth = %s"
    try:
        cursor.execute(sql, [userid,provinceid])
        db.commit()
        return 1
    except:
        return 0
def DeleteAuth(cursor,db,userid):
    sql = "delete from authority where User_id = %s and Auth_type=2"
    try:
        cursor.execute(sql,userid)
        db.commit()
        return 1
    except:
        return 0
def ExamAuthRepeat(cursor,userid,provinceid):
    sql = "select * from authority where User_id = %s and Province_auth = %s and Auth_type = 2"
    cursor.execute(sql,[userid,provinceid])
    result = cursor.fetchall()
    if result == ():
        return 0
    else:
        return 1
def GetTwolevelProvince(cursor,userid):
    sql = "select Province_id from authority where User_id = %s and Auth_type = 2"
    cursor.execute(sql,[userid])
    result = cursor.fetchall()
    return result

