import pymysql
db = pymysql.connect("localhost","root","123456a",database="shiyan3",charset="utf8")
cursor = db.cursor()
sql1 = "select count(*) from patient_status natural join patient where province_id = %s"
sql2 = "select count(*) from patient_status natural join patient where province_id = %s and Pstatus = 1"
sql3 = "select count(*) from patient_status natural join patient where province_id = %s and Pstatus = 2"
sql4 = "select count(*) from patient_status natural join patient where province_id = %s and Pstatus = 3"
sql5 = "select count(*) from patient_status natural join patient where province_id = %s and Pstatus = 4"

def gdate(number):
    base = "2020-"
    if number <=31:
        base+="01-"
        base+=str(number)
    elif number>31 and number <=60:
        base+="02-"
        base+=str(number-31)
    elif number>60 and number <=91:
        base+="03-"
        base+=str(number-60)
    elif number>91 and number <=111:
        base+="04-"
        base+=str(number-91)
    return base
l = []
for i in range(1,35):
    li = [i,0,0,0,0,0,0]
    cursor.execute(sql2,i)
    result = cursor.fetchall()
    zhiyu = result[0][0]
    cursor.execute(sql3, i)
    result = cursor.fetchall()
    xianyou = result[0][0]
    cursor.execute(sql4, i)
    result = cursor.fetchall()
    yisi = result[0][0]
    cursor.execute(sql5, i)
    result = cursor.fetchall()
    siwang = result[0][0]
    for j in range(1,112):
        if j%4==0 and li[3]<zhiyu:
            li[3]+=1
        elif j%4 == 1 and li[4]<xianyou:
            li[4]+=1
        elif j%4 == 2 and li[5]<yisi:
            li[5]+=1
        elif j%4 == 3 and li[6]<siwang:
            li[6]+=1
        li[2] = li[3]+li[4]+li[5]+li[6]
        li[1] = gdate(j)
        l.append(tuple(li))

print(l)